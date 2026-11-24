# INFORME TÉCNICO: ANÁLISIS DE SISTEMAS DIGITALES EN DISPOSITIVOS LCD
## ESTUDIO DE CASO: CONSOLA PORTÁTIL NINTENDO GAME & WATCH: JUDGE (SERIE SILVER, MODELO IP-05)

---

```text
==================== [HOJA 1: PORTADA OFICIAL] ====================
(Nota: Sin número de página visible. Todo centrado vertical y horizontalmente).
```

# UNIVERSIDAD CATÓLICA DEL NORTE
### FACULTAD DE INGENIERÍA Y CIENCIAS GEOLÓGICAS
### ESCUELA DE INGENIERÍA — SEDE COQUIMBO
### DEPARTAMENTO DE INGENIERÍA DE SISTEMAS Y COMPUTACIÓN

**ASIGNATURA:** PROYECTO DE SISTEMAS DIGITALES  
**PERIODO ACADÉMICO:** SEGUNDO SEMESTRE 2026  

---

## INFORME TÉCNICO: ANÁLISIS DE SISTEMAS DIGITALES EN DISPOSITIVOS LCD
### ESTUDIO DE CASO: CONSOLA PORTÁTIL NINTENDO GAME & WATCH: JUDGE (SERIE SILVER, MODELO IP-05)

---

**NOMBRE DEL EQUIPO:**  
RNGPT++  

**INTEGRANTES:**  
• Tomás Sabando — [RUT: XX.XXX.XXX-X] — [correo1@alumnos.ucn.cl]  
• Luis Molina — [RUT: XX.XXX.XXX-X] — [correo2@alumnos.ucn.cl]  
• Pedro Segovia — [RUT: XX.XXX.XXX-X] — [correo3@alumnos.ucn.cl]  

**PROFESOR GUÍA:**  
Ing. Bastian Ruiz Garay  

**FECHA DE ENTREGA:**  
21 de Septiembre de 2026  
Coquimbo, Chile  

```text
==================== [FIN HOJA 1 - SALTO DE PÁGINA: CTRL + ENTER] ====================
```

```text
==================== [HOJA 2: ÍNDICE GENERAL Y GLOSARIO TÉCNICO] ====================
(Nota: En Word generar con "Referencias -> Tabla de contenido -> Tabla automática 1").
```

## ÍNDICE GENERAL

1. INTRODUCCIÓN ................................................................................................ Pág. 3  
2. DESCRIPCIÓN DEL DISPOSITIVO ............................................................................ Pág. 4  
   2.1. Antecedentes Históricos y Contexto Tecnológico .......................................... Pág. 4  
   2.2. Características Físicas, Ergonómicas y Mecánicas ........................................ Pág. 4  
   2.3. Arquitectura Electrónica Interna (Sharp SM510) ............................................. Pág. 4  
   2.4. Principio de Funcionamiento General ......................................................... Pág. 4  
3. ANÁLISIS FUNCIONAL DEL SISTEMA .................................................................... Pág. 5  
   3.1. Reglas y Dinámica Competitiva de Juego ..................................................... Pág. 5  
   3.2. Mapeo de Entradas, Salidas y Antirrebote (Debounce) ..................................... Pág. 5  
   3.3. Formalización de la Máquina de Estados Finitos (FSM) ................................ Pág. 5  
4. LÓGICA COMBINACIONAL, KARNAUGH Y PERTURBACIONES (GLITCHES) .......... Pág. 6  
   4.1. Lógica Combinacional de Arbitraje y Comparación de Magnitud .................... Pág. 6  
   4.2. Análisis Físico de Perturbaciones Dinámicas (Glitches) ................................. Pág. 6  
   4.3. Resolución por Mapa de Karnaugh y Término de Consenso Redundante ......... Pág. 6  
   4.4. Síntesis con Compuertas Universales NAND ................................................. Pág. 6  
   4.5. Diagramas de Flujo del Comportamiento Digital ............................................. Pág. 6  
5. ALCANCE Y FACTIBILIDAD DE IMPLEMENTACIÓN (TTL Y ARDUINO) ....................... Pág. 7  
   5.1. Delimitación Técnica para Maqueta Discreta TTL (74LS) ................................... Pág. 7  
   5.2. Factibilidad Física: Fan-Out y Ruido en Protoboard ............................................ Pág. 7  
   5.3. Estrategia de Migración y Simulación en Arduino ............................................ Pág. 7  
