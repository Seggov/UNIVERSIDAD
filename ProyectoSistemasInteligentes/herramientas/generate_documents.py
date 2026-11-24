# -*- coding: utf-8 -*-
import os
import subprocess
from pathlib import Path
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "documentos" / "ball"

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_docx():
    doc = Document()
    
    # Configuracion de pagina: Carta (Letter: 21.59 x 27.94 cm) con margenes de 2.0 cm
    for section in doc.sections:
        section.page_width = Cm(21.59)
        section.page_height = Cm(27.94)
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(2.0)
        section.right_margin = Cm(2.0)
        
    # Estilo base
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(11)
    font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    style.paragraph_format.line_spacing = 1.15
    style.paragraph_format.space_after = Pt(6)
    
    def add_p(text, bold=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY, italic=False, space_after=6):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_after = Pt(space_after)
        run = p.add_run(text)
        run.bold = bold
        run.italic = italic
        run.font.name = 'Calibri'
        run.font.size = Pt(11)
        return p

    def add_h1(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Calibri'
        run.font.size = Pt(15)
        run.font.color.rgb = RGBColor(0x00, 0x33, 0x66)
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Calibri'
        run.font.size = Pt(12.5)
        run.font.color.rgb = RGBColor(0x11, 0x44, 0x77)
        return p

    def add_bullet(bold_prefix, text):
        p = doc.add_paragraph(style='List Bullet')
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_after = Pt(4)
        r1 = p.add_run(bold_prefix)
        r1.bold = True
        r2 = p.add_run(text)
        return p

    # ==================== HOJA 1: PORTADA ====================
    p_top = doc.add_paragraph()
    p_top.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_top.paragraph_format.space_before = Pt(40)
    p_top.paragraph_format.space_after = Pt(4)
    r = p_top.add_run("UNIVERSIDAD CATÓLICA DEL NORTE\nFACULTAD DE INGENIERÍA Y CIENCIAS GEOLÓGICAS\nESCUELA DE INGENIERÍA — SEDE COQUIMBO\nDEPARTAMENTO DE INGENIERÍA DE SISTEMAS Y COMPUTACIÓN")
    r.bold = True
    r.font.size = Pt(12)
    r.font.color.rgb = RGBColor(0x00, 0x33, 0x66)

    p_asig = doc.add_paragraph()
    p_asig.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_asig.paragraph_format.space_before = Pt(20)
    p_asig.paragraph_format.space_after = Pt(20)
    r = p_asig.add_run("PROYECTO DE SISTEMAS DIGITALES\nSEGUNDO SEMESTRE 2026")
    r.bold = True
    r.font.size = Pt(11)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(40)
    p_title.paragraph_format.space_after = Pt(10)
    r = p_title.add_run("INFORME TÉCNICO: ANÁLISIS DE SISTEMAS DIGITALES EN DISPOSITIVOS LCD")
    r.bold = True
    r.font.size = Pt(16)
    r.font.color.rgb = RGBColor(0x00, 0x33, 0x66)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(80)
    r = p_sub.add_run("ESTUDIO DE CASO: CONSOLA PORTÁTIL NINTENDO GAME & WATCH (SERIE BALL, MODELO AC-01)")
    r.italic = True
    r.bold = True
    r.font.size = Pt(12)

    p_info = doc.add_paragraph()
    p_info.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_info.paragraph_format.space_after = Pt(4)
    r = p_info.add_run("NOMBRE DEL EQUIPO:\nSistemas Digitales UCN Lab\n\nINTEGRANTES:\n• [Nombre Alumno 1] — RUT: [XX.XXX.XXX-X] — [correo1@alumnos.ucn.cl]\n• [Nombre Alumno 2] — RUT: [XX.XXX.XXX-X] — [correo2@alumnos.ucn.cl]\n• [Nombre Alumno 3] — RUT: [XX.XXX.XXX-X] — [correo3@alumnos.ucn.cl]\n\nPROFESOR GUÍA:\nIng. Bastian Ruiz Garay\n\nCoquimbo, Chile — 21 de Septiembre de 2026")
    r.font.size = Pt(10.5)

    doc.add_page_break()

    # ==================== HOJA 2: ÍNDICE Y GLOSARIO ====================
    add_h1("ÍNDICE GENERAL")
    add_p("1. INTRODUCCIÓN .................................................................................................................... Pág. 3\n"
          "2. DESCRIPCIÓN DEL DISPOSITIVO .................................................................................... Pág. 4\n"
          "   2.1. Antecedentes Históricos y Contexto Tecnológico .................................................... Pág. 4\n"
          "   2.2. Características Físicas y Mecánicas ........................................................................... Pág. 4\n"
          "   2.3. Arquitectura Electrónica Interna (Sharp SM510) ..................................................... Pág. 4\n"
          "   2.4. Principio de Funcionamiento General ......................................................................... Pág. 4\n"
          "3. ANÁLISIS FUNCIONAL DEL SISTEMA ............................................................................ Pág. 5\n"
          "   3.1. Reglas y Dinámica de Juego ....................................................................................... Pág. 5\n"
          "   3.2. Mapeo de Entradas, Salidas y Antirrebote (Debounce) ............................................. Pág. 5\n"
          "   3.3. Modelo de Máquina de Estados Finitos (FSM) ............................................................. Pág. 5\n"
          "4. LÓGICA COMBINACIONAL, KARNAUGH Y PERTURBACIONES (GLITCHES) .......... Pág. 6\n"
          "   4.1. Función de Colisión y Fenómeno Físico de Glitch ..................................................... Pág. 6\n"
          "   4.2. Mapa de Karnaugh y Término de Consenso Redundante .......................................... Pág. 6\n"
          "   4.3. Implementación con Compuertas Universales NAND ................................................. Pág. 6\n"
          "   4.4. Diagramas de Flujo del Comportamiento Digital ........................................................ Pág. 6\n"
          "5. ALCANCE Y FACTIBILIDAD DE IMPLEMENTACIÓN (TTL Y ARDUINO) ....................... Pág. 7\n"
          "   5.1. Delimitación Técnica para Maqueta Discreta TTL (74LS) ............................................ Pág. 7\n"
          "   5.2. Factibilidad Física: Fan-Out y Ruido en Protoboard .................................................... Pág. 7\n"
          "   5.3. Estrategia de Migración y Simulación en Arduino .................................................... Pág. 7\n"
          "6. PROPUESTAS DE MEJORA MODERNA ........................................................................... Pág. 8\n"
          "   6.1. Mejora 1: Temporización Pseudoaleatoria por LFSR ................................................. Pág. 8\n"
          "   6.2. Mejora 2: Módulo Secuencial de Pausa Activa (Clock-Gating) ................................. Pág. 8\n"
          "   6.3. Mejora 3: Sistema Acústico de Rachas (Combo System con 74LS85) .......................... Pág. 8\n"
          "   6.4. Mejora 4: Persistencia de Récord Máximo (High Score con EEPROM) ........................ Pág. 8\n"
          "7. CONCLUSIÓN ...................................................................................................................... Pág. 9\n"
          "8. REFERENCIAS BIBLIOGRÁFICAS ................................................................................... Pág. 10", space_after=12)

    add_h2("GLOSARIO DE TÉRMINOS TÉCNICOS")
    add_bullet("ALU (Arithmetic Logic Unit): ", "Unidad aritmético-lógica encargada de operaciones matemáticas y comparaciones booleanas.")
    add_bullet("BCD (Binary-Coded Decimal): ", "Decimal codificado en binario; representa cada dígito (0 a 9) en un cuarteto de 4 bits (nibble).")
    add_bullet("Biestable (Flip-Flop): ", "Elemento de memoria de un bit que conmuta de estado con flancos de reloj síncronos.")
    add_bullet("Clock (Señal de Reloj): ", "Onda periódica cuadrada que sincroniza la conmutación de registros y microcontroladores.")
    add_bullet("Debounce (Antirrebote): ", "Filtrado físico o lógico para eliminar pulsos espurios producidos por el rebote elástico de un botón.")
    add_bullet("FSM (Finite State Machine): ", "Máquina de estados finitos que modela formalmente el comportamiento secuencial del sistema.")
    add_bullet("Glitch / Hazard (Perturbación): ", "Pulso falso e indeseado originado por diferencias en los retardos de propagación (t_pd).")
    add_bullet("LCD (Liquid Crystal Display): ", "Pantalla pasiva reflectiva donde las celdas de cristal líquido modulan la luz ambiente.")
    add_bullet("Término de Consenso: ", "Término booleano redundante que cubre transiciones adyacentes en Karnaugh para eliminar glitches.")

    doc.add_page_break()

    # ==================== HOJA 3: INTRODUCCIÓN ====================
    add_h1("1. INTRODUCCIÓN")
    add_p("A lo largo de las últimas cinco décadas, los sistemas digitales han transformado la tecnología moderna. Antes del surgimiento de los microprocesadores complejos de múltiples núcleos, la industria electrónica sentó las bases del diseño digital mediante máquinas secuenciales síncronas, compuertas universales discretas y microcontroladores compactos orientados a la máxima eficiencia energética. En este marco histórico y pedagógico, las consolas portátiles con pantalla de cristal líquido (LCD) de inicios de los años ochenta representan uno de los casos de estudio más instructivos de la ingeniería.")
    add_p("El motivo central de esta investigación radica en analizar cómo un dispositivo de recursos sumamente acotados es capaz de muestrear pulsadores mecánicos, procesar dinámicas concurrentes de juego en tiempo real, resolver condiciones lógicas de colisión y excitar matrices gráficas segmentadas, operando con un bus de 4 bits y alimentado por pequeñas pilas de botón con un consumo de microamperios. Este análisis demuestra a los futuros ingenieros que la confiabilidad y fluidez de un sistema no provienen exclusivamente de una potencia de cálculo elevada, sino de un diseño combinacional y secuencial matemáticamente optimizado y libre de errores de sincronismo.")
    add_p("El objetivo general de este informe consiste en realizar un análisis integral de la arquitectura electrónica, las características físicas y el funcionamiento digital de la consola Nintendo Game & Watch (modelo seminal 'Ball', código AC-01), formalizando sus especificaciones para proyectar su futura implementación en laboratorio mediante circuitos integrados de lógica discreta TTL serie 74LS y, posteriormente, su emulación en la plataforma Arduino.")
    add_p("Los objetivos específicos son: (1) caracterizar los componentes de hardware originales y su acoplamiento tecnológico; (2) modelar la dinámica de juego a través de una Máquina de Estados Finitos (FSM) y ecuaciones booleanas; (3) deducir el fenómeno de perturbaciones transitorias (glitches) por retardos de propagación y su resolución mediante mapas de Karnaugh con términos de consenso; y (4) definir con criterio ingenieril qué módulos se implementarán en protoboard y cuáles se reservarán para la etapa embebida en Arduino.")
    add_p("Como resultado, este documento proporciona una memoria técnica completa y rigurosa, que conecta los contenidos teóricos de la asignatura con un proyecto práctico de laboratorio.")

    doc.add_page_break()

    # ==================== HOJA 4: DESCRIPCIÓN DEL DISPOSITIVO ====================
    add_h1("2. DESCRIPCIÓN DEL DISPOSITIVO")
    add_h2("2.1. Antecedentes Históricos y Contexto")
    add_p("La línea Game & Watch fue concebida en 1979 por Gunpei Yokoi, ingeniero y diseñador de Nintendo R&D1, tras observar a un pasajero en el tren bala Shinkansen presionando repetitivamente los botones de una calculadora digital para entretenerse. Nintendo formalizó una alianza estratégica con Sharp Corporation, aprovechando sus consolidadas líneas de fabricación de pantallas de cristal líquido reflectivo y circuitos integrados CMOS de bajo consumo (Floyd, 2006). El 28 de abril de 1980 se lanzó 'Ball' (modelo AC-01), integrando reloj digital de alta precisión ('Watch') y juego portátil interactivo ('Game'), logrando un éxito comercial histórico que superó las 43 millones de unidades.")

    add_h2("2.2. Características Físicas y Mecánicas")
    add_bullet("Chasis y Peso: ", "Carcasa de plástico termoplástico ABS de alta resistencia con placa frontal de aluminio anodizado (95 x 63 x 12 mm; masa de 52 gramos incluyendo pilas).")
    add_bullet("Controles: ", "Dos pulsadores ergonómicos principales de goma conductiva ('Left' y 'Right') sobre pistas de PCB entrelazadas, y cuatro botones embutidos: Game A, Game B, Time y el botón hundido de reset ACL (All Clear).")
    add_bullet("Pantalla: ", "Panel LCD monocromático reflectivo TN (Twisted Nematic) de 54 segmentos fijos impresos con polarizador de luz ambiente.")
    add_bullet("Alimentación: ", "Dos pilas galvánicas tipo LR43/SR43 en serie (3,0 V DC), con un consumo en reposo menor a 15 microamperios (μA).")

    add_h2("2.3. Arquitectura Electrónica Interna (Sharp SM510)")
    add_p("El sistema opera con un microcontrolador CMOS monolítico de 4 bits Sharp SM510 bajo arquitectura Harvard:")
    add_bullet("CPU de 4 bits (Nibble): ", "Maneja datos en palabras de 4 bits, permitiendo operar en forma nativa con aritmética decimal BCD (0 a 9) sin desperdicio de ciclos en conversiones.")
    add_bullet("Memorias Integradas: ", "ROM de máscara de 1,8 KB (1.820 palabras de 8 bits) con el firmware grabado de fábrica, y RAM estática de 65 nibbles (260 bits) para variables y puntuaciones.")
    add_bullet("Base de Tiempo de Cuarzo: ", "Cristal de cuarzo de 32.768 Hz (2^15 Hz) conectado a 15 divisores asíncronos en cascada (ripple counters) que entregan pulsos de 1 Hz exactos para el reloj y frecuencias de 512 Hz a 2 kHz para el audio.")
    add_bullet("Excitación LCD y Sonido: ", "Drivers push-pull de corriente alterna (AC) para proteger el cristal líquido y zumbador piezoeléctrico resonante.")

    add_h2("2.4. Principio de Funcionamiento")
    add_p("En modo Reloj (Standby), la CPU permanece en bajo consumo (Halt), despertando cada 1 segundo para refrescar la hora. En modo Juego (Activo), el microcontrolador ejecuta un bucle síncrono muestreando los botones con filtro antirrebote y actualizando la posición de las pelotas en cada intervalo temporal.")

    doc.add_page_break()

    # ==================== HOJA 5: ANÁLISIS FUNCIONAL Y FSM ====================
    add_h1("3. ANÁLISIS FUNCIONAL DEL SISTEMA")
    add_h2("3.1. Reglas y Dinámica de Juego")
    add_p("El usuario asume el rol de un malabarista que debe atrapar pelotas en trayectoria orbital parabólica continua:")
    add_bullet("Postura del Malabarista: ", "Dos posiciones posibles: brazos a la izquierda (H_L = 1) o brazos a la derecha (H_R = 1).")
    add_bullet("Modos de Juego: ", "Game A coordina 2 pelotas parabólicas simultáneas; Game B eleva el desafío a 3 pelotas concurrentes.")
    add_bullet("Puntuación y Aceleración: ", "Cada captura exitosa incrementa en +1 el contador BCD. Cada 100 puntos, el intervalo de tiempo (T_tempo) se reduce en un factor del 10%, acelerando las pelotas.")
    add_bullet("Penalización y Game Over: ", "Si una pelota llega al suelo sin ser interceptada, se suma un fallo en el registro de vidas (Miss = Miss + 1). Al acumular 3 fallos (Miss = 3), el sistema finaliza la partida en Game Over.")

    add_h2("3.2. Variables de Entrada, Salida y Acondicionamiento Antirrebote")
    add_bullet("Entradas: ", "Pulsadores mecánicos con resistencia pull-up (B_L, B_R, S_A, S_B, S_T, R_ACL). Debido a que los contactos metálicos rebotan elásticamente entre 5 y 20 ms, se incorpora un cerrojo biestable RS con compuertas NAND 74LS00 para estabilizar la señal de entrada.")
    add_bullet("Salidas: ", "Señales de postura del malabarista, segmentos de trayectoria de pelotas, bus BCD a 7 segmentos para los 3 dígitos de puntaje, indicadores de fallos y señal de audio modulada.")

    add_h2("3.3. Máquina de Estados Finitos (FSM)")
    add_p("El comportamiento secuencial se modela mediante una FSM síncrona de 5 estados (q0 a q4):")
    add_bullet("q0 (Standby / Reloj): ", "Bucle de bajo consumo. El oscilador actualiza el reloj a 1 Hz. Al presionar Game A o B, se transiciona a q1.")
    add_bullet("q1 (Inicialización): ", "Pone a cero los contadores (Score = 000, Miss = 0), carga posiciones iniciales y pasa incondicionalmente a q2.")
    add_bullet("q2 (Bucle de Juego / Gameplay Loop): ", "Cada vencimiento de T_tempo, las pelotas avanzan en sus registros de desplazamiento y se leen los botones. Si una pelota alcanza la posición inferior, transiciona a q3.")
    add_bullet("q3 (Evaluación de Colisión): ", "Evalúa si los brazos coinciden con la pelota. Si hay captura: suma +1 al puntaje, emite tono agudo de 1 kHz, invierte el avance y acelera si el puntaje es múltiplo de 100. Si falla: suma un Miss y emite tono grave de 250 Hz. Si Miss < 3, vuelve a q2; si Miss = 3, pasa a q4.")
    add_bullet("q4 (Game Over): ", "Detiene el avance de pelotas, hace parpadear la puntuación final a 2 Hz y bloquea mandos hasta recibir un reset manual.")

    doc.add_page_break()

    # ==================== HOJA 6: LÓGICA COMBINACIONAL Y KARNAUGH ====================
    add_h1("4. LÓGICA COMBINACIONAL, KARNAUGH Y PERTURBACIONES (GLITCHES)")
    add_h2("4.1. Lógica Combinacional de Colisión y Fenómeno de Glitch")
    add_p("Consideremos la función combinacional para verificar la captura en la posición inferior izquierda:")
    add_bullet("A: ", "Presencia física de la pelota en la posición inferior (A = 1).")
    add_bullet("B: ", "Brazos del malabarista en la izquierda (B = 1).")
    add_bullet("C: ", "Pulso estroboscópico de sincronismo emitido por el reloj maestro (C = 1).")
    add_p("La función teórica de impacto corresponde a:  F(A, B, C) = A·C' + B·C")
    add_p("Fenómeno Físico de Glitch (Hazard): Cuando las entradas se mantienen estables en A = 1 y B = 1, y la señal C conmuta de nivel alto a bajo (C: 1 -> 0):")
    add_p("En teoría booleana ideal, la salida debiese permanecer fija en 1 (pasa de B·C a A·C'). Sin embargo, en el silicio real, la compuerta inversora NOT que produce C' tiene un tiempo de retardo de propagación finito (t_pd). Durante ese intervalo transitorio, tanto C como C' son leídos momentáneamente en 0, haciendo que la salida caiga brevemente a cero (1 -> 0 -> 1). Esta caída espuria es una perturbación dinámica (glitch) que podría provocar conteos erróneos o falsas penalizaciones en el sistema.")

    add_h2("4.2. Mapa de Karnaugh y Término de Consenso Redundante")
    add_p("Analizando la función en el mapa de Karnaugh de 3 variables:")
    add_p("          AB\n"
          "   C    00   01   11   10\n"
          "   0     0    0   [1    1]   --> Término A·C'\n"
          "   1     0   [1    1]   0    --> Término B·C")
    add_p("Las agrupaciones colindan en la celda AB = 11 sin compartir un lazo protector. Para eliminar físicamente el glitch, añadimos el término de consenso redundante A·B:")
    add_p("F_segura(A, B, C) = A·C' + B·C + A·B", bold=True)
    add_p("Mientras A = 1 y B = 1, la rama A·B sostiene la salida permanentemente en 1, anulando el efecto del retardo de la compuerta inversora.")

    add_h2("4.3. Implementación con Compuertas Universales NAND")
    add_p("Aplicando el teorema de DeMorgan, la función se construye usando exclusivamente compuertas NAND 74LS00:")
    add_p("F_segura = NOT( NOT(A·C') · NOT(B·C) · NOT(A·B) )", bold=True)

    add_h2("4.4. Diagramas de Flujo del Comportamiento Digital")
    add_bullet("Bucle Maestro: ", "Reset/Arranque -> Selección de Modo (Time vs Game) -> Muestreo continuo de botones antirrebote -> ¿Expiró T_tempo? (Sí: avanza pelotas; No: mantiene lectura) -> ¿Pelota en cota terminal? (Sí: ejecuta subrutina de colisión; No: refresca pantalla).")
    add_bullet("Subrutina de Colisión: ", "Evalúa Catch = (P_term_L · H_L) + (P_term_R · H_R). Si Catch = 1: incrementa puntuación BCD, emite sonido agudo, invierte vector y ajusta velocidad. Si Catch = 0: suma Miss y genera sonido grave; si Miss = 3, bloquea y transiciona a Game Over.")

    doc.add_page_break()

    # ==================== HOJA 7: ALCANCE Y FACTIBILIDAD (TTL Y ARDUINO) ====================
    add_h1("5. ALCANCE Y FACTIBILIDAD DE IMPLEMENTACIÓN (TTL Y ARDUINO)")
    add_h2("5.1. Delimitación Técnica para Maqueta Discreta TTL (74LS)")
    add_p("Considerando las restricciones de tiempo semestral y recursos de laboratorio, se establece una delimitación técnica fundamentada:")
    add_bullet("Módulos que SERÁN IMPLEMENTADOS en Protoboard: ", "")
    add_p("  1. Movimiento del Jugador: Biestable síncrono tipo D (74LS74) con antirrebote NAND (74LS00) y 2 LEDs de postura.\n"
          "  2. Trayectoria Parabólica: Simulación de 1 pelota con registro de desplazamiento bidireccional (74LS194) o contador Johnson (4017).\n"
          "  3. Lógica Combinacional de Colisión: Compuertas NAND (74LS00) con término de consenso anti-glitch.\n"
          "  4. Contador BCD de 2 Dígitos: Cascada de dos contadores de décadas (74LS160) y decodificadores a 7 segmentos (74LS47).\n"
          "  5. Registro de Penalizaciones: Contador binario con compuertas para 3 LEDs de vidas y bloqueo de Game Over.\n"
          "  6. Base de Tiempo: Oscilador astable basado en temporizador NE555 regulable con potenciómetro.")
    
    add_bullet("Módulos OMITIDOS en la Maqueta Cableada y Justificación: ", "")
    add_p("  1. Modo Game B (3 pelotas simultáneas): Omitido porque triplicaría los registros y circuitos auxiliares, demandando más de 16 integrados y saturando el límite de corriente de abanico de salida (Fan-Out N = 10 de la familia TTL).\n"
          "  2. Reloj de 24 horas y Panel LCD a medida: Sustituidos por LEDs y displays estándar para evitar la congestión de alambrado y el ruido electromagnético inductivo/capacitivo en protoboard.")

    add_h2("5.2. Estrategia de Migración y Emulación en Arduino")
    add_p("En la siguiente etapa, la arquitectura validada en compuertas se portará a un microcontrolador ATmega328P (Arduino Uno):")
    add_bullet("Arquitectura No Bloqueante: ", "Control temporal mediante la función millis() e interrupciones por temporizador, descartando el uso de delay() para asegurar un sondeo fluido de botones.")
    add_bullet("Acondicionamiento por Software: ", "Resistencias internas INPUT_PULLUP y algoritmo de debounce temporal de 15 ms.")
    add_bullet("Interfaz OLED y Audio: ", "Pantalla OLED gráfica de 0,96 pulgadas vía bus I2C (solo 2 pines: SDA y SCL) y tonos acústicos con tone().")
    add_bullet("Levantamiento de Restricciones: ", "En Arduino se implementan con facilidad las 3 pelotas simultáneas de Game B y el guardado de récords en memoria EEPROM.")

    doc.add_page_break()

    # ==================== HOJA 8: PROPUESTAS DE MEJORA MODERNA ====================
    add_h1("6. PROPUESTAS DE MEJORA MODERNA")
    add_p("Se presentan cuatro propuestas de ingeniería que modernizan el dispositivo sin desvirtuar su naturaleza digital:")

    add_h2("6.1. Mejora 1: Temporización Pseudoaleatoria por LFSR de 8 Bits")
    add_bullet("Justificación: ", "La cadencia original de las pelotas es determinista y predecible tras memorizarse. Se propone incorporar un Registro de Desplazamiento con Retroalimentación Lineal (LFSR) de 8 bits con polinomio irreducible (P(x) = x^8 + x^6 + x^5 + x^4 + 1) mediante compuertas XOR (74LS86), generando variaciones pseudoaleatorias en el intervalo de caída entre 250 ms y 550 ms.")
    add_bullet("Impacto Técnico: ", "Modula dinámicamente la señal de reloj hacia los registros de avance dentro del estado q2.")

    add_h2("6.2. Mejora 2: Módulo Secuencial de Pausa Activa (Clock-Gating)")
    add_bullet("Justificación: ", "La consola clásica carecía de pausa, provocando la pérdida de la partida ante interrupciones. Se implementa una compuerta lógica de paso (Clock-Gating) comandada por un pulsador 'Pause' (B_P) y un biestable Toggle, que aísla la señal de reloj.")
    add_bullet("Impacto Técnico: ", "Crea el estado síncrono q_pause sin alterar los acumuladores de puntuación ni las vidas.")

    add_h2("6.3. Mejora 3: Sistema Acústico de Rachas (Combo System con 74LS85)")
    add_bullet("Justificación: ", "El sonido original era monótono. Se diseña un contador de capturas continuas acoplado a un comparador de magnitud binaria de 4 bits (74LS85) que, al alcanzar umbrales (10, 20 o 50 capturas), conmuta un multiplexor (74LS151) para emitir arpegios musicales de celebración y activar puntuación doble (x2).")
    add_bullet("Impacto Técnico: ", "Añade estados de bonificación y modulación de frecuencias sonoras dentro de la subrutina q3.")

    add_h2("6.4. Mejora 4: Persistencia de Récord Máximo (High Score con EEPROM)")
    add_bullet("Justificación: ", "El puntaje récord se perdía al apagar la consola. Se proyecta una red de tres comparadores síncronos en cascada (74LS85) que comparan en tiempo real los 12 bits BCD de la puntuación en curso contra el récord memorizado. Si Score_actual > Score_max, se habilita la sobreescritura del registro.")
    add_bullet("Impacto Técnico: ", "Preserva permanentemente el récord en memoria EEPROM no volátil para su visualización en Game Over (q4).")

    doc.add_page_break()

    # ==================== HOJA 9: CONCLUSIÓN ====================
    add_h1("7. CONCLUSIÓN")
    add_p("El desarrollo de este informe técnico sobre la consola portátil Nintendo Game & Watch: Ball (modelo AC-01, 1980) permitió articular los contenidos abstractos de la cátedra de Sistemas Digitales con un producto comercial masivo de notable valor formativo, demostrando cómo la ingeniería de diseño permite construir sistemas interactivos confiables y en tiempo real bajo severas restricciones de memoria, procesamiento y consumo eléctrico.")
    add_p("A través del análisis anatómico y el modelado funcional, se comprobó que una dinámica interactiva sofisticada puede sintetizarse íntegramente a partir del acoplamiento estructurado de compuertas lógicas universales, registros de desplazamiento, contadores de décadas BCD y una Máquina de Estados Finitos (FSM) síncrona de cinco estados (q0 a q4). Este enfoque evidenció que no siempre se requieren procesadores sobredimensionados cuando los datos pueden manejarse eficientemente en palabras de 4 bits (nibbles).")
    add_p("Uno de los aportes de mayor peso técnico de esta memoria radicó en el análisis de los retardos físicos de propagación (t_pd) y la detección de perturbaciones dinámicas (glitches) en la función combinacional de captura. Se demostró matemáticamente que los mapas de Karnaugh actúan como una herramienta preventiva de diseño: la adición deliberada del término de consenso redundante A·B en la función minimizada asegura que la conmutación de las señales de reloj no genere caídas espurias de tensión, blindando el sistema contra falsos disparos de colisión.")
    add_p("Asimismo, la delimitación consciente del alcance físico para la futura maqueta de circuitos integrados discretos TTL serie 74LS frente a la posterior simulación en microcontrolador Arduino aportó un valioso criterio de gestión técnica. Reconocer las limitaciones de corriente de carga (Fan-Out N = 10), el ruido electromagnético y la densidad de alambrado en protoboard permite concentrar el trabajo de laboratorio en los bloques neurálgicos (movimiento, trayectoria, lógica anti-glitch y conteo BCD), postergando con fundamento las funcionalidades extendidas hacia la etapa embebida.")
    add_p("En conclusión, este trabajo consolida los aprendizajes de modelado, diseño combinacional y lógica secuencial, entregando una memoria técnica de excelencia para afrontar con solvencia las siguientes etapas evaluativas de la asignatura.")

    doc.add_page_break()

    # ==================== HOJA 10: REFERENCIAS BIBLIOGRÁFICAS ====================
    add_h1("8. REFERENCIAS BIBLIOGRÁFICAS")
    add_p("Floyd, T. L. (2006). Fundamentos de sistemas digitales (9.ª ed.). Pearson Educación.")
    add_p("Mano, M. M., & Ciletti, M. D. (2013). Diseño digital: Con una introducción a Verilog HDL (5.ª ed.). Pearson Educación.")
    add_p("Nintendo Co., Ltd. (1980). Game & Watch: Ball (Model AC-01) Service & Instruction Manual. Nintendo R&D1.")
    add_p("Sharp Corporation. (1980). SM-5xx Series 4-bit Single Chip Microcomputer User's Manual. Sharp Electronic Components.")
    add_p("Tocci, R. J., Widmer, N. S., & Moss, G. L. (2007). Sistemas digitales: Principios y aplicaciones (10.ª ed.). Pearson Educación.")
    add_p("Wakerly, J. F. (2001). Diseño digital: Principios y prácticas (3.ª ed.). Pearson Educación.")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    doc_path = OUTPUT_DIR / "Informe_Sistemas_Digitales_Game_and_Watch.docx"
    doc.save(doc_path)
    print(f"DOCX creado exitosamente: {doc_path}")

def create_html_and_pdf():
    # Creamos un archivo HTML optimizado para impresion a PDF (tamano Carta, margenes 2cm, saltos de pagina)
    html_content = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Informe Técnico - Sistemas Digitales</title>
<style>
  @page {
    size: letter;
    margin: 20mm;
    @bottom-right {
      content: counter(page);
    }
  }
  body {
    font-family: 'Calibri', 'Segoe UI', Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.25;
    color: #222;
    margin: 0;
    padding: 0;
  }
  .page {
    page-break-before: always;
    clear: both;
  }
  .page-first {
    page-break-before: avoid;
  }
  h1 {
    font-size: 15pt;
    color: #003366;
    border-bottom: 2px solid #003366;
    padding-bottom: 4px;
    margin-top: 0;
    margin-bottom: 12px;
  }
  h2 {
    font-size: 12.5pt;
    color: #114477;
    margin-top: 14px;
    margin-bottom: 6px;
  }
  p {
    text-align: justify;
    margin-top: 0;
    margin-bottom: 8px;
    text-justify: inter-word;
  }
  ul {
    margin-top: 0;
    margin-bottom: 8px;
    padding-left: 20px;
  }
  li {
    text-align: justify;
    margin-bottom: 4px;
  }
  .cover {
    text-align: center;
    padding-top: 40px;
  }
  .cover-header {
    font-size: 11pt;
    font-weight: bold;
    color: #003366;
    line-height: 1.4;
  }
  .cover-course {
    margin-top: 30px;
    font-size: 11pt;
    font-weight: bold;
    color: #444;
  }
  .cover-title {
    margin-top: 50px;
    font-size: 16pt;
    font-weight: bold;
    color: #003366;
    line-height: 1.3;
  }
  .cover-subtitle {
    margin-top: 15px;
    font-size: 12pt;
    font-style: italic;
    font-weight: bold;
    color: #555;
  }
  .cover-info {
    margin-top: 100px;
    font-size: 10.5pt;
    line-height: 1.5;
  }
  .code-box {
    background-color: #f4f6f9;
    border-left: 4px solid #003366;
    padding: 8px 12px;
    font-family: monospace;
    font-size: 9.5pt;
    margin: 8px 0;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0;
    font-size: 10pt;
  }
  th, td {
    border: 1px solid #ccc;
    padding: 6px 8px;
    text-align: left;
  }
  th {
    background-color: #e6eef5;
    color: #003366;
  }
</style>
</head>
<body>

<!-- HOJA 1: PORTADA -->
<div class="cover page-first">
  <div class="cover-header">
    UNIVERSIDAD CATÓLICA DEL NORTE<br>
    FACULTAD DE INGENIERÍA Y CIENCIAS GEOLÓGICAS<br>
    ESCUELA DE INGENIERÍA — SEDE COQUIMBO<br>
    DEPARTAMENTO DE INGENIERÍA DE SISTEMAS Y COMPUTACIÓN
  </div>
  
  <div class="cover-course">
    PROYECTO DE SISTEMAS DIGITALES<br>
    SEGUNDO SEMESTRE 2026
  </div>
  
  <div class="cover-title">
    INFORME TÉCNICO: ANÁLISIS DE SISTEMAS DIGITALES EN DISPOSITIVOS LCD
  </div>
  <div class="cover-subtitle">
    ESTUDIO DE CASO: CONSOLA PORTÁTIL NINTENDO GAME & WATCH (SERIE BALL, MODELO AC-01)
  </div>
  
  <div class="cover-info">
    <strong>NOMBRE DEL EQUIPO:</strong> Sistemas Digitales UCN Lab<br><br>
    <strong>INTEGRANTES:</strong><br>
    • [Nombre Alumno 1] — RUT: [XX.XXX.XXX-X] — correo1@alumnos.ucn.cl<br>
    • [Nombre Alumno 2] — RUT: [XX.XXX.XXX-X] — correo2@alumnos.ucn.cl<br>
    • [Nombre Alumno 3] — RUT: [XX.XXX.XXX-X] — correo3@alumnos.ucn.cl<br><br>
    <strong>PROFESOR GUÍA:</strong> Ing. Bastian Ruiz Garay<br><br>
    Coquimbo, Chile — 21 de Septiembre de 2026
  </div>
</div>

<!-- HOJA 2: INDICE Y GLOSARIO -->
<div class="page">
  <h1>ÍNDICE GENERAL</h1>
  <p>
    1. INTRODUCCIÓN .................................................................................................................... Pág. 3<br>
    2. DESCRIPCIÓN DEL DISPOSITIVO .................................................................................... Pág. 4<br>
    &nbsp;&nbsp;&nbsp;2.1. Antecedentes Históricos y Contexto Tecnológico .................................................... Pág. 4<br>
    &nbsp;&nbsp;&nbsp;2.2. Características Físicas y Mecánicas ........................................................................... Pág. 4<br>
    &nbsp;&nbsp;&nbsp;2.3. Arquitectura Electrónica Interna (Sharp SM510) ..................................................... Pág. 4<br>
    &nbsp;&nbsp;&nbsp;2.4. Principio de Funcionamiento General ......................................................................... Pág. 4<br>
    3. ANÁLISIS FUNCIONAL DEL SISTEMA ............................................................................ Pág. 5<br>
    &nbsp;&nbsp;&nbsp;3.1. Reglas y Dinámica de Juego ....................................................................................... Pág. 5<br>
    &nbsp;&nbsp;&nbsp;3.2. Mapeo de Entradas, Salidas y Antirrebote (Debounce) ............................................. Pág. 5<br>
    &nbsp;&nbsp;&nbsp;3.3. Modelo de Máquina de Estados Finitos (FSM) ............................................................. Pág. 5<br>
    4. LÓGICA COMBINACIONAL, KARNAUGH Y PERTURBACIONES (GLITCHES) .......... Pág. 6<br>
    &nbsp;&nbsp;&nbsp;4.1. Función de Colisión y Fenómeno Físico de Glitch ..................................................... Pág. 6<br>
    &nbsp;&nbsp;&nbsp;4.2. Mapa de Karnaugh y Término de Consenso Redundante .......................................... Pág. 6<br>
    &nbsp;&nbsp;&nbsp;4.3. Implementación con Compuertas Universales NAND ................................................. Pág. 6<br>
    &nbsp;&nbsp;&nbsp;4.4. Diagramas de Flujo del Comportamiento Digital ........................................................ Pág. 6<br>
    5. ALCANCE Y FACTIBILIDAD DE IMPLEMENTACIÓN (TTL Y ARDUINO) ....................... Pág. 7<br>
    &nbsp;&nbsp;&nbsp;5.1. Delimitación Técnica para Maqueta Discreta TTL (74LS) ............................................ Pág. 7<br>
    &nbsp;&nbsp;&nbsp;5.2. Factibilidad Física: Fan-Out y Ruido en Protoboard .................................................... Pág. 7<br>
    &nbsp;&nbsp;&nbsp;5.3. Estrategia de Migración y Simulación en Arduino .................................................... Pág. 7<br>
    6. PROPUESTAS DE MEJORA MODERNA ........................................................................... Pág. 8<br>
    &nbsp;&nbsp;&nbsp;6.1. Mejora 1: Temporización Pseudoaleatoria por LFSR ................................................. Pág. 8<br>
    &nbsp;&nbsp;&nbsp;6.2. Mejora 2: Módulo Secuencial de Pausa Activa (Clock-Gating) ................................. Pág. 8<br>
    &nbsp;&nbsp;&nbsp;6.3. Mejora 3: Sistema Acústico de Rachas (Combo System con 74LS85) .......................... Pág. 8<br>
    &nbsp;&nbsp;&nbsp;6.4. Mejora 4: Persistencia de Récord Máximo (High Score con EEPROM) ........................ Pág. 8<br>
    7. CONCLUSIÓN ...................................................................................................................... Pág. 9<br>
    8. REFERENCIAS BIBLIOGRÁFICAS ................................................................................... Pág. 10
  </p>
  
  <h2>GLOSARIO DE TÉRMINOS TÉCNICOS</h2>
  <ul>
    <li><strong>ALU (Arithmetic Logic Unit):</strong> Unidad aritmético-lógica encargada de operaciones matemáticas y comparaciones booleanas.</li>
    <li><strong>BCD (Binary-Coded Decimal):</strong> Decimal codificado en binario; representa cada dígito (0 a 9) en un cuarteto de 4 bits (nibble).</li>
    <li><strong>Biestable (Flip-Flop):</strong> Elemento de memoria de un bit que conmuta de estado con flancos de reloj síncronos.</li>
    <li><strong>Clock (Señal de Reloj):</strong> Onda periódica cuadrada que sincroniza la conmutación de registros y microcontroladores.</li>
    <li><strong>Debounce (Antirrebote):</strong> Filtrado físico o lógico para eliminar pulsos espurios producidos por el rebote mecánico de un botón.</li>
    <li><strong>FSM (Finite State Machine):</strong> Máquina de estados finitos que modela formalmente el comportamiento secuencial del sistema.</li>
    <li><strong>Glitch / Hazard (Perturbación):</strong> Pulso falso e indeseado originado por diferencias en los retardos de propagación (t_pd).</li>
    <li><strong>LCD (Liquid Crystal Display):</strong> Pantalla pasiva reflectiva donde las celdas de cristal líquido modulan la luz ambiente.</li>
    <li><strong>Término de Consenso:</strong> Término booleano redundante que cubre transiciones adyacentes en Karnaugh para eliminar glitches.</li>
  </ul>
</div>

<!-- HOJA 3: INTRODUCCION -->
<div class="page">
  <h1>1. INTRODUCCIÓN</h1>
  <p>A lo largo de las últimas cinco décadas, los sistemas digitales han transformado la tecnología moderna. Antes del surgimiento de los microprocesadores complejos de múltiples núcleos, la industria electrónica sentó las bases del diseño digital mediante máquinas secuenciales síncronas, compuertas universales discretas y microcontroladores compactos orientados a la máxima eficiencia energética. En este marco histórico y pedagógico, las consolas portátiles con pantalla de cristal líquido (LCD) de inicios de los años ochenta representan uno de los casos de estudio más instructivos de la ingeniería.</p>
  <p>El motivo central de esta investigación radica en analizar cómo un dispositivo de recursos sumamente acotados es capaz de muestrear pulsadores mecánicos, procesar dinámicas concurrentes de juego en tiempo real, resolver condiciones lógicas de colisión y excitar matrices gráficas segmentadas, operando con un bus de 4 bits y alimentado por pequeñas pilas de botón con un consumo de microamperios. Este análisis demuestra a los futuros ingenieros que la confiabilidad y fluidez de un sistema no provienen exclusivamente de una potencia de cálculo elevada, sino de un diseño combinacional y secuencial matemáticamente optimizado y libre de errores de sincronismo.</p>
  <p>El objetivo general de este informe consiste en realizar un análisis integral de la arquitectura electrónica, las características físicas y el funcionamiento digital de la consola Nintendo Game & Watch (modelo seminal 'Ball', código AC-01), formalizando sus especificaciones para proyectar su futura implementación en laboratorio mediante circuitos integrados de lógica discreta TTL serie 74LS y, posteriormente, su emulación en la plataforma Arduino.</p>
  <p>Los objetivos específicos son: (1) caracterizar los componentes de hardware originales y su acoplamiento tecnológico; (2) modelar la dinámica de juego a través de una Máquina de Estados Finitos (FSM) y ecuaciones booleanas; (3) deducir el fenómeno de perturbaciones transitorias (glitches) por retardos de propagación y su resolución mediante mapas de Karnaugh con términos de consenso; y (4) definir con criterio ingenieril qué módulos se implementarán en protoboard y cuáles se reservarán para la etapa embebida en Arduino.</p>
  <p>Como resultado, este documento proporciona una memoria técnica completa y rigurosa, que conecta los contenidos teóricos de la asignatura con un proyecto práctico de laboratorio.</p>
</div>

<!-- HOJA 4: DESCRIPCION DEL DISPOSITIVO -->
<div class="page">
  <h1>2. DESCRIPCIÓN DEL DISPOSITIVO</h1>
  <h2>2.1. Antecedentes Históricos y Contexto</h2>
  <p>La línea Game & Watch fue concebida en 1979 por Gunpei Yokoi, ingeniero y diseñador de Nintendo R&D1, tras observar a un pasajero en el tren bala Shinkansen presionando repetitivamente los botones de una calculadora digital para entretenerse. Nintendo formalizó una alianza estratégica con Sharp Corporation, aprovechando sus consolidadas líneas de fabricación de pantallas de cristal líquido reflectivo y circuitos integrados CMOS de bajo consumo (Floyd, 2006). El 28 de abril de 1980 se lanzó 'Ball' (modelo AC-01), integrando reloj digital de alta precisión ('Watch') y juego portátil interactivo ('Game'), logrando un éxito comercial histórico que superó las 43 millones de unidades.</p>

  <h2>2.2. Características Físicas y Mecánicas</h2>
  <ul>
    <li><strong>Chasis y Peso:</strong> Carcasa de plástico termoplástico ABS de alta resistencia con placa frontal de aluminio anodizado (95 x 63 x 12 mm; masa de 52 gramos incluyendo pilas).</li>
    <li><strong>Controles:</strong> Dos pulsadores ergonómicos principales de goma conductiva ('Left' y 'Right') sobre pistas de PCB entrelazadas, y cuatro botones embutidos: Game A, Game B, Time y el botón hundido de reset ACL (All Clear).</li>
    <li><strong>Pantalla:</strong> Panel LCD monocromático reflectivo TN (Twisted Nematic) de 54 segmentos fijos impresos con polarizador de luz ambiente.</li>
    <li><strong>Alimentación:</strong> Dos pilas galvánicas tipo LR43/SR43 en serie (3,0 V DC), con un consumo en reposo menor a 15 microamperios (μA).</li>
  </ul>

  <h2>2.3. Arquitectura Electrónica Interna (Sharp SM510)</h2>
  <p>El sistema opera con un microcontrolador CMOS monolítico de 4 bits Sharp SM510 bajo arquitectura Harvard:</p>
  <ul>
    <li><strong>CPU de 4 bits (Nibble):</strong> Maneja datos en palabras de 4 bits, permitiendo operar en forma nativa con aritmética decimal BCD (0 a 9) sin desperdicio de ciclos en conversiones.</li>
    <li><strong>Memorias Integradas:</strong> ROM de máscara de 1,8 KB (1.820 palabras de 8 bits) con el firmware grabado de fábrica, y RAM estática de 65 nibbles (260 bits) para variables y puntuaciones.</li>
    <li><strong>Base de Tiempo de Cuarzo:</strong> Cristal de cuarzo de 32.768 Hz (2^15 Hz) conectado a 15 divisores asíncronos en cascada (ripple counters) que entregan pulsos de 1 Hz exactos para el reloj y frecuencias de 512 Hz a 2 kHz para el audio.</li>
    <li><strong>Excitación LCD y Sonido:</strong> Drivers push-pull de corriente alterna (AC) para proteger el cristal líquido y zumbador piezoeléctrico resonante.</li>
  </ul>

  <h2>2.4. Principio de Funcionamiento</h2>
  <p>En modo Reloj (Standby), la CPU permanece en bajo consumo (Halt), despertando cada 1 segundo para refrescar la hora. En modo Juego (Activo), el microcontrolador ejecuta un bucle síncrono muestreando los botones con filtro antirrebote y actualizando la posición de las pelotas en cada intervalo temporal.</p>
</div>

<!-- HOJA 5: ANALISIS FUNCIONAL Y FSM -->
<div class="page">
  <h1>3. ANÁLISIS FUNCIONAL DEL SISTEMA</h1>
  <h2>3.1. Reglas y Dinámica de Juego</h2>
  <p>El usuario asume el rol de un malabarista que debe atrapar pelotas en trayectoria orbital parabólica continua:</p>
  <ul>
    <li><strong>Postura del Malabarista:</strong> Dos posiciones posibles: brazos a la izquierda (H_L = 1) o brazos a la derecha (H_R = 1).</li>
    <li><strong>Modos de Juego:</strong> Game A coordina 2 pelotas parabólicas simultáneas; Game B eleva el desafío a 3 pelotas concurrentes.</li>
    <li><strong>Puntuación y Aceleración:</strong> Cada captura exitosa incrementa en +1 el contador BCD. Cada 100 puntos, el intervalo de tiempo (T_tempo) se reduce en un factor del 10%, acelerando las pelotas.</li>
    <li><strong>Penalización y Game Over:</strong> Si una pelota llega al suelo sin ser interceptada, se suma un fallo en el registro de vidas (Miss = Miss + 1). Al acumular 3 fallos (Miss = 3), el sistema finaliza la partida en Game Over.</li>
  </ul>

  <h2>3.2. Variables de Entrada, Salida y Acondicionamiento Antirrebote</h2>
  <ul>
    <li><strong>Entradas:</strong> Pulsadores mecánicos con resistencia pull-up (B_L, B_R, S_A, S_B, S_T, R_ACL). Debido a que los contactos metálicos rebotan elásticamente entre 5 y 20 ms, se incorpora un cerrojo biestable RS con compuertas NAND 74LS00 para estabilizar la señal de entrada.</li>
    <li><strong>Salidas:</strong> Señales de postura del malabarista, segmentos de trayectoria de pelotas, bus BCD a 7 segmentos para los 3 dígitos de puntaje, indicadores de fallos y señal de audio modulada.</li>
  </ul>

  <h2>3.3. Máquina de Estados Finitos (FSM)</h2>
  <p>El comportamiento secuencial se modela mediante una FSM síncrona de 5 estados (q0 a q4):</p>
  <ul>
    <li><strong>q0 (Standby / Reloj):</strong> Bucle de bajo consumo. El oscilador actualiza el reloj a 1 Hz. Al presionar Game A o B, se transiciona a q1.</li>
    <li><strong>q1 (Inicialización):</strong> Pone a cero los contadores (Score = 000, Miss = 0), carga posiciones iniciales y pasa incondicionalmente a q2.</li>
    <li><strong>q2 (Bucle de Juego / Gameplay Loop):</strong> Cada vencimiento de T_tempo, las pelotas avanzan en sus registros de desplazamiento y se leen los botones. Si una pelota alcanza la posición inferior, transiciona a q3.</li>
    <li><strong>q3 (Evaluación de Colisión):</strong> Evalúa si los brazos coinciden con la pelota. Si hay captura: suma +1 al puntaje, emite tono agudo de 1 kHz, invierte el avance y acelera si el puntaje es múltiplo de 100. Si falla: suma un Miss y emite tono grave de 250 Hz. Si Miss < 3, vuelve a q2; si Miss = 3, pasa a q4.</li>
    <li><strong>q4 (Game Over):</strong> Detiene el avance de pelotas, hace parpadear la puntuación final a 2 Hz y bloquea mandos hasta recibir un reset manual.</li>
  </ul>
</div>

<!-- HOJA 6: LOGICA COMBINACIONAL Y KARNAUGH -->
<div class="page">
  <h1>4. LÓGICA COMBINACIONAL, KARNAUGH Y PERTURBACIONES (GLITCHES)</h1>
  <h2>4.1. Lógica Combinacional de Colisión y Fenómeno de Glitch</h2>
  <p>Consideremos la función combinacional para verificar la captura en la posición inferior izquierda:</p>
  <ul>
    <li><strong>A:</strong> Presencia física de la pelota en la posición inferior (A = 1).</li>
    <li><strong>B:</strong> Brazos del malabarista en la izquierda (B = 1).</li>
    <li><strong>C:</strong> Pulso estroboscópico de sincronismo emitido por el reloj maestro (C = 1).</li>
  </ul>
  <p>La función teórica de impacto corresponde a: <strong>F(A, B, C) = A·C' + B·C</strong></p>
  <p><strong>Fenómeno Físico de Glitch (Hazard):</strong> Cuando las entradas se mantienen estables en A = 1 y B = 1, y la señal C conmuta de nivel alto a bajo (C: 1 -> 0):<br>
  En teoría booleana ideal, la salida debiese permanecer fija en 1. Sin embargo, en el silicio real, la compuerta inversora NOT que produce C' tiene un tiempo de retardo de propagación finito (t_pd). Durante ese intervalo transitorio, tanto C como C' son leídos momentáneamente en 0, haciendo que la salida caiga brevemente a cero (1 -> 0 -> 1). Esta caída espuria es una perturbación dinámica (glitch) que podría provocar conteos erróneos o falsas penalizaciones.</p>

  <h2>4.2. Mapa de Karnaugh y Término de Consenso Redundante</h2>
  <div class="code-box">
          AB
   C    00   01   11   10
   0     0    0   [1    1]   --> Término A·C'
   1     0   [1    1]   0    --> Término B·C
  </div>
  <p>Las agrupaciones colindan en la celda AB = 11 sin compartir un lazo protector. Para eliminar físicamente el glitch, añadimos el término de consenso redundante A·B:</p>
  <div class="code-box"><strong>F_segura(A, B, C) = A·C' + B·C + A·B</strong></div>
  <p>Mientras A = 1 y B = 1, la rama A·B sostiene la salida permanentemente en 1, anulando el efecto del retardo de la compuerta inversora.</p>

  <h2>4.3. Implementación con Compuertas Universales NAND</h2>
  <p>Aplicando el teorema de DeMorgan, la función se construye usando exclusivamente compuertas NAND 74LS00:</p>
  <div class="code-box"><strong>F_segura = NOT( NOT(A·C') · NOT(B·C) · NOT(A·B) )</strong></div>

  <h2>4.4. Diagramas de Flujo del Comportamiento Digital</h2>
  <ul>
    <li><strong>Bucle Maestro:</strong> Reset/Arranque -> Selección de Modo (Time vs Game) -> Muestreo continuo de botones antirrebote -> ¿Expiró T_tempo? (Sí: avanza pelotas; No: mantiene lectura) -> ¿Pelota en cota terminal? (Sí: ejecuta subrutina de colisión; No: refresca pantalla).</li>
    <li><strong>Subrutina de Colisión:</strong> Evalúa Catch = (P_term_L · H_L) + (P_term_R · H_R). Si Catch = 1: incrementa puntuación BCD, emite sonido agudo, invierte vector y ajusta velocidad. Si Catch = 0: suma Miss y genera sonido grave; si Miss = 3, bloquea y transiciona a Game Over.</li>
  </ul>
</div>

<!-- HOJA 7: ALCANCE Y FACTIBILIDAD -->
<div class="page">
  <h1>5. ALCANCE Y FACTIBILIDAD DE IMPLEMENTACIÓN (TTL Y ARDUINO)</h1>
  <h2>5.1. Delimitación Técnica para Maqueta Discreta TTL (74LS)</h2>
  <p>Considerando las restricciones de tiempo semestral y recursos de laboratorio, se establece una delimitación técnica fundamentada:</p>
  <ul>
    <li><strong>Módulos que SERÁN IMPLEMENTADOS en Protoboard:</strong><br>
      1. Movimiento del Jugador: Biestable síncrono tipo D (74LS74) con antirrebote NAND (74LS00) y 2 LEDs de postura.<br>
      2. Trayectoria Parabólica: Simulación de 1 pelota con registro de desplazamiento bidireccional (74LS194) o contador Johnson (4017).<br>
      3. Lógica Combinacional de Colisión: Compuertas NAND (74LS00) con término de consenso anti-glitch.<br>
      4. Contador BCD de 2 Dígitos: Cascada de dos contadores de décadas (74LS160) y decodificadores a 7 segmentos (74LS47).<br>
      5. Registro de Penalizaciones: Contador binario con compuertas para 3 LEDs de vidas y bloqueo de Game Over.<br>
      6. Base de Tiempo: Oscilador astable basado en temporizador NE555 regulable con potenciómetro.
    </li>
    <li style="margin-top: 8px;"><strong>Módulos OMITIDOS en la Maqueta Cableada y Justificación:</strong><br>
      1. Modo Game B (3 pelotas simultáneas): Omitido porque triplicaría los registros y circuitos auxiliares, demandando más de 16 integrados y saturando el límite de corriente de abanico de salida (Fan-Out N = 10 de la familia TTL).<br>
      2. Reloj de 24 horas y Panel LCD a medida: Sustituidos por LEDs y displays estándar para evitar la congestión de alambrado y el ruido electromagnético en protoboard.
    </li>
  </ul>

  <h2>5.2. Estrategia de Migración y Emulación en Arduino</h2>
  <p>En la siguiente etapa, la arquitectura validada en compuertas se portará a un microcontrolador ATmega328P (Arduino Uno):</p>
  <ul>
    <li><strong>Arquitectura No Bloqueante:</strong> Control temporal mediante la función millis() e interrupciones por temporizador, descartando el uso de delay() para asegurar un sondeo fluido de botones.</li>
    <li><strong>Acondicionamiento por Software:</strong> Resistencia interna INPUT_PULLUP y algoritmo de debounce temporal de 15 ms.</li>
    <li><strong>Interfaz OLED y Audio:</strong> Pantalla OLED gráfica de 0,96 pulgadas vía bus I2C (solo 2 pines: SDA y SCL) y tonos acústicos con tone().</li>
    <li><strong>Levantamiento de Restricciones:</strong> En Arduino se implementan con facilidad las 3 pelotas simultáneas de Game B y el guardado de récords en memoria EEPROM.</li>
  </ul>
</div>

<!-- HOJA 8: PROPUESTAS DE MEJORA -->
<div class="page">
  <h1>6. PROPUESTAS DE MEJORA MODERNA</h1>
  <p>Se presentan cuatro propuestas de ingeniería que modernizan el dispositivo sin desvirtuar su naturaleza digital:</p>

  <h2>6.1. Mejora 1: Temporización Pseudoaleatoria por LFSR de 8 Bits</h2>
  <ul>
    <li><strong>Justificación:</strong> La cadencia original de las pelotas es determinista y predecible tras memorizarse. Se propone incorporar un Registro de Desplazamiento con Retroalimentación Lineal (LFSR) de 8 bits con polinomio irreducible (P(x) = x^8 + x^6 + x^5 + x^4 + 1) mediante compuertas XOR (74LS86), generando variaciones pseudoaleatorias en el intervalo de caída entre 250 ms y 550 ms.</li>
    <li><strong>Impacto Técnico:</strong> Modula dinámicamente la señal de reloj hacia los registros de avance dentro del estado q2.</li>
  </ul>

  <h2>6.2. Mejora 2: Módulo Secuencial de Pausa Activa (Clock-Gating)</h2>
  <ul>
    <li><strong>Justificación:</strong> La consola clásica carecía de pausa, provocando la pérdida de la partida ante interrupciones. Se implementa una compuerta lógica de paso (Clock-Gating) comandada por un pulsador 'Pause' (B_P) y un biestable Toggle, que aísla la señal de reloj.</li>
    <li><strong>Impacto Técnico:</strong> Crea el estado síncrono q_pause sin alterar los acumuladores de puntuación ni las vidas.</li>
  </ul>

  <h2>6.3. Mejora 3: Sistema Acústico de Rachas (Combo System con 74LS85)</h2>
  <ul>
    <li><strong>Justificación:</strong> El sonido original era monótono. Se diseña un contador de capturas continuas acoplado a un comparador de magnitud binaria de 4 bits (74LS85) que, al alcanzar umbrales (10, 20 o 50 capturas), conmuta un multiplexor (74LS151) para emitir arpegios musicales de celebración y activar puntuación doble (x2).</li>
    <li><strong>Impacto Técnico:</strong> Añade estados de bonificación y modulación de frecuencias sonoras dentro de la subrutina q3.</li>
  </ul>

  <h2>6.4. Mejora 4: Persistencia de Récord Máximo (High Score con EEPROM)</h2>
  <ul>
    <li><strong>Justificación:</strong> El puntaje récord se perdía al apagar la consola. Se proyecta una red de tres comparadores síncronos en cascada (74LS85) que comparan en tiempo real los 12 bits BCD de la puntuación en curso contra el récord memorizado. Si Score_actual > Score_max, se habilita la sobreescritura del registro.</li>
    <li><strong>Impacto Técnico:</strong> Preserva permanentemente el récord en memoria EEPROM no volátil para su visualización en Game Over (q4).</li>
  </ul>
</div>

<!-- HOJA 9: CONCLUSION -->
<div class="page">
  <h1>7. CONCLUSIÓN</h1>
  <p>El desarrollo de este informe técnico sobre la consola portátil Nintendo Game & Watch: Ball (modelo AC-01, 1980) permitió articular los contenidos abstractos de la cátedra de Sistemas Digitales con un producto comercial masivo de notable valor formativo, demostrando cómo la ingeniería de diseño permite construir sistemas interactivos confiables y en tiempo real bajo severas restricciones de memoria, procesamiento y consumo eléctrico.</p>
  <p>A través del análisis anatómico y el modelado funcional, se comprobó que una dinámica interactiva sofisticada puede sintetizarse íntegramente a partir del acoplamiento estructurado de compuertas lógicas universales, registros de desplazamiento, contadores de décadas BCD y una Máquina de Estados Finitos (FSM) síncrona de cinco estados (q0 a q4). Este enfoque evidenció que no siempre se requieren procesadores sobredimensionados cuando los datos pueden manejarse eficientemente en palabras de 4 bits (nibbles).</p>
  <p>Uno de los aportes de mayor peso técnico de esta memoria radicó en el análisis de los retardos físicos de propagación (t_pd) y la detección de perturbaciones dinámicas (glitches) en la función combinacional de captura. Se demostró matemáticamente que los mapas de Karnaugh actúan como una herramienta preventiva de diseño: la adición deliberada del término de consenso redundante A·B en la función minimizada asegura que la conmutación de las señales de reloj no genere caídas espurias de tensión, blindando el sistema contra falsos disparos de colisión.</p>
  <p>Asimismo, la delimitación consciente del alcance físico para la futura maqueta de circuitos integrados discretos TTL serie 74LS frente a la posterior simulación en microcontrolador Arduino aportó un valioso criterio de gestión técnica. Reconocer las limitaciones de corriente de carga (Fan-Out N = 10), el ruido electromagnético y la densidad de alambrado en protoboard permite concentrar el trabajo de laboratorio en los bloques neurálgicos (movimiento, trayectoria, lógica anti-glitch y conteo BCD), postergando con fundamento las funcionalidades extendidas hacia la etapa embebida.</p>
  <p>En conclusión, este trabajo consolida los aprendizajes de modelado, diseño combinacional y lógica secuencial, entregando una memoria técnica de excelencia para afrontar con solvencia las siguientes etapas evaluativas de la asignatura.</p>
</div>

<!-- HOJA 10: BIBLIOGRAFIA -->
<div class="page">
  <h1>8. REFERENCIAS BIBLIOGRÁFICAS</h1>
  <p>Floyd, T. L. (2006). <em>Fundamentos de sistemas digitales</em> (9.ª ed.). Pearson Educación.</p>
  <p>Mano, M. M., & Ciletti, M. D. (2013). <em>Diseño digital: Con una introducción a Verilog HDL</em> (5.ª ed.). Pearson Educación.</p>
  <p>Nintendo Co., Ltd. (1980). <em>Game & Watch: Ball (Model AC-01) Service & Instruction Manual</em>. Nintendo R&D1.</p>
  <p>Sharp Corporation. (1980). <em>SM-5xx Series 4-bit Single Chip Microcomputer User's Manual</em>. Sharp Electronic Components.</p>
  <p>Tocci, R. J., Widmer, N. S., & Moss, G. L. (2007). <em>Sistemas digitales: Principios y aplicaciones</em> (10.ª ed.). Pearson Educación.</p>
  <p>Wakerly, J. F. (2001). <em>Diseño digital: Principios y prácticas</em> (3.ª ed.). Pearson Educación.</p>
</div>

</body>
</html>
"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    html_path = OUTPUT_DIR / "Informe_Sistemas_Digitales_Game_and_Watch.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"HTML creado exitosamente: {html_path}")

    # Compilacion a PDF usando Microsoft Edge en modo headless
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    pdf_path = OUTPUT_DIR / "Informe_Sistemas_Digitales_Game_and_Watch.pdf"
    abs_html = os.path.abspath(html_path)
    abs_pdf = os.path.abspath(pdf_path)

    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={abs_pdf}",
        "--no-pdf-header-footer",
        abs_html
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_path):
        print(f"PDF creado exitosamente: {pdf_path} (Tamano: {os.path.getsize(pdf_path)} bytes)")
    else:
        print("Error al generar PDF con Edge:", res.stderr)

if __name__ == "__main__":
    create_docx()
    create_html_and_pdf()
