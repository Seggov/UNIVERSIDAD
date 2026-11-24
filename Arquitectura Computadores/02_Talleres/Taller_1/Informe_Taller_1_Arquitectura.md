# INFORME DE LABORATORIO - TALLER #1: SIMUPROC
**Asignatura:** Arquitectura de Computadores (Período 2026-2)  
**Herramienta:** Simulador de un Procesador Hipotético (SimuProc v1.4.3.0)  
**Tema:** Sucesión de Fibonacci Generalizada y Operaciones Aritméticas de Doble Longitud  

---

## Integrantes del Grupo de Trabajo (Hasta 5 integrantes)

| N° | Nombre Completo del Estudiante | Código / Cédula / Identificación |
|:--:|:-------------------------------|:--------------------------------:|
| 1  | [Nombre y Apellidos del Integrante 1] | [ID / Matrícula] |
| 2  | [Nombre y Apellidos del Integrante 2] | [ID / Matrícula] |
| 3  | [Nombre y Apellidos del Integrante 3] | [ID / Matrícula] |
| 4  | [Nombre y Apellidos del Integrante 4] | [ID / Matrícula] |
| 5  | [Nombre y Apellidos del Integrante 5] | [ID / Matrícula] |

---

## 1. Introducción y Objetivos

### 1.1. Contextualización
El presente informe documenta el desarrollo técnico, análisis algorítmico y verificación matemática de los problemas planteados en el **Taller #1 de Arquitectura de Computadores**. La práctica tiene como propósito comprender la microarquitectura de una CPU basada en acumulador mediante la programación en ensamblador sobre el simulador **SimuProc** (versión 1.4.3.0).

SimuProc modela la arquitectura de Von Neumann clásica, permitiendo visualizar la interacción entre la Unidad Aritmético-Lógica (ALU), el banco de registros, los registros de control/banderas, la memoria principal de 16 bits y el ciclo de instrucción (*Fetch*, *Decode*, *Execute*, *Writeback*).

### 1.2. Objetivos
* **Problema 1 (Sucesión de Fibonacci):** Diseñar e implementar un algoritmo iterativo que genere los primeros $N$ términos ($N \le 10$) de una sucesión de Fibonacci generalizada a partir de dos términos iniciales $a_0$ y $a_1$ ubicados en las posiciones de memoria `#30` y `#31`. Validar la entrada de teclado (`LDT`), el control de flujo con el registro contador `CX` (`LOOP`) y la presentación de resultados en pantalla (`EAP`).
* **Problema 2 (Aritmética de Doble Longitud y División):** Implementar la multiplicación por pares de 6 datos binarios ubicados a partir de `#100` y depositar los resultados a partir de `#200`. Justificar por qué cada producto de 16 bits ocupa dos localidades de memoria (32 bits) distribuidas entre `BX` (alta) y `AX` (baja). Realizar la división entera del dato en `#103` entre el de `#104`, guardando el cociente (`AX`) y el residuo (`BX`) en `#206` y `#207`.
* **Análisis Crítico Hardware:** Examinar el operando de 24 bits presente en la dirección `#101` frente a la restricción arquitectónica de 16 bits por palabra de SimuProc, analizando los efectos del truncamiento y contrastando con el valor teórico decimal.

---

## 2. Arquitectura del Simulador SimuProc

### 2.1. Memoria Principal y Buses
* **Capacidad:** 4.096 posiciones de memoria (palabras) de 16 bits cada una.
* **Direccionamiento:** Hexadecimal desde `000` hasta `FFF` (bus de direcciones de 12 bits).
* **Formato de Instrucción:** En instrucciones de una palabra (16 bits), 4 bits especifican el Código de Operación (`OPCODE`) y 12 bits representan la Dirección de Memoria (`DIR`).