6. PROPUESTAS DE MEJORA MODERNA ....................................................................... Pág. 8  
   6.1. Mejora 1: Generador Pseudoaleatorio Dinámico por LFSR de 8 Bits ................. Pág. 8  
   6.2. Mejora 2: Módulo Secuencial de Pausa Activa (Clock-Gating) ........................... Pág. 8  
   6.3. Mejora 3: Sistema Acústico de Rachas (Combo System con 74LS85) ................. Pág. 8  
   6.4. Mejora 4: Persistencia de Récord de Velocidad (Quickdraw en EEPROM) ................. Pág. 8  
7. CONCLUSIÓN ..................................................................................................... Pág. 9  
8. REFERENCIAS BIBLIOGRÁFICAS .............................................................................. Pág. 10  

---

## GLOSARIO DE TÉRMINOS TÉCNICOS
- **ALU (Arithmetic Logic Unit):** Unidad aritmético-lógica encargada de operaciones matemáticas y comparaciones booleanas.
- **BCD (Binary-Coded Decimal):** Decimal codificado en binario; representa cada dígito decimal (0 a 9) mediante un grupo de 4 bits (*nibble* de 0000 a 1001).
- **Biestable (Flip-Flop):** Circuito secuencial básico capaz de almacenar un bit de información síncrona.
- **Comparador de Magnitud:** Circuito combinacional que contrasta dos palabras binarias determinando si $A > B$, $A < B$ o $A = B$.
- **Clock (Señal de Reloj):** Señal periódica de onda cuadrada que marca el paso temporal de registros y procesadores.
- **Debounce (Antirrebote):** Filtrado circuital o por software para suprimir pulsos falsos generados por el choque mecánico de un botón.
- **FSM (Finite State Machine):** Máquina de estados finitos que describe formalmente las etapas síncronas de funcionamiento.
- **Glitch / Hazard (Perturbación):** Pulso espurio e indeseado originado por diferencias en los retardos de propagación ($t_{pd}$) del silicio.
- **LCD (Liquid Crystal Display):** Pantalla reflectiva pasiva donde las celdas de cristal líquido modulan la luz ambiental.
- **Quickdraw:** Mecánica de desenfunde rápido en situaciones de empate ($A = B$) donde el primer jugador en conectar el golpe gana la ronda.
- **Término de Consenso:** Término booleano redundante que enlaza agrupaciones adyacentes en un mapa de Karnaugh para eliminar perturbaciones.

```text
==================== [FIN HOJA 2 - SALTO DE PÁGINA: CTRL + ENTER] ====================
```

```text
==================== [HOJA 3: INTRODUCCIÓN] ====================
(Nota: Extensión de una página completa. Texto rigurosamente justificado).
```

# 1. INTRODUCCIÓN

A lo largo de las últimas cinco décadas, los sistemas digitales han transformado radicalmente la tecnología moderna y el procesamiento de la información. Antes del surgimiento de los microprocesadores complejos de múltiples núcleos y litografía nanométrica, la industria electrónica sentó las bases de la computación digital moderna a través del empleo riguroso de máquinas secuenciales síncronas, compuertas lógicas universales discretas y arquitecturas de microcontroladores ultra compactos orientados a la máxima eficiencia energética. En este marco histórico y formativo, las consolas portátiles con pantalla de cristal líquido (LCD) de inicios de los años ochenta representan uno de los casos de estudio más didácticos y enriquecedores de la ingeniería digital.

El motivo central de esta investigación radica en analizar cómo un dispositivo de recursos sumamente acotados es capaz de coordinar la lectura simultánea de pulsadores mecánicos para dos jugadores, procesar dinámicas competitivas de reflejos en tiempo real, resolver comparaciones numéricas de magnitud mediante álgebra booleana y excitar matrices gráficas segmentadas en un panel pasivo, todo gobernado por un bus de 4 bits y alimentado por pequeñas pilas de botón que consumen microamperios. Este análisis demuestra a los estudiantes de ingeniería que un sistema interactivo sofisticado no requiere forzosamente de una potencia de cómputo desmedida, sino de un diseño combinacional y secuencial matemáticamente optimizado, inmune a fallos de sincronismo y con retardos físicos rigurosamente controlados.

