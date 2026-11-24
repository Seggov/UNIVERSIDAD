#SimuProc 1.4.3.0
; ==============================================================================
; TALLER #1 - ARQUITECTURA DE COMPUTADORES (SIMUPROC)
; PROBLEMA 1: SUCESIÓN DE FIBONACCI GENERALIZADA
; ==============================================================================
; INTEGRANTES DEL GRUPO:
; 1. [Nombre del Integrante 1] - [ID / Matrícula]
; 2. [Nombre del Integrante 2] - [ID / Matrícula]
; 3. [Nombre del Integrante 3] - [ID / Matrícula]
; 4. [Nombre del Integrante 4] - [ID / Matrícula]
; 5. [Nombre del Integrante 5] - [ID / Matrícula]
; ==============================================================================
; DESCRIPCIÓN DEL PROBLEMA:
; En las direcciones de memoria #30 y #31 se encuentran los términos iniciales
; a0 y a1 de una sucesión de Fibonacci (enteros sucesivos <= 30, ej: 20 y 21,
; o la sucesión clásica con 0 y 1).
; Se ingresa por teclado (LDT) la cantidad de términos a generar (máx. 10).
; Regla de recurrencia: a_n = a_{n-2} + a_{n-1}
; Nótese que el primer término generado es a2 = a0 + a1.
; Todos los términos generados se presentan en pantalla (EAP).
; ==============================================================================

            MSG "TALLER 1 - PROBLEMA 1: FIBONACCI"
            
            ; --- PASO 1: MOSTRAR TÉRMINOS INICIALES CONFIGURADOS EN MEMORIA ---
            LDA 30          ; Cargar en AX el término inicial a0 desde la dir #30
            EAP "Termino inicial a0:" ; Mostrar a0 en pantalla
            LDA 31          ; Cargar en AX el término inicial a1 desde la dir #31
            EAP "Termino inicial a1:" ; Mostrar a1 en pantalla

            ; --- PASO 2: INICIALIZAR VARIABLES DE TRABAJO ---
            ; Preservamos las direcciones originales #30 y #31 copiándolas a #32 y #33
            MOV 32, 30      ; mem[32] = a0 (variable para a_{n-2})
            MOV 33, 31      ; mem[33] = a1 (variable para a_{n-1})

            ; --- PASO 3: LECTURA DE CANTIDAD DE TÉRMINOS POR TECLADO ---
            LDT "Cantidad de terminos a generar (max 10):" ; AX = N ingresado por usuario
            STA 35          ; Guardar N en memoria #35 para control
            
            ; --- PASO 4: VALIDACIÓN DE N (Si N <= 0 terminar inmediatamente) ---
            CLA             ; AX = 0
            CMP 35          ; Comparar AX (0) con mem[35] (N). Si N==0 -> Z=1
            JEQ 016         ; Si N == 0, salta al HLT (dir 016)
            JMA 016         ; Si 0 > N (N negativo), salta al HLT (dir 016)
            
            ; --- PASO 5: CARGAR REGISTRO CONTADOR CX ---
            MOV CX, 35      ; CX = N (número de iteraciones para la instrucción LOOP)
            MSG "--- TERMINOS GENERADOS DE LA SUCESION ---"

            ; --- PASO 6: BUCLE DE GENERACIÓN DE FIBONACCI (Dirección 00F) ---
            LDA 32          ; AX = a_{n-2} (término antepenúltimo)
            ADD 33          ; AX = a_{n-2} + a_{n-1} -> nuevo término a_n
            STA 34          ; Guardar nuevo término a_n en memoria #34
            EAP "Termino calculado (an):" ; Presentar a_n en pantalla
            
            ; Desplazamiento de variables para la siguiente iteración:
            ; el nuevo a_{n-2} será el anterior a_{n-1}
            MOV 32, 33      ; mem[32] = mem[33]
            ; el nuevo a_{n-1} será el término a_n recién calculado
            MOV 33, 34      ; mem[33] = mem[34]
            
            LOOP 00F        ; CX = CX - 1; Si CX != 0 salta a la dirección 00F

            ; --- PASO 7: FINALIZACIÓN ---
            MSG "Generacion completada con exito."
            HLT             ; Detener la CPU

; ==============================================================================
; SECCIÓN DE DATOS (Dirección #30 en adelante)
; ==============================================================================
#30
10100                       ; Dir #30: Término inicial a0 = 20 decimal (10100 binario)
10101                       ; Dir #31: Término inicial a1 = 21 decimal (10101 binario)
0                           ; Dir #32: Variable de trabajo a_{n-2}
0                           ; Dir #33: Variable de trabajo a_{n-1}
0                           ; Dir #34: Variable de trabajo a_n (último calculado)
0                           ; Dir #35: Almacenamiento de N (cantidad de términos)