### 2.2. Registros de la CPU
* **AX (Acumulador):** Registro de 16 bits donde convergen las operaciones aritméticas y lógicas, y actúa como canal exclusivo para operaciones de entrada/salida (`LDT`, `EAP`).
* **BX (Base / Index):** Registro de 16 bits usado como base para direccionamiento indexado (`mem+BX`), parte más significativa en multiplicaciones de 32 bits y residuo en divisiones.
* **CX (Counter):** Registro de 16 bits reservado para contar iteraciones en bucles (`LOOP`).
* **PC (Program Counter):** Puntero de instrucción que indica la dirección de memoria de la próxima instrucción a ejecutar.
* **MAR (Memory Address Register) y MDR (Memory Data Register):** Registros de acoplamiento al bus de direcciones y de datos respectivamente.
* **IR (Instruction Register):** Contiene la instrucción en decodificación y ejecución.
* **SP (Stack Pointer) y BP (Base Pointer):** Punteros para la gestión de la pila (por defecto en `F80`).

### 2.3. Registro de Banderas (Flags)
* **Z (Zero):** Se activa (`1`) si el resultado de la última operación fue `0`.
* **N (Negative):** Se activa (`1`) si el bit más significativo (signo) es `1`.
* **C (Carry):** Se activa (`1`) si se produjo acarreo en suma o préstamo en resta.
* **O (Overflow):** Se activa (`1`) si hubo desbordamiento de rango. En `MUL`, se activa cuando el producto excede 16 bits y requiere el registro `BX`.

---

## 3. Problema 1: Sucesión de Fibonacci Generalizada

### 3.1. Planteamiento Matemático
La sucesión de Fibonacci generalizada se define mediante la recurrencia:
$$a_n = a_{n-2} + a_{n-1} \quad \text{para } n \ge 2$$
El enunciado estipula:
* Condiciones iniciales $a_0$ y $a_1$ en `#30` y `#31` como enteros sucesivos $\le 30$ (ej: 20 y 21) y también la sucesión básica ($a_0 = 0, a_1 = 1$).
* Cantidad de términos calculados $N$ ingresada por teclado mediante `LDT` ($N \le 10$).
* El primer término calculado y mostrado es $a_2 = a_0 + a_1$.

### 3.2. Mapa de Memoria y Variables de Trabajo
Para preservar las constantes iniciales en `#30` y `#31` y permitir reejecuciones del programa sin alterar los datos originales, se diseñó el siguiente mapa:

| Dirección | Identificador | Rol en el Algoritmo | Valor Inicial (Caso A / B) |
|:---------:|:-------------|:-------------------|:--------------------------:|
| `#30` (`030h`) | `a0_orig` | Condición inicial $a_0$ | `20` (`10100b`) / `0` (`0b`) |
| `#31` (`031h`) | `a1_orig` | Condición inicial $a_1$ | `21` (`10101b`) / `1` (`1b`) |
| `#32` (`032h`) | `a_prev2` | Variable de trabajo para $a_{n-2}$ | `0` (copiado desde `#30`) |
| `#33` (`033h`) | `a_prev1` | Variable de trabajo para $a_{n-1}$ | `0` (copiado desde `#31`) |
| `#34` (`034h`) | `a_curr`  | Variable para nuevo término $a_n$ | `0` |
| `#35` (`035h`) | `N_terms` | Cantidad de términos $N$ leída por teclado | `0` (leído en runtime) |

### 3.3. Algoritmo Paso a Paso
1. **Lectura y despliegue de condiciones iniciales:** Cargar `#30` y `#31` en `AX` y desplegar con `EAP`.
2. **Preservación:** Copiar `#30` a `#32` y `#31` a `#33` con `MOV`.
3. **Entrada de usuario:** Leer $N$ con `LDT` y guardar en `#35`.
4. **Validación:** Comparar $N$ con 0 (`CLA`, `CMP 35`). Si $N \le 0$, saltar a `HLT` (dirección `016h`).
5. **Inicialización de bucle:** `MOV CX, 35` (el registro `CX` controlará el bucle).
6. **Bucle de cálculo (dirección `00Fh`):**
   * `LDA 32` ($AX \leftarrow a_{n-2}$)
   * `ADD 33` ($AX \leftarrow a_{n-2} + a_{n-1} = a_n$)
   * `STA 34` (almacenar $a_n$)
   * `EAP` (presentar $a_n$ en pantalla)
   * `MOV 32, 33` ($a_{n-2} \leftarrow \text{antiguo } a_{n-1}$)
   * `MOV 33, 34` ($a_{n-1} \leftarrow \text{nuevo } a_n$)
   * `LOOP 00F` (decrementa `CX`; si $CX \ne 0$ repite el bucle)