El objetivo general de este informe consiste en realizar un análisis integral de la arquitectura electrónica, las características físicas y el funcionamiento digital de la consola portátil Nintendo Game & Watch: Judge (modelo IP-05, perteneciente a la histórica Serie Silver de 1980), formalizando sus especificaciones técnicas para proyectar su futura implementación en laboratorio mediante circuitos integrados de lógica discreta TTL serie 74LS y, posteriormente, su emulación en la plataforma Arduino.

Los objetivos específicos son: (1) caracterizar los componentes de hardware originales y su acoplamiento tecnológico; (2) modelar matemáticamente las reglas y el arbitraje de la competencia mediante una Máquina de Estados Finitos (FSM) y ecuaciones booleanas; (3) deducir el fenómeno de perturbaciones transitorias (*glitches*) por retardos de propagación física y su resolución mediante mapas de Karnaugh con términos de consenso; y (4) definir con criterio ingenieril qué módulos se implementarán físicamente en protoboard y cuáles se migrarán a microcontrolador.

Como resultado, este documento proporciona una memoria técnica completa, estructurada y libre de distorsiones conceptuales, que conecta los contenidos teóricos de la asignatura con un proyecto práctico de laboratorio.

```text
==================== [FIN HOJA 3 - SALTO DE PÁGINA: CTRL + ENTER] ====================
```

```text
==================== [HOJA 4: DESCRIPCIÓN DEL DISPOSITIVO] ====================
(Nota: Texto justificado. Citas bibliográficas en formato APA).
```

# 2. DESCRIPCIÓN DEL DISPOSITIVO

### 2.1. Antecedentes Históricos y Contexto Tecnológico
La línea Game & Watch fue creada en 1979 por Gunpei Yokoi, legendario diseñador e ingeniero jefe de Nintendo R&D1, tras observar en el tren bala Shinkansen a un oficinista aburrido que jugaba presionando los botones de una calculadora digital para entretenerse. Nintendo concretó la idea mediante una alianza estratégica con Sharp Corporation, aprovechando sus consolidadas líneas de manufactura de pantallas de cristal líquido reflectivo y circuitos integrados CMOS de bajo consumo (Floyd, 2006).

Dentro de la primera etapa de consolas portátiles, el 4 de octubre de 1980 Nintendo lanzó al mercado Game & Watch: Judge (modelo IP-05), correspondiente al quinto título de la prestigiosa Serie Silver (caracterizada por su placa frontal de aluminio pulido). Judge introdujo una innovación trascendental en la serie: fue el primer videojuego portátil que integró una modalidad multijugador competitiva cara a cara (1 vs 1) en el mismo chasis físico, permitiendo a dos personas competir simultáneamente mediante controles independientes.

### 2.2. Características Físicas, Ergonómicas y Mecánicas
- **Chasis y Masa:** Carcasa moldeada en termoplástico ABS de alta resistencia con frontal de aluminio pulido anodizado (95 mm de ancho, 63 mm de alto y 12 mm de grosor; masa total de 55 gramos incluyendo pilas).
- **Interfaz de Usuario:** Dispone de cuatro pulsadores de juego principales construidos con membranas de goma conductiva sobre pistas de PCB entrelazadas: dos a la izquierda para el Jugador 1 ("Attack" y "Dodge") y dos a la derecha para el Jugador 2 ("Attack" y "Dodge"). Incorpora además cuatro botones auxiliares embutidos: *Game A* (1 Jugador vs CPU), *Game B* (2 Jugadores), *Time* (Reloj) y el interruptor hundido *ACL* (*All Clear* / Reset maestro).
- **Pantalla:** Panel LCD monocromático reflectivo TN (*Twisted Nematic*) con segmentos gráficos personalizados que representan a los dos jueces con sus mazos, posturas de esquiva, carteles numéricos del 1 al 9 y dígitos de puntuación.
- **Alimentación Eléctrica:** Dos pilas de botón de óxido de plata o alcalinas tipo LR43/SR43 en serie (3,0 V DC), con un consumo en reposo inferior a 15 microamperios ($\mu\text{A}$).

