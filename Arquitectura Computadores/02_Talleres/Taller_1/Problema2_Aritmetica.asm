#SimuProc 1.4.3.0
; ==============================================================================
; TALLER #1 - ARQUITECTURA DE COMPUTADORES (SIMUPROC)
; PROBLEMA 2: MULTIPLICACIÓN POR PARES Y DIVISIÓN ENTERA
; ==============================================================================
; INTEGRANTES DEL GRUPO:
; 1. [Nombre del Integrante 1] - [ID / Matrícula]
; 2. [Nombre del Integrante 2] - [ID / Matrícula]
; 3. [Nombre del Integrante 3] - [ID / Matrícula]
; 4. [Nombre del Integrante 4] - [ID / Matrícula]
; 5. [Nombre del Integrante 5] - [ID / Matrícula]
; ==============================================================================
; DESCRIPCIÓN DEL PROBLEMA:
; A partir de la dirección #100 se encuentran 6 datos binarios (#100 a #105):
; #100: 101101010001 (12 bits) = 2897 decimal (0x0B51)
; #101: 0100010101101111 (16 bits) = 17775 decimal (0x456F)
;       [Nota: El enunciado indica 110000010100010101101111 de 24 bits = 12666223 dec;
;        en la arquitectura de 16 bits de SimuProc, una palabra almacena 16 bits,
;        correspondiendo a los 16 bits menos significativos 0100010101101111 = 17775 dec]
; #102: 1010 (4 bits) = 10 decimal (0x000A)
; #103: 1111100001111 (13 bits) = 7951 decimal (0x1F0F)
; #104: 11111100 (8 bits) = 252 decimal (0x00FC)
; #105: 110 (3 bits) = 6 decimal (0x0006)
;
; OPERACIONES:
; 1. Multiplicar por pares y almacenar los 3 resultados a partir de #200.
;    Cada producto de 16 bits produce hasta 32 bits, requiriendo 2 posiciones de memoria:
;    - Par 1: dato[100] * dato[101] -> #200 (parte alta / BX) y #201 (parte baja / AX)
;    - Par 2: dato[102] * dato[103] -> #202 (parte alta / BX) y #203 (parte baja / AX)
;    - Par 3: dato[104] * dato[105] -> #204 (parte alta / BX) y #205 (parte baja / AX)
; 2. División entera de dato[103] entre dato[104]:
;    - Resultado ocupa las direcciones inmediatamente posteriores a las multiplicaciones:
;      #206: Cociente (registro AX)
;      #207: Residuo / Resto (registro BX)
; ==============================================================================

            MSG "TALLER 1 - PROBLEMA 2: MULTIPLICACION Y DIVISION"

            ; ==================================================================
            ; MULTIPLICACIÓN PAR 1: dato[100] * dato[101]
            ; 2897 * 17775 = 51494175 (0x0311BD1F)
            ; Parte Alta (BX) = 0x0311 = 785  |  Parte Baja (AX) = 0xBD1F = 48415
            ; ==================================================================
            MSG "--- MULTIPLICACION PAR 1 (100 * 101) ---"
            LDA 100         ; AX = dato[100] (2897 dec)
            MUL 101         ; AX = AX * dato[101] -> AX = parte baja, BX = parte alta
            STA 201         ; Guardar parte baja (AX = 48415) en la dir #201
            MOV 200, BX     ; Guardar parte alta (BX = 785) en la dir #200
            
            ; Visualización en pantalla del Par 1
            EAP "Par 1 - Parte Baja (AX en #201):" ; Muestra AX (48415)
            MOV AX, BX      ; Copiar parte alta a AX para poder mostrarla con EAP
            EAP "Par 1 - Parte Alta (BX en #200):" ; Muestra BX (785)

            ; ==================================================================
            ; MULTIPLICACIÓN PAR 2: dato[102] * dato[103]
            ; 10 * 7951 = 79510 (0x00013696)
            ; Parte Alta (BX) = 0x0001 = 1  |  Parte Baja (AX) = 0x3696 = 13974
            ; ==================================================================
            MSG "--- MULTIPLICACION PAR 2 (102 * 103) ---"
            LDA 102         ; AX = dato[102] (10 dec)
            MUL 103         ; AX = AX * dato[103] -> AX = parte baja, BX = parte alta
            STA 203         ; Guardar parte baja (AX = 13974) en la dir #203
            MOV 202, BX     ; Guardar parte alta (BX = 1) en la dir #202
            
            ; Visualización en pantalla del Par 2
            EAP "Par 2 - Parte Baja (AX en #203):" ; Muestra AX (13974)
            MOV AX, BX      ; Copiar parte alta a AX
            EAP "Par 2 - Parte Alta (BX en #202):" ; Muestra BX (1)

            ; ==================================================================
            ; MULTIPLICACIÓN PAR 3: dato[104] * dato[105]
            ; 252 * 6 = 1512 (0x000005E8)
            ; Parte Alta (BX) = 0x0000 = 0  |  Parte Baja (AX) = 0x05E8 = 1512
            ; ==================================================================
            MSG "--- MULTIPLICACION PAR 3 (104 * 105) ---"
            LDA 104         ; AX = dato[104] (252 dec)
            MUL 105         ; AX = AX * dato[105] -> AX = parte baja, BX = parte alta
            STA 205         ; Guardar parte baja (AX = 1512) en la dir #205
            MOV 204, BX     ; Guardar parte alta (BX = 0) en la dir #204
            
            ; Visualización en pantalla del Par 3
            EAP "Par 3 - Parte Baja (AX en #205):" ; Muestra AX (1512)
            MOV AX, BX      ; Copiar parte alta a AX
            EAP "Par 3 - Parte Alta (BX en #204):" ; Muestra BX (0)

            ; ==================================================================
            ; DIVISIÓN ENTERA: dato[103] / dato[104]
            ; 7951 / 252 = Cociente 31 (0x001F) con Residuo 139 (0x008B)
            ; Verificación: 31 * 252 + 139 = 7812 + 139 = 7951
            ; ==================================================================
            MSG "--- DIVISION: dato[103] / dato[104] ---"
            LDA 103         ; AX = dato[103] (7951 dec, dividendo)
            DIV 104         ; AX = Cociente (31), BX = Residuo (139)
            STA 206         ; Guardar Cociente (AX = 31) en la dir #206
            MOV 207, BX     ; Guardar Residuo (BX = 139) en la dir #207
            
            ; Visualización en pantalla de la División
            EAP "Division - Cociente (AX en #206):" ; Muestra Cociente (31)
            MOV AX, BX      ; Copiar Residuo a AX
            EAP "Division - Residuo (BX en #207):"  ; Muestra Residuo (139)

            MSG "Todas las operaciones concluyeron con exito."
            HLT             ; Detener la CPU

; ==============================================================================
; DATOS BINARIOS EN MEMORIA (A partir de la dirección #100)
; ==============================================================================
#100
101101010001                ; #100: 2897 dec (0x0B51)
0100010101101111            ; #101: 17775 dec (0x456F) [truncado a 16 bits de 110000010100010101101111]
1010                        ; #102: 10 dec (0x000A)
1111100001111               ; #103: 7951 dec (0x1F0F)
11111100                    ; #104: 252 dec (0x00FC)
110                         ; #105: 6 dec (0x0006)