7. **Terminación:** Mostrar mensaje de fin y detener CPU con `HLT`.

### 3.4. Código Fuente Ensamblador (`Problema1_Fibonacci.asm`)
```asm
#SimuProc 1.4.3.0
; ==============================================================================
; TALLER 1 - PROBLEMA 1: SUCESION DE FIBONACCI GENERALIZADA
; ==============================================================================
            MSG "TALLER 1 - PROBLEMA 1: FIBONACCI"
            
            ; 1. Visualizar terminos iniciales configurados en memoria
            LDA 30          ; AX = mem[30] (Carga termino a0)
            EAP "Termino inicial a0:" ; Imprime a0 en pantalla
            LDA 31          ; AX = mem[31] (Carga termino a1)
            EAP "Termino inicial a1:" ; Imprime a1 en pantalla

            ; 2. Inicializar variables de trabajo para no sobreescribir originales
            MOV 32, 30      ; mem[32] = a0 (variable de trabajo para a_{n-2})
            MOV 33, 31      ; mem[33] = a1 (variable de trabajo para a_{n-1})

            ; 3. Solicitar por teclado la cantidad de terminos N (maximo 10)
            LDT "Cantidad de terminos a generar (max 10):" ; AX = N ingresado
            STA 35          ; mem[35] = N

            ; 4. Validar que N sea estrictamente mayor a cero
            CLA             ; AX = 0
            CMP 35          ; Compara AX (0) con mem[35] (N). Si N==0 activa flag Z
            JEQ 016         ; Si N == 0 salta directamente a la direccion 016 (HLT)
            JMA 016         ; Si 0 > N (N negativo) salta al HLT

            ; 5. Cargar contador CX con el numero de iteraciones
            MOV CX, 35      ; CX = N
            MSG "--- TERMINOS GENERADOS DE LA SUCESION ---"

            ; 6. Bucle de generacion (Direccion 00Fh)
            LDA 32          ; AX = a_{n-2}
            ADD 33          ; AX = a_{n-2} + a_{n-1} -> nuevo termino a_n
            STA 34          ; mem[34] = a_n (almacena el termino calculado)
            EAP "Termino calculado (an):" ; Muestra a_n en pantalla
            
            ; Desplazamiento de variables para la siguiente iteracion
            MOV 32, 33      ; a_{n-2} = mem[33] (antiguo a_{n-1})
            MOV 33, 34      ; a_{n-1} = mem[34] (nuevo termino a_n)
            
            LOOP 00F        ; CX = CX - 1; Si CX != 0 salta a la dir 00Fh

            ; 7. Finalizacion
            MSG "Generacion completada con exito."
            HLT             ; Detener la ejecucion de la CPU

; ==============================================================================
; SECCION DE DATOS (Direccion #30 en adelante)
; ==============================================================================
#30
10100                       ; Dir #30: a0 = 20 decimal (10100 binario)
10101                       ; Dir #31: a1 = 21 decimal (10101 binario)
0                           ; Dir #32: Variable de trabajo a_{n-2}
0                           ; Dir #33: Variable de trabajo a_{n-1}
0                           ; Dir #34: Variable de trabajo a_n
0                           ; Dir #35: Variable N de control
```

### 3.5. Tabla de Traza de Ejecución Paso a Paso
Ejemplo de ejecución con $a_0 = 20, a_1 = 21, N = 5$:

| Paso | PC | Instrucción | AX | BX | CX | Flags (Z,N,C,O) | Acción / Efecto en Memoria |
|:----:|:--:|:------------|:--:|:--:|:--:|:---------------:|:---------------------------|
| 1 | `001` | `LDA 30` | 20 | 0 | 0 | 0, 0, 0, 0 | Carga $a_0$ en `AX` |
| 2 | `002` | `EAP` | 20 | 0 | 0 | 0, 0, 0, 0 | Despliega "Termino inicial a0: 20" |
| 3 | `003` | `LDA 31` | 21 | 0 | 0 | 0, 0, 0, 0 | Carga $a_1$ en `AX` |
| 4 | `004` | `EAP` | 21 | 0 | 0 | 0, 0, 0, 0 | Despliega "Termino inicial a1: 21" |
| 5 | `005` | `MOV 32, 30` | 21 | 0 | 0 | 0, 0, 0, 0 | `mem[32] = 20` |
| 6 | `006` | `MOV 33, 31` | 21 | 0 | 0 | 0, 0, 0, 0 | `mem[33] = 21` |
| 7 | `007` | `LDT` | 5 | 0 | 0 | 0, 0, 0, 0 | Usuario ingresa $N = 5$ |
| 8 | `00D` | `MOV CX, 35` | 0 | 0 | 5 | 0, 1, 0, 0 | `CX = 5` (contador inicial) |
| 9 | `00F` | `LDA 32 + ADD 33` | 41 | 0 | 5 | 0, 0, 0, 0 | $a_2 = 20 + 21 = 41$; `mem[34] = 41` |
| 10 | `015` | `LOOP 00F (it. 1)` | 41 | 0 | 4 | 0, 0, 0, 0 | `EAP: 41`; Desplaza; $CX \leftarrow 4 \ne 0 \Rightarrow$ Salta a `00F` |
| 11 | `015` | `LOOP 00F (it. 2)` | 62 | 0 | 3 | 0, 0, 0, 0 | `EAP: 62`; $a_3 = 21 + 41 = 62$; $CX \leftarrow 3$ |
| 12 | `015` | `LOOP 00F (it. 3)` | 103 | 0 | 2 | 0, 0, 0, 0 | `EAP: 103`; $a_4 = 41 + 62 = 103$; $CX \leftarrow 2$ |
| 13 | `015` | `LOOP 00F (it. 4)` | 165 | 0 | 1 | 0, 0, 0, 0 | `EAP: 165`; $a_5 = 62 + 103 = 165$; $CX \leftarrow 1$ |
| 14 | `015` | `LOOP 00F (it. 5)` | 268 | 0 | 0 | 0, 0, 0, 0 | `EAP: 268`; $a_6 = 103 + 165 = 268$; $CX \leftarrow 0 \Rightarrow$ Sale |
| 15 | `017` | `HLT` | 268 | 0 | 0 | 0, 0, 0, 0 | CPU detenida con éxito |

### 3.6. Validación de Casos de Prueba (10 Términos)

| Término | Recurrencia | Caso A: $a_0=20, a_1=21$ | Caso B: $a_0=0, a_1=1$ | Binario (16 bits) Caso A |
|:-------:|:------------|:------------------------:|:----------------------:|:------------------------:|
| $a_2$ | $a_0 + a_1$ | **41** | **1** | `0000 0000 0010 1001b` (`0029h`) |
| $a_3$ | $a_1 + a_2$ | **62** | **2** | `0000 0000 0011 1110b` (`003Eh`) |
| $a_4$ | $a_2 + a_3$ | **103** | **3** | `0000 0000 0110 0111b` (`0067h`) |
| $a_5$ | $a_3 + a_4$ | **165** | **5** | `0000 0000 1010 0101b` (`00A5h`) |
| $a_6$ | $a_4 + a_5$ | **268** | **8** | `0000 0001 0000 1100b` (`010Ch`) |
| $a_7$ | $a_5 + a_6$ | **433** | **13** | `0000 0001 1011 0001b` (`01B1h`) |
| $a_8$ | $a_6 + a_7$ | **701** | **21** | `0000 0010 1011 1101b` (`02BDh`) |
| $a_9$ | $a_7 + a_8$ | **1134** | **34** | `0000 0100 0110 1110b` (`046Eh`) |
| $a_{10}$ | $a_8 + a_9$ | **1835** | **55** | `0000 0111 0010 1011b` (`072Bh`) |
| $a_{11}$ | $a_9 + a_{10}$ | **2969** | **89** | `0000 1011 1001 1001b` (`0B99h`) |

---

## 4. Problema 2: Multiplicación por Pares y División Entera