### 2.3. Arquitectura Electrónica Interna (Sharp SM510)
El sistema opera gobernado por un microcontrolador CMOS monolítico de 4 bits **Sharp SM510** bajo arquitectura Harvard pura:
- **CPU de 4 bits (Nibble):** Su bus nativo de 4 bits manipula directamente números en código BCD (0 al 9), ideal para comparar los carteles y registrar los puntajes sin requerir subrutinas complejas de conversión binario-decimal.
- **Memorias Integradas:** ROM de máscara de 1,8 KB (1.820 palabras de 8 bits) con el firmware grabado de fábrica, y RAM estática de 65 *nibbles* (260 bits totales) para variables dinámicas (números de los carteles, puntajes y registros horarios).
- **Base de Tiempo de Cuarzo:** Cristal de cuarzo de 32.768 Hz ($2^{15}\text{ Hz}$) acoplado a 15 divisores asíncronos en cascada (*ripple counters*) que entregan pulsos síncronos de 1 Hz exactos para el reloj y frecuencias de 512 Hz a 2 kHz para el audio.
- **Excitación LCD y Sonido:** Drivers *push-pull* de corriente alterna (AC) para proteger el cristal líquido y disco cerámico piezoeléctrico de resonancia mecánica.

### 2.4. Principio de Funcionamiento
En modo Reloj (Standby), la CPU permanece en bajo consumo (*Halt*), despertando cada 1 segundo para refrescar la hora. En modo Juego (Activo), ejecuta un bucle síncrono que genera los números aleatorios, abre la ventana de reacción de 1 a 2 segundos, muestrea los 4 botones con filtro antirrebote y arbitra la puntuación.

```text
==================== [FIN HOJA 4 - SALTO DE PÁGINA: CTRL + ENTER] ====================
```

```text
==================== [HOJA 5: ANÁLISIS FUNCIONAL Y FSM] ====================
(Nota: Texto justificado. Formalización matemática de estados).
```

# 3. ANÁLISIS FUNCIONAL DEL SISTEMA

### 3.1. Reglas y Dinámica Competitiva de Juego
Game & Watch: Judge es un juego de reflejos y comparación de magnitudes entre dos personajes que sostienen un mazo:
- **Inicio de Ronda:** Tras una breve cuenta regresiva, ambos personajes levantan simultáneamente un cartel con un número aleatorio entre 1 y 9 ($N_1$ para Jugador 1, $N_2$ para Jugador 2).
- **Caso 1: Jugador 1 tiene el número mayor ($N_1 > N_2$):** La acción correcta para J1 es Atacar y para J2 es Esquivar. Si J1 golpea antes de que J2 esquive, J1 recibe **+3 puntos**. Si J2 esquiva a tiempo hacia atrás, J2 recibe **+2 puntos**.
- **Caso 2: Jugador 1 tiene el número menor ($N_1 < N_2$):** La situación es simétrica invertida: J2 debe Atacar (+3 puntos si conecta) y J1 debe Esquivar (+2 puntos si evade).
- **Caso 3: Empate Numérico ($N_1 = N_2$ / Quickdraw):** Ningún jugador debe esquivar; ambos deben Atacar. El primer jugador en conectar el golpe gana **+3 puntos**.
- **Penalización por Acción Inversa (Error de Juicio):** Si un jugador ataca teniendo el número menor, o esquiva teniendo el número mayor, comete una falta grave y el oponente recibe **+2 puntos** inmediatamente.
- **Condición de Victoria:** El juego se desarrolla por rondas sucesivas hasta que el primer participante alcanza los **50 puntos** acumulados.

### 3.2. Mapeo de Entradas, Salidas y Acondicionamiento Antirrebote
- **Entradas:** 4 botones de juego con resistencia *pull-up*: $Atk_1$ y $Ddg_1$ (Jugador 1), $Atk_2$ y $Ddg_2$ (Jugador 2), más los selectores *Game A*, *Game B*, *Time* y *ACL*. Para evitar pulsaciones espurias causadas por el rebote elástico metálico (5 a 20 ms), se implementan cerrojos biestables RS construidos con compuertas NAND 74LS00.
- **Salidas:** Segmentos de personajes (postura normal, ataque con mazo, esquiva hacia atrás), carteles numéricos con dígitos BCD, bus de 7 segmentos para los puntajes de J1 y J2 (hasta 50), y transductor piezoeléctrico de audio.

### 3.3. Formalización de la Máquina de Estados Finitos (FSM)
El comportamiento síncrono del sistema se modela formalmente mediante una FSM de 5 estados ($q_0$ a $q_4$):
- **$q_0$ (Standby / Reloj RTC):** Bucle de bajo consumo. El oscilador actualiza la hora a 1 Hz en pantalla. Al presionar *Game A* o *Game B*, conmuta al estado $q_1$.
- **$q_1$ (Inicialización y Puesta a Cero):** Limpia a cero los registros de puntuación BCD ($Score_1 = 00, Score_2 = 00$), borra los carteles y transiciona incondicionalmente a $q_2$.
- **$q_2$ (Countdown y Generación Pseudoaleatoria):** Ejecuta una cuenta regresiva estroboscópica y genera dos valores BCD ($N_1$ y $N_2$ entre 1 y 9). Revela los carteles y salta inmediatamente a $q_3$.
- **$q_3$ (Ventana de Reacción y Arbitraje Combinacional):** Abre una ventana de tiempo de reacción (1 a 2 segundos). La red combinacional muestrea las entradas y evalúa el comparador de magnitud ($N_1$ vs $N_2$). Asigna los +3 puntos al golpe certero, +2 puntos a la esquiva o +2 puntos por falta inversa. Actualiza los contadores BCD y evalúa si algún jugador llegó a 50 puntos. Si nadie ha ganado, retorna a $q_2$; si un puntaje alcanza 50, salta a $q_4$.
- **$q_4$ (Game Over y Celebración):** Detiene la generación de rondas, muestra la animación de victoria del ganador, hace parpadear el marcador final a 2 Hz y bloquea mandos hasta recibir un reset manual.

```text
==================== [FIN HOJA 5 - SALTO DE PÁGINA: CTRL + ENTER] ====================
```

```text
==================== [HOJA 6: LÓGICA COMBINACIONAL Y KARNAUGH] ====================
(Nota: Deducción booleana rigurosa y diagramas de flujo).
```

# 4. LÓGICA COMBINACIONAL, KARNAUGH Y PERTURBACIONES (GLITCHES)

### 4.1. Lógica Combinacional de Arbitraje y Comparación de Magnitud
El núcleo del arbitraje en Judge se sustenta en un comparador de magnitud binario de 4 bits (IC 74LS85) que contrasta el cuarteto de bits del Jugador 1 ($A = N_1$) contra el cuarteto del Jugador 2 ($B = N_2$), entregando tres líneas booleanas activas en nivel alto: $(A > B)$, $(A < B)$ y $(A = B)$.

Para validar la habilitación del golpe ganador del Jugador 1 en sincronismo con la ventana de arbitraje temporal, definimos tres variables booleanas:
- **$A$:** Condición de superioridad numérica o prioridad de ataque confirmada por el comparador ($A = 1$ indica $N_1 \ge N_2$).
- **$B$:** Acción física de ataque ejecutada por el Jugador 1 ($B = Atk_1 = 1$).
- **$C$:** Señal estroboscópica de validación de ventana temporal emitida por el temporizador maestro ($C = 1$).

La función lógica teórica de conmutación de bus y verificación de impacto corresponde a:
$$F(A, B, C) = A\bar{C} + BC$$

### 4.2. Análisis Físico de Perturbaciones Dinámicas (Glitches)
Analicemos qué ocurre en el silicio real cuando las entradas se mantienen estables en $A = 1$ y $B = 1$, mientras que la señal de temporización $C$ conmuta de nivel alto a bajo ($C: 1 \to 0$):
- *En teoría booleana ideal:* Dado que $A = 1$ y $B = 1$, el término $BC$ pasa de 1 a 0 y $A\bar{C}$ pasa de 0 a 1; por ende, la función debiese permanecer fija en nivel alto ($F = 1$).
- *En el silicio real:* La compuerta inversora NOT encargada de sintetizar $\bar{C}$ presenta un retardo de propagación finito ($t_{pd}$). Durante el intervalo transitorio $\Delta t = t_{pd}$, tanto $C$ como $\bar{C}$ son interpretados simultáneamente en nivel bajo ($0$). En consecuencia, $BC$ cae a 0 antes de que $A\bar{C}$ logre subir a 1, produciendo una **caída transitoria espuria a nivel bajo ($1 \to 0 \to 1$)**. Este impulso falso es lo que se conoce como Perturbación Dinámica (*Glitch*), y en el juego provocaría un falso conteo de puntos o un disparo erróneo de penalización.