### 4.1. Conversión de los Datos Binarios de Entrada
Los 6 datos binarios especificados a partir de la dirección `#100` (`100h` a `105h`) se desglosan a continuación:

| Dirección | Cadena Binaria | Longitud | Hexadecimal | Decimal | Rol Operacional |
|:---------:|:---------------|:--------:|:-----------:|:-------:|:----------------|
| `#100` (`100h`) | `101101010001` | 12 bits | `0B51h` | **2.897** | Multiplicando Par 1 |
| `#101` (`101h`) | `110000010100010101101111` | 24 bits | `C1456Fh` | **12.666.223** | Multiplicador Par 1 (Valor original 24b) |
| `#101` (SimuProc) | `0100010101101111` | 16 bits | `456Fh` | **17.775** | Multiplicador Par 1 (Truncado a 16b) |
| `#102` (`102h`) | `1010` | 4 bits | `000Ah` | **10** | Multiplicando Par 2 |
| `#103` (`103h`) | `1111100001111` | 13 bits | `1F0Fh` | **7.951** | Multiplicador Par 2 / Dividendo |
| `#104` (`104h`) | `11111100` | 8 bits | `00FCh` | **252** | Multiplicando Par 3 / Divisor |
| `#105` (`105h`) | `110` | 3 bits | `0006h` | **6** | Multiplicador Par 3 |

### 4.2. Análisis del Operando de 24 bits frente a la Arquitectura de 16 bits
El dato en `#101` contiene 24 dígitos binarios. Dado que SimuProc implementa celdas de memoria y registros de **16 bits**, el hardware del simulador almacena los 16 bits menos significativos:
$$\text{LSB}_{16}(1100\ 0001\ 0100\ 0101\ 0110\ 1111_2) = 0100\ 0101\ 0110\ 1111_2 = 456F_{16} = 17.775_{10}$$
* **Cálculo con valor nativo SimuProc (16 bits):**
  $$2.897 \times 17.775 = 51.494.175_{10} = \text{0311BD1F}_{16}$$
  * Parte Alta (16 bits más significativos): $\text{0311}_{16} = 785_{10}$ $\rightarrow$ Almacenado en `#200`.
  * Parte Baja (16 bits menos significativos): $\text{BD1F}_{16} = 48.415_{10}$ $\rightarrow$ Almacenado en `#201`.
  * Comprobación: $785 \times 65.536 + 48.415 = 51.445.760 + 48.415 = 51.494.175$.
* **Cálculo con valor teórico de 24 bits:**
  $$2.897 \times 12.666.223 = 36.694.048.031_{10} = 8\ 8910\ \text{F19F}_{16}$$
  Este resultado ocupa 36 bits, lo que excedería la capacidad del par de registros `BX:AX` (32 bits), requiriendo un algoritmo de multiprecisión de tres palabras en software.

### 4.3. Mecánica de la Multiplicación y la División
* **Multiplicación de Doble Longitud (`MUL`):**
  La instrucción `MUL mem` multiplica `AX` por el contenido de memoria. Dado que el producto de dos números de 16 bits puede alcanzar hasta 32 bits, el resultado se descompone en:
  * `BX` $\leftarrow$ Parte más significativa (MSB, bits 16-31).
  * `AX` $\leftarrow$ Parte menos significativa (LSB, bits 0-15).
  Por ello, cada resultado ocupa **dos localidades de memoria contiguas** (orden Big-Endian por palabras en SimuProc):
  * Par 1: `#200` (alta/BX) y `#201` (baja/AX).
  * Par 2: `#202` (alta/BX) y `#203` (baja/AX).
  * Par 3: `#204` (alta/BX) y `#205` (baja/AX).
* **División Entera (`DIV`):**
  La instrucción `DIV 104` divide `AX` (`dato[103]` = 7.951) entre `mem[104]` (`dato[104]` = 252).
  * `AX` $\leftarrow$ Cociente: $\lfloor 7.951 / 252 \rfloor = 31_{10} = \text{001F}_{16}$. Se almacena en `#206`.
  * `BX` $\leftarrow$ Residuo: $7.951 \pmod{252} = 139_{10} = \text{008B}_{16}$. Se almacena en `#207`.
  * Comprobación: $31 \times 252 + 139 = 7.812 + 139 = 7.951$.