### 4.3. Resolución por Mapa de Karnaugh y Término de Consenso
Graficando la función en el mapa de Karnaugh de 3 variables:
```text
        AB
   C    00   01   11   10
   0     0    0   [1    1]   --> Agrupación A·C' (m4, m6)
   1     0   [1    1]   0    --> Agrupación B·C  (m3, m7)
```
Las agrupaciones colindan en la celda $AB = 11$ pero no comparten un lazo directo de cobertura. Para blindar el circuito contra perturbaciones, incorporamos el **término de consenso redundante $AB$** (adyacencia entre $m_6$ y $m_7$):
$$F_{segura}(A, B, C) = A\bar{C} + BC + AB$$

Al añadir la compuerta AND para $AB$, mientras $A = 1$ y $B = 1$ dicha rama mantiene la salida afianzada en nivel alto independientemente de las transiciones y retardos de $C$, eliminando completamente el *glitch*.

### 4.4. Síntesis Universal con Compuertas NAND
Aplicando el teorema de DeMorgan (Clase 07 de la cátedra), la función se sintetiza íntegramente con compuertas NAND 74LS00:
$$F_{segura} = \overline{\overline{A\bar{C} + BC + AB}} = \overline{\overline{(A\bar{C})} \cdot \overline{(BC)} \cdot \overline{(AB)}}$$

### 4.5. Diagramas de Flujo del Comportamiento Digital
- **Bucle Maestro:** Arranque/Reset $\to$ Selección de Modo (Time vs Game A/B) $\to$ Cuenta regresiva $\to$ Generación de $N_1$ y $N_2$ $\to$ Apertura de ventana de reacción $\to$ Muestreo de botones con antirrebote $\to$ Salto a subrutina de arbitraje.
- **Subrutina de Arbitraje:** Compara $N_1$ vs $N_2$ con el 74LS85. Si $N_1 > N_2$: premia ataque de J1 (+3) o esquiva de J2 (+2), o penaliza acción inversa (+2 al rival). Si $N_1 = N_2$: premia al primer botón de ataque (+3). Actualiza contadores BCD y verifica si $Score_1$ o $Score_2$ alcanzó 50 puntos para derivar a *Game Over*.

```text
==================== [FIN HOJA 6 - SALTO DE PÁGINA: CTRL + ENTER] ====================
```

```text
==================== [HOJA 7: ALCANCE Y FACTIBILIDAD] ====================
(Nota: Delimitación fundamentada de ingeniería).
```

# 5. ALCANCE Y FACTIBILIDAD DE IMPLEMENTACIÓN (TTL Y ARDUINO)

### 5.1. Delimitación Técnica para Maqueta Discreta TTL (74LS)
Considerando las restricciones de tiempo semestral y recursos de laboratorio, se establece una delimitación técnica fundamentada entre lo implementable en protoboard y lo que será omitido:

- **Módulos que SERÁN IMPLEMENTADOS en Protoboard:**
  1. *Bloque Comparador de Magnitud:* Circuito integrado 74LS85 que contrasta las entradas numéricas $N_1$ y $N_2$ en BCD.
  2. *Cerrojos Antirrebote y Pulsadores:* Cuatro cerrojos biestables RS construidos con compuertas NAND 74LS00 para estabilizar $Atk_1, Ddg_1, Atk_2$ y $Ddg_2$.
  3. *Lógica Combinacional de Arbitraje Anti-Glitch:* Red de compuertas universales NAND (74LS00) con término de consenso.
  4. *Contadores de Puntuación BCD:* Dos contadores síncronos de décadas (74LS160) y decodificadores a 7 segmentos (74LS47) para visualizar los marcadores.
  5. *Base de Tiempo de Ronda:* Oscilador astable basado en el temporizador integrado NE555 regulable por potenciómetro.

- **Módulos OMITIDOS en la Maqueta Cableada y Justificación Técnica:**
  1. *Algoritmo de Inteligencia Artificial de la CPU (Modo Game A):* Omitido en compuertas discretas debido a que implementar la toma de decisiones probabilística y tiempos de reacción variables exigiría más de 20 circuitos integrados auxiliares, superando los límites de abanico de salida (*Fan-Out* $N = 10$) y saturando el alambrado en protoboard.
  2. *Reloj Horario de 24 Horas y Panel LCD a Medida:* Se sustituyen por LEDs y visualizadores de 7 segmentos estándar para enfocar el esfuerzo en la lógica competitiva y evitar fallas por ruido capacitivo e inductivo en placa de pruebas.

### 5.2. Estrategia de Migración y Emulación en Arduino
En la siguiente fase, la arquitectura se portará a un microcontrolador ATmega328P (Arduino Uno):
- **Arquitectura No Bloqueante:** Control temporal estricto mediante la función `millis()` y máquinas de estado `switch-case`, descartando por completo funciones bloqueantes (`delay()`) para garantizar una lectura inmediata de los reflejos de los jugadores.
- **Acondicionamiento por Software:** Activación de resistencias internas `INPUT_PULLUP` y algoritmo de debounce temporal de 15 ms.
- **Interfaz Gráfica OLED I2C y Audio:** Pantalla gráfica OLED de 0,96 pulgadas (128x64 px) gobernada por bus I2C (pines SDA/SCL) para dibujar a los personajes con mazos y carteles, y generación de tonos acústicos con `tone()`.
- **Levantamiento de Restricciones:** En Arduino se programa con naturalidad la máquina de estados del rival virtual (CPU para Game A) y el almacenamiento permanente del récord en memoria EEPROM.

```text
==================== [FIN HOJA 7 - SALTO DE PÁGINA: CTRL + ENTER] ====================
```

```text
==================== [HOJA 8: PROPUESTAS DE MEJORA] ====================
(Nota: 4 propuestas fundamentadas con impacto en entradas, salidas y estados).
```

# 6. PROPUESTAS DE MEJORA MODERNA

Se plantean cuatro propuestas de ingeniería digital que modernizan Game & Watch: Judge sin alterar su esencia clásica:

### 6.1. Mejora 1: Generador Pseudoaleatorio Dinámico por LFSR de 8 Bits
- **Justificación Técnica:** En el juego original, los números de los carteles se generaban con secuencias cíclicas fijas que jugadores expertos lograban predecir. Se propone incorporar un Registro de Desplazamiento con Retroalimentación Lineal (LFSR) de 8 bits con polinomio irreducible ($P(x) = x^8 + x^6 + x^5 + x^4 + 1$) mediante compuertas XOR (74LS86), asegurando una distribución pseudoaleatoria real y uniforme de los números de los carteles (1 a 9).
- **Impacto Técnico:** Elimina la predictibilidad de los números dentro del estado de preparación $q_2$.

### 6.2. Mejora 2: Módulo Secuencial de Pausa Activa (Clock-Gating)
- **Justificación Técnica:** La consola clásica carecía de función de pausa, obligando a perder la partida ante cualquier interrupción externa. Se implementa una compuerta lógica de paso (*Clock-Gating*) comandada por un botón 'Pause' ($B_P$) y un biestable Toggle, que aísla la señal de reloj síncrono.
- **Impacto Técnico:** Crea el estado formal $q_{pause}$ sin alterar los puntajes BCD acumulados ni las variables de ronda.

### 6.3. Mejora 3: Sistema Acústico de Rachas (Combo System con 74LS85)
- **Justificación Técnica:** El sonido original consistía en pitidos planos y monótonos. Se diseña un circuito con un contador de golpes y esquivas exitosas continuas conectado a un comparador de magnitud binaria de 4 bits (74LS85) que, al llegar a umbrales (5, 10 o 15 aciertos seguidos), conmuta un multiplexor (74LS151) para emitir arpegios de victoria y otorgar bonificaciones sonoras diferenciadas.
- **Impacto Técnico:** Añade modulación sonora polifónica de 500 Hz a 2 kHz dentro de la subrutina de arbitraje $q_3$.

### 6.4. Mejora 4: Persistencia de Récord de Velocidad (Quickdraw en EEPROM)
- **Justificación Técnica:** El tiempo de reacción récord de los jugadores se perdía al apagar la consola. Se propone un temporizador contador de milisegundos que registra la velocidad del golpe en empates ($A = B$) y la contrasta mediante comparadores contra el récord histórico guardado en memoria.
- **Impacto Técnico:** Preserva permanentemente el mejor tiempo de desenfunde en memoria EEPROM no volátil para su visualización en *Game Over* ($q_4$).