### 4.4. Código Fuente Ensamblador (`Problema2_Aritmetica.asm`)
```asm
#SimuProc 1.4.3.0
; ==============================================================================
; TALLER 1 - PROBLEMA 2: MULTIPLICACION POR PARES Y DIVISION ENTERA
; ==============================================================================
            MSG "TALLER 1 - PROBLEMA 2: MULTIPLICACION Y DIVISION"

            ; ==================================================================
            ; MULTIPLICACION PAR 1: dato[100] * dato[101]
            ; 2897 * 17775 = 51494175 (0x0311BD1F)
            ; Parte Alta en #200 (BX = 785) | Parte Baja en #201 (AX = 48415)
            ; ==================================================================
            MSG "--- MULTIPLICACION PAR 1 (100 * 101) ---"
            LDA 100         ; Cargar dato[100] (2897 dec) en AX
            MUL 101         ; AX = AX * dato[101] -> AX=Baja, BX=Alta
            STA 201         ; Guardar Parte Baja (AX) en la direccion #201
            MOV 200, BX     ; Guardar Parte Alta (BX) en la direccion #200
            
            ; Visualizacion en pantalla del Par 1
            EAP "Par 1 - Parte Baja (AX en #201):" ; Muestra 48415
            MOV AX, BX      ; Transferir parte alta a AX para EAP
            EAP "Par 1 - Parte Alta (BX en #200):" ; Muestra 785

            ; ==================================================================
            ; MULTIPLICACION PAR 2: dato[102] * dato[103]
            ; 10 * 7951 = 79510 (0x00013696)
            ; Parte Alta en #202 (BX = 1)   | Parte Baja en #203 (AX = 13974)
            ; ==================================================================
            MSG "--- MULTIPLICACION PAR 2 (102 * 103) ---"
            LDA 102         ; Cargar dato[102] (10 dec) en AX
            MUL 103         ; AX = AX * dato[103] -> AX=Baja, BX=Alta
            STA 203         ; Guardar Parte Baja (AX) en la direccion #203
            MOV 202, BX     ; Guardar Parte Alta (BX) en la direccion #202
            
            ; Visualizacion en pantalla del Par 2
            EAP "Par 2 - Parte Baja (AX en #203):" ; Muestra 13974
            MOV AX, BX      ; Transferir parte alta a AX para EAP
            EAP "Par 2 - Parte Alta (BX en #202):" ; Muestra 1

            ; ==================================================================
            ; MULTIPLICACION PAR 3: dato[104] * dato[105]
            ; 252 * 6 = 1512 (0x000005E8)
            ; Parte Alta en #204 (BX = 0)   | Parte Baja en #205 (AX = 1512)
            ; ==================================================================
            MSG "--- MULTIPLICACION PAR 3 (104 * 105) ---"
            LDA 104         ; Cargar dato[104] (252 dec) en AX
            MUL 105         ; AX = AX * dato[105] -> AX=Baja, BX=Alta
            STA 205         ; Guardar Parte Baja (AX) en la direccion #205
            MOV 204, BX     ; Guardar Parte Alta (BX) en la direccion #204
            
            ; Visualizacion en pantalla del Par 3
            EAP "Par 3 - Parte Baja (AX en #205):" ; Muestra 1512
            MOV AX, BX      ; Transferir parte alta a AX para EAP
            EAP "Par 3 - Parte Alta (BX en #204):" ; Muestra 0

            ; ==================================================================
            ; DIVISION: dato[103] / dato[104]
            ; 7951 / 252 = Cociente 31 (0x001F) con Residuo 139 (0x008B)
            ; Cociente en #206 (AX = 31)    | Residuo en #207 (BX = 139)
            ; ==================================================================
            MSG "--- DIVISION: dato[103] / dato[104] ---"
            LDA 103         ; AX = dato[103] (7951 dec, dividendo)
            DIV 104         ; AX = Cociente (31), BX = Residuo (139)
            STA 206         ; Guardar Cociente (AX) en la direccion #206
            MOV 207, BX     ; Guardar Residuo (BX) en la direccion #207
            
            ; Visualizacion en pantalla de la Division
            EAP "Division - Cociente (AX en #206):" ; Muestra 31
            MOV AX, BX      ; Transferir residuo a AX para EAP
            EAP "Division - Residuo (BX en #207):"  ; Muestra 139

            MSG "Todas las operaciones concluyeron con exito."
            HLT             ; Detener la CPU

; ==============================================================================
; DATOS BINARIOS EN MEMORIA (A partir de la direccion #100)
; ==============================================================================
#100
101101010001                ; #100: 2897 dec (0x0B51)
0100010101101111            ; #101: 17775 dec (0x456F) [truncado a 16 bits de 110000010100010101101111]
1010                        ; #102: 10 dec (0x000A)
1111100001111               ; #103: 7951 dec (0x1F0F)
11111100                    ; #104: 252 dec (0x00FC)
110                         ; #105: 6 dec (0x0006)
```