```text
==================== [FIN HOJA 8 - SALTO DE PÁGINA: CTRL + ENTER] ====================
```

```text
==================== [HOJA 9: CONCLUSIÓN] ====================
(Nota: Extensión de una página completa. Síntesis y proyección práctica).
```

# 7. CONCLUSIÓN

El desarrollo de la presente memoria técnica en torno a la consola portátil Nintendo Game & Watch: Judge (modelo IP-05, Serie Silver de 1980) permitió articular los contenidos teóricos de la cátedra de Sistemas Digitales con un producto comercial masivo de notable relevancia histórica, demostrando cómo la ingeniería de diseño optimiza recursos mínimos para implementar una experiencia interactiva y competitiva en tiempo real bajo severas restricciones de silicio y energía.

A través del análisis anatómico y el modelado funcional, se comprobó que una dinámica competitiva de dos jugadores con arbitraje de acciones concurrentes puede modelarse enteramente a partir del acoplamiento estructurado de comparadores de magnitud digital (74LS85), cerrojos antirrebote con compuertas universales NAND, contadores decimales BCD y una Máquina de Estados Finitos (FSM) síncrona de cinco estados ($q_0$ a $q_4$). Este enfoque demostró que el procesamiento nativo en palabras de 4 bits (*nibbles*) es ideal para manipular directamente dígitos decimales sin desperdicio de compuertas.

Uno de los aportes formativos de mayor peso radicó en el análisis de los retardos físicos de propagación ($t_{pd}$) y la detección de perturbaciones dinámicas (*glitches*) en la función combinacional de impacto y arbitraje. Se demostró matemáticamente que los mapas de Karnaugh no solo actúan como herramientas de simplificación booleana, sino como un método preventivo fundamental de diseño: la adición deliberada del término de consenso redundante $AB$ en la función minimizada asegura que las transiciones del temporizador estroboscópico no generen caídas espurias a nivel bajo, blindando el circuito contra falsos cobros de puntos o penalizaciones erróneas.

Asimismo, la delimitación consciente del alcance físico para la futura maqueta de circuitos integrados discretos TTL serie 74LS frente a la posterior simulación en microcontrolador Arduino aportó un valioso criterio de gestión técnica. Reconocer las limitaciones de corriente de carga (*Fan-Out* $N = 10$), el ruido electromagnético y la congestión de alambrado en protoboard permite concentrar el trabajo de laboratorio en el núcleo del arbitraje (comparador de números, cerrojos de botones y conteo de puntaje), postergando con fundamento el algoritmo de CPU del rival virtual hacia la etapa embebida.

En conclusión, este trabajo consolida las competencias de modelado, diseño combinacional y lógica secuencial, entregando una memoria técnica rigurosa y libre de errores para sustentar con éxito las próximas etapas evaluativas de la asignatura.

```text
==================== [FIN HOJA 9 - SALTO DE PÁGINA: CTRL + ENTER] ====================
```

```text
==================== [HOJA 10: REFERENCIAS BIBLIOGRÁFICAS] ====================
(Nota: Formato APA 7ma edición con sangría francesa de 1,27 cm).
```

# 8. REFERENCIAS BIBLIOGRÁFICAS

Floyd, T. L. (2006). *Fundamentos de sistemas digitales* (9.ª ed.). Pearson Educación.  
Mano, M. M., & Ciletti, M. D. (2013). *Diseño digital: Con una introducción a Verilog HDL* (5.ª ed.). Pearson Educación.  
Nintendo Co., Ltd. (1980). *Game & Watch: Judge (Model IP-05) Service & Instruction Manual*. Nintendo R&D1.  
Sharp Corporation. (1980). *SM-5xx Series 4-bit Single Chip Microcomputer User's Manual*. Sharp Electronic Components.  
Tocci, R. J., Widmer, N. S., & Moss, G. L. (2007). *Sistemas digitales: Principios y aplicaciones* (10.ª ed.). Pearson Educación.  
Wakerly, J. F. (2001). *Diseño digital: Principios y prácticas* (3.ª ed.). Pearson Educación.  

```text
==================== [FIN HOJA 10 - FIN DEL INFORME] ====================
```