### 4.5. Tabla Comparativa Exhaustiva con la Forma Decimal

| Operación | Operandos | Decimal Teórico | SimuProc (Memoria) | Desglose Hexadecimal | Comprobación Matemática |
|:----------|:---------:|:---------------:|:------------------:|:--------------------:|:------------------------|
| **Multiplicación Par 1 (16b SimuProc)** | $2.897 \times 17.775$ | **51.494.175** | `#200`: 785<br>`#201`: 48.415 | Alta: `0311h`<br>Baja: `BD1Fh` | $785 \times 65.536 + 48.415 = 51.494.175$ (Exacto) |
| **Multiplicación Par 1 (Teórico 24b)** | $2.897 \times 12.666.223$ | **36.694.048.031** | Excede 32 bits | `8 8910 F19Fh` (3 palabras) | Requiere precisión extendida |
| **Multiplicación Par 2** | $10 \times 7.951$ | **79.510** | `#202`: 1<br>`#203`: 13.974 | Alta: `0001h`<br>Baja: `3696h` | $1 \times 65.536 + 13.974 = 79.510$ (Exacto) |
| **Multiplicación Par 3** | $252 \times 6$ | **1.512** | `#204`: 0<br>`#205`: 1.512 | Alta: `0000h`<br>Baja: `05E8h` | $0 \times 65.536 + 1.512 = 1.512$ (Exacto) |
| **División Entera (103 / 104)** | $7.951 / 252$ | **Cociente: 31**<br>**Residuo: 139** | `#206`: 31<br>`#207`: 139 | Cociente: `001Fh`<br>Residuo: `008Bh` | $31 \times 252 + 139 = 7.951$ (Exacto) |

### 4.6. Volcado de Memoria Final (Memory Dump)

| Dirección | Binario (16 bits) | Hexadecimal | Decimal | Descripción del Contenido |
|:---------:|:-----------------:|:-----------:|:-------:|:--------------------------|
| `#100` (`100h`) | `0000 1011 0101 0001b` | `0B51h` | 2.897 | Multiplicando Par 1 |
| `#101` (`101h`) | `0100 0101 0110 1111b` | `456Fh` | 17.775 | Multiplicador Par 1 (16 bits) |
| `#102` (`102h`) | `0000 0000 0000 1010b` | `000Ah` | 10 | Multiplicando Par 2 |
| `#103` (`103h`) | `0001 1111 0000 1111b` | `1F0Fh` | 7.951 | Multiplicador Par 2 / Dividendo |
| `#104` (`104h`) | `0000 0000 1111 1100b` | `00FCh` | 252 | Multiplicando Par 3 / Divisor |
| `#105` (`105h`) | `0000 0000 0000 0110b` | `0006h` | 6 | Multiplicador Par 3 |
| *---* | *--------------------* | *------* | *-------* | *Posiciones intermedias no alteradas* |
| `#200` (`200h`) | `0000 0011 0001 0001b` | `0311h` | 785 | Par 1: Producto Parte Alta (`BX`) |
| `#201` (`201h`) | `1011 1101 0001 1111b` | `BD1Fh` | 48.415 | Par 1: Producto Parte Baja (`AX`) |
| `#202` (`202h`) | `0000 0000 0000 0001b` | `0001h` | 1 | Par 2: Producto Parte Alta (`BX`) |
| `#203` (`203h`) | `0011 0110 1001 0110b` | `3696h` | 13.974 | Par 2: Producto Parte Baja (`AX`) |
| `#204` (`204h`) | `0000 0000 0000 0000b` | `0000h` | 0 | Par 3: Producto Parte Alta (`BX`) |
| `#205` (`205h`) | `0000 0101 1110 1000b` | `05E8h` | 1.512 | Par 3: Producto Parte Baja (`AX`) |
| `#206` (`206h`) | `0000 0000 0001 1111b` | `001Fh` | 31 | División (103/104): Cociente (`AX`) |
| `#207` (`207h`) | `0000 0000 1000 1011b` | `008Bh` | 139 | División (103/104): Residuo (`BX`) |

---

## 5. Guía de Ejecución y Manual de Usuario en SimuProc

1. **Abrir el Editor Interno:** Ejecutar `Procesador.exe` y seleccionar `Utilidades` $\rightarrow$ `Editor Interno...`.
2. **Cargar Código:** En el **Editor 2 (Editor de Texto)**, pegar el código fuente del programa deseado (`Problema1_Fibonacci.asm` o `Problema2_Aritmetica.asm`).
3. **Compilar y Validar:** Presionar el botón `[<-]` (*Pasa al Editor 1*). El ensamblador validará la sintaxis y reportará cero errores.
4. **Enviar a Memoria:** En el **Editor 1**, presionar el botón `Enviar a Memoria`.
5. **Mostrar Pantalla de E/S:** En la ventana principal de SimuProc, presionar el botón `Mostrar` en el panel de Dispositivos de E/S.
6. **Ejecutar:** Presionar `Ejecutar`. Para el Problema 1, ingresar la cantidad de términos solicitada en el diálogo de teclado (`LDT`). Para el Problema 2, observar las salidas de las multiplicaciones y la división.
7. **Verificación de Memoria:** Consultar directamente las celdas `#200` a `#207` en la tabla de memoria principal de la interfaz para corroborar los resultados.

---

## 6. Conclusiones

1. **Modelo de Acumulador:** Se evidenció la simplicidad y a la vez las limitaciones de una arquitectura de acumulador único (`AX`), donde toda transferencia hacia o desde la ALU o los dispositivos de E/S debe transitar obligatoriamente por dicho registro.
2. **Preservación de Estado:** El diseño de variables de trabajo contiguas para la sucesión de Fibonacci evitó la sobreescritura destructiva de las constantes iniciales en `#30` y `#31`, garantizando idempotencia en la ejecución.
3. **Manejo de Doble Longitud:** La multiplicación en hardware demostró la necesidad de acoplar dos registros (`BX` y `AX`) para albergar el producto de 32 bits de dos palabras de 16 bits sin pérdida de precisión.
4. **Impacto del Ancho de Palabra:** El análisis del operando de 24 bits evidenció que en arquitecturas de palabra fija (16 bits), cualquier exceso es truncado por el bus y la celda física de memoria a menos que se implementen algoritmos de precisión extendida por software.
5. **Eficiencia en la División:** La instrucción `DIV` de SimuProc proporciona de manera atómica el cociente en `AX` y el residuo en `BX`, optimizando notablemente el número de ciclos de reloj frente a esquemas de restas sucesivas.

---

## 7. Referencias Bibliográficas
* **[1]** Stallings, W. (2018). *Organización y Arquitectura de Computadores*. 10ª Edición. Pearson Educación.
* **[2]** Tanenbaum, A. S., & Austin, T. (2013). *Structured Computer Organization*. 6th Edition. Pearson.
* **[3]** Yepes B., V. (2003). *Manual de Referencia y Ayuda en Línea de SimuProc v1.4.3.0*.
* **[4]** Patterson, D. A., & Hennessy, J. L. (2020). *Estructura y Diseño de Computadores: La Interfaz Hardware/Software*. 5ª Edición. Reverté.
