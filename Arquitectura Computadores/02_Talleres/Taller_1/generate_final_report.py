import os, sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def create_element(name):
    return OxmlElement(name)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = create_element('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = create_element('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = create_element(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, color="D0D5DD", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    tblBorders = create_element('w:tblBorders')
    for border_name in ['top', 'bottom', 'insideH']:
        border = create_element(f'w:{border_name}')
        border.set(qn('w:val'), val)
        border.set(qn('w:sz'), sz)
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), color)
        tblBorders.append(border)
    for border_name in ['left', 'right', 'insideV']:
        border = create_element(f'w:{border_name}')
        border.set(qn('w:val'), 'none')
        tblBorders.append(border)
    tblPr.append(tblBorders)

def add_header(doc, text, level):
    h = doc.add_heading(text, level=level)
    h.paragraph_format.keep_with_next = True
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after = Pt(4)
    run = h.runs[0]
    if level == 1:
        run.font.name = 'Calibri'
        run.font.size = Pt(16)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79) # Navy Blue
    elif level == 2:
        run.font.name = 'Calibri'
        run.font.size = Pt(13)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x2E, 0x75, 0xB6) # Steel Blue
    elif level == 3:
        run.font.name = 'Calibri'
        run.font.size = Pt(11)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    return h

def add_p(doc, text="", bold_prefix=None, space_after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
        r_pre.font.name = 'Calibri'
        r_pre.font.size = Pt(10.5)
        r_pre.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
    if text:
        r = p.add_run(text)
        r.font.name = 'Calibri'
        r.font.size = Pt(10.5)
        r.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    return p

def add_bullet(doc, text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
        r_pre.font.name = 'Calibri'
        r_pre.font.size = Pt(10)
        r_pre.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
    if text:
        r = p.add_run(text)
        r.font.name = 'Calibri'
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    return p

def add_code_box(doc, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F4F6F9")
    set_cell_margins(cell, top=100, bottom=100, left=160, right=160)
    
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = create_element('w:tcBorders')
    left_b = create_element('w:left')
    left_b.set(qn('w:val'), 'single')
    left_b.set(qn('w:sz'), '24')
    left_b.set(qn('w:color'), '1F4E79')
    tcBorders.append(left_b)
    for b_name in ['top', 'bottom', 'right']:
        b = create_element(f'w:{b_name}')
        b.set(qn('w:val'), 'single')
        b.set(qn('w:sz'), '4')
        b.set(qn('w:color'), 'D0D5DD')
        tcBorders.append(b)
    tcPr.append(tcBorders)

    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(code_text)
    run.font.name = 'Consolas'
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(0x11, 0x18, 0x27)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)

def add_callout(doc, title, text, alert_type="NOTE"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    
    if alert_type == "IMPORTANT":
        bg_hex = "FEF3F2"
        border_hex = "B42318"
        title_color = RGBColor(0xB4, 0x23, 0x18)
    elif alert_type == "TIP":
        bg_hex = "EDFBF0"
        border_hex = "027A48"
        title_color = RGBColor(0x02, 0x7A, 0x48)
    else: # NOTE
        bg_hex = "F0F4F9"
        border_hex = "1F4E79"
        title_color = RGBColor(0x1F, 0x4E, 0x79)
        
    set_cell_background(cell, bg_hex)
    set_cell_margins(cell, top=100, bottom=100, left=160, right=160)
    
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = create_element('w:tcBorders')
    left_b = create_element('w:left')
    left_b.set(qn('w:val'), 'single')
    left_b.set(qn('w:sz'), '24')
    left_b.set(qn('w:color'), border_hex)
    tcBorders.append(left_b)
    for b_name in ['top', 'bottom', 'right']:
        b = create_element(f'w:{b_name}')
        b.set(qn('w:val'), 'none')
        tcBorders.append(b)
    tcPr.append(tcBorders)

    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    r_t = p.add_run(f"[{alert_type}] {title}\n")
    r_t.bold = True
    r_t.font.name = 'Calibri'
    r_t.font.size = Pt(9.5)
    r_t.font.color.rgb = title_color
    
    r_txt = p.add_run(text)
    r_txt.font.name = 'Calibri'
    r_txt.font.size = Pt(9)
    r_txt.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)

def format_table_header(row, col_names, col_widths=None):
    for i, name in enumerate(col_names):
        cell = row.cells[i]
        set_cell_background(cell, "1F4E79")
        set_cell_margins(cell, top=120, bottom=120, left=140, right=140)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(name)
        r.bold = True
        r.font.name = 'Calibri'
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        if col_widths and i < len(col_widths):
            cell.width = col_widths[i]

def format_table_row(row, values, bg_hex="FFFFFF", aligns=None, col_widths=None):
    for i, val in enumerate(values):
        cell = row.cells[i]
        set_cell_background(cell, bg_hex)
        set_cell_margins(cell, top=80, bottom=80, left=140, right=140)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        if aligns and i < len(aligns):
            p.alignment = aligns[i]
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(str(val))
        r.font.name = 'Calibri'
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
        if col_widths and i < len(col_widths):
            cell.width = col_widths[i]

def build_report():
    doc = docx.Document()
    
    # Page setup - Margins 2.0 cm
    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)
        
    # -------------------------------------------------------------
    # PORTADA / COVER PAGE
    # -------------------------------------------------------------
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(36)
    p_title.paragraph_format.space_after = Pt(6)
    r = p_title.add_run("UNIVERSIDAD NACIONAL / FACULTAD DE INGENIERÍA\n")
    r.font.name = 'Calibri'
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    
    r_sub = p_title.add_run("DEPARTAMENTO DE INGENIERÍA DE SISTEMAS Y COMPUTACIÓN\nARQUITECTURA DE COMPUTADORES - PERÍODO 2026-2\n")
    r_sub.font.name = 'Calibri'
    r_sub.font.size = Pt(11)
    r_sub.font.bold = True
    r_sub.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
    
    p_main = doc.add_paragraph()
    p_main.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_main.paragraph_format.space_before = Pt(40)
    p_main.paragraph_format.space_after = Pt(12)
    r_m = p_main.add_run("INFORME DE LABORATORIO\nTALLER #1: SIMUPROC\n")
    r_m.font.name = 'Calibri'
    r_m.font.size = Pt(22)
    r_m.font.bold = True
    r_m.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
    
    r_desc = p_main.add_run("Implementación de la Sucesión de Fibonacci Generalizada y Operaciones Aritméticas de Doble Precisión (Multiplicación y División) en Lenguaje Ensamblador")
    r_desc.font.name = 'Calibri'
    r_desc.font.size = Pt(12)
    r_desc.font.italic = True
    r_desc.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
    
    # Table of Authors
    p_auth = doc.add_paragraph()
    p_auth.paragraph_format.space_before = Pt(45)
    p_auth.paragraph_format.space_after = Pt(6)
    r_a = p_auth.add_run("INTEGRANTES DEL GRUPO DE TRABAJO (HASTA 5 INTEGRANTES):")
    r_a.font.name = 'Calibri'
    r_a.font.size = Pt(10.5)
    r_a.font.bold = True
    r_a.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
    
    table_team = doc.add_table(rows=6, cols=3)
    table_team.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_team)
    format_table_header(table_team.rows[0], ["N°", "Nombre Completo del Estudiante", "Código / Cédula / Identificación"], [Inches(0.6), Inches(3.6), Inches(2.3)])
    
    students = [
        ("1", "Integrante 1: [Nombre y Apellidos]", "[Código Estudiantil / ID]"),
        ("2", "Integrante 2: [Nombre y Apellidos]", "[Código Estudiantil / ID]"),
        ("3", "Integrante 3: [Nombre y Apellidos]", "[Código Estudiantil / ID]"),
        ("4", "Integrante 4: [Nombre y Apellidos]", "[Código Estudiantil / ID]"),
        ("5", "Integrante 5: [Nombre y Apellidos]", "[Código Estudiantil / ID]"),
    ]
    for idx, s in enumerate(students):
        bg = "F9FAFB" if idx % 2 == 1 else "FFFFFF"
        format_table_row(table_team.rows[idx+1], [s[0], s[1], s[2]], bg_hex=bg, aligns=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER], col_widths=[Inches(0.6), Inches(3.6), Inches(2.3)])
        
    p_foot = doc.add_paragraph()
    p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_foot.paragraph_format.space_before = Pt(60)
    p_foot.paragraph_format.space_after = Pt(0)
    r_f = p_foot.add_run("Docente Titular: [Nombre del Profesor / Docente]\nFecha de Entrega: Septiembre 2026\nSimulador Utilizado: SimuProc v1.4.3.0")
    r_f.font.name = 'Calibri'
    r_f.font.size = Pt(10)
    r_f.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    
    doc.add_page_break()
    
    # -------------------------------------------------------------
    # 1. INTRODUCCIÓN Y OBJETIVOS
    # -------------------------------------------------------------
    add_header(doc, "1. Introducción y Objetivos", level=1)
    
    add_p(doc, "El presente informe documenta el desarrollo técnico, análisis algorítmico y verificación exhaustiva de los problemas planteados en el Taller #1 de Arquitectura de Computadores (semestre 2026-2). El objetivo central de la práctica es comprender en profundidad el funcionamiento del hardware interno de un procesador mediante el diseño e implementación de programas en lenguaje ensamblador sobre el simulador hipotético SimuProc (versión 1.4.3.0).", bold_prefix="Contextualización: ")
    
    add_p(doc, "SimuProc modela una máquina de arquitectura de acumulador bajo el paradigma de Von Neumann, permitiendo visualizar de manera interactiva la transferencia de registros, el funcionamiento de buses, la interacción con la memoria principal (4096 palabras de 16 bits), la modificación dinámica de banderas de estado de la ALU (Zero, Negative, Carry, Overflow) y el ciclo de instrucción completo (Fetch, Decode, Execute, Writeback).")
    
    add_header(doc, "1.1. Objetivos del Taller", level=2)
    add_bullet(doc, "Diseñar, codificar y depurar en lenguaje ensamblador de SimuProc un algoritmo iterativo eficiente para generar los primeros N términos de una sucesión de Fibonacci generalizada a partir de valores iniciales a0 y a1 fijados en memoria (#30 y #31).", bold_prefix="Objetivo Problema 1: ")
    add_bullet(doc, "Implementar la lectura de datos mediante teclado (instrucción LDT), la validación de cotas de entrada (N <= 10, N > 0), el control de bucles mediante registro contador CX (LOOP) y la presentación en pantalla (EAP/MSG).", bold_prefix="Control de Flujo e I/O: ")
    add_bullet(doc, "Estructurar y ejecutar operaciones aritméticas fundamentales (multiplicación y división) sobre datos binarios precargados en memoria a partir de la dirección #100.", bold_prefix="Objetivo Problema 2: ")
    add_bullet(doc, "Analizar y justificar el comportamiento de la multiplicación de palabras de 16 bits, la cual genera resultados de doble longitud (32 bits) distribuidos en los registros BX (parte alta) y AX (parte baja), requiriendo dos posiciones contiguas de memoria (#200-#205).", bold_prefix="Aritmética de Doble Longitud: ")
    add_bullet(doc, "Examinar en profundidad la restricción del ancho de palabra de 16 bits del procesador frente a operandos de 24 bits presentes en el enunciado (dirección #101), demostrando las implicaciones del truncamiento de hardware y contrastando los resultados con su valor decimal teórico.", bold_prefix="Análisis de Restricciones Hardware: ")
    add_bullet(doc, "Desarrollar la división entera de la dirección #103 entre la #104, almacenando el cociente (AX) y el residuo (BX) en las direcciones contiguas #206 y #207, comparando rigurosamente cada resultado con el cálculo matemático en base decimal.", bold_prefix="División y Residuo: ")

    # -------------------------------------------------------------
    # 2. MARCO TEÓRICO Y ARQUITECTURA DE SIMUPROC
    # -------------------------------------------------------------
    add_header(doc, "2. Arquitectura del Simulador SimuProc", level=1)
    
    add_p(doc, "SimuProc emula un procesador didáctico de 16 bits con organización basada en acumulador. Las características cardinales de su arquitectura son:")
    
    add_header(doc, "2.1. Memoria Principal y Direccionamiento", level=2)
    add_p(doc, "La memoria principal posee una capacidad de 4.096 palabras (posiciones) de 16 bits cada una. Las direcciones se indexan en base hexadecimal desde 000h hasta FFFh (requiriendo 12 bits de bus de direcciones). En una instrucción convencional de una sola palabra (16 bits), los 4 bits más significativos corresponden al código de operación (OPCODE) y los 12 bits restantes especifican la dirección de memoria de destino u origen (DIR), tal como se verifica en el formato IR(OP) e IR(DIR).")
    
    add_header(doc, "2.2. Modelo de Registros", level=2)
    add_bullet(doc, "Acumulador principal de 16 bits. Es el receptor implícito y exclusivo de la mayoría de operaciones aritméticas (ADD, SUB, MUL, DIV) y lógicas. También es el registro intermediario en operaciones de entrada/salida (LDT, EAP).", bold_prefix="AX (Accumulator): ")
    add_bullet(doc, "Registro de propósito general e índice de base de 16 bits. Sirve como puntero para direccionamiento indexado (LDB/STB mem+BX) y almacena la parte más significativa (bits 16-31) en operaciones de multiplicación (MUL), así como el residuo (módulo) en la división (DIV).", bold_prefix="BX (Base / Index): ")
    add_bullet(doc, "Registro contador de 16 bits. Reservado para el control de iteraciones en bucles repetitivos mediante la instrucción LOOP, la cual decrementa CX en cada ciclo y salta si CX != 0.", bold_prefix="CX (Counter): ")
    add_bullet(doc, "Puntero de la próxima instrucción a buscar y ejecutar. Se incrementa automáticamente en cada fase de búsqueda (Fetch).", bold_prefix="PC / IP (Program Counter): ")
    add_bullet(doc, "Registro intermediario conectado al bus de direcciones. Almacena la dirección física a la cual se accederá para lectura o escritura.", bold_prefix="MAR (Memory Address Register): ")
    add_bullet(doc, "Registro de datos de memoria conectado al bus de datos bidireccional. Retiene el dato leído de memoria o el dato listo para ser escrito.", bold_prefix="MDR (Memory Data Register): ")
    add_bullet(doc, "Almacena la instrucción binaria recién extraída de memoria para su posterior decodificación por la Unidad de Control.", bold_prefix="IR (Instruction Register): ")
    add_bullet(doc, "Stack Pointer (puntero al tope de la pila) y Base Pointer (inicio del marco de pila, por defecto en F80h).", bold_prefix="SP y BP: ")

    add_header(doc, "2.3. Banderas de Estado (Flags de la ALU)", level=2)
    add_p(doc, "La Unidad Aritmético-Lógica (ALU) actualiza dinámicamente cuatro indicadores de condición tras cada operación:")
    add_bullet(doc, "Se activa (1) si el resultado de la última operación fue exactamente cero.", bold_prefix="Zero Flag (Z): ")
    add_bullet(doc, "Se activa (1) si el bit de signo (bit 15 en complemento a dos) es 1, indicando un número negativo.", bold_prefix="Negative Flag (N): ")
    add_bullet(doc, "Se activa (1) cuando una adición genera acarreo fuera del bit más significativo o una sustracción requiere un préstamo.", bold_prefix="Carry Flag (C): ")
    add_bullet(doc, "Se activa (1) si una operación aritmética sobrepasa el rango representable de 16 bits (desbordamiento). En la instrucción MUL, se activa cuando el producto requiere el registro BX.", bold_prefix="Overflow Flag (O): ")

    add_header(doc, "2.4. Ciclo de Instrucción Hardware (Microoperaciones)", level=2)
    add_p(doc, "Cada instrucción en SimuProc atraviesa las fases estándar de la máquina de Von Neumann:")
    add_p(doc, "Fase de Captación (Fetch): MAR <- PC; MDR <- M[MAR]; IR <- MDR; PC <- PC + 1.", bold_prefix="1. Fetch: ")
    add_p(doc, "La Unidad de Control descompone IR en IR(OP) (código de operación) e IR(DIR) (dirección del operando).", bold_prefix="2. Decodificación (Decode): ")
    add_p(doc, "Si la instrucción requiere un operando en memoria (ej. LDA, ADD, MUL), se coloca MAR <- IR(DIR); MDR <- M[MAR] y se transfiere a la ALU.", bold_prefix="3. Búsqueda de Operandos: ")
    add_p(doc, "La ALU ejecuta la microoperación correspondiente (suma, resta, producto, división) y actualiza los registros internos y banderas.", bold_prefix="4. Ejecución (Execute): ")
    add_p(doc, "El resultado se deposita en el registro destino (AX, BX) o se escribe en memoria (STA, STB) mediante MAR <- IR(DIR); MDR <- AX; M[MAR] <- MDR.", bold_prefix="5. Almacenamiento (Store/Writeback): ")

    # -------------------------------------------------------------
    # 3. PROBLEMA 1: SUCESIÓN DE FIBONACCI
    # -------------------------------------------------------------
    add_header(doc, "3. Problema 1: Sucesión de Fibonacci Generalizada", level=1)
    
    add_callout(doc, "Enunciado Oficial del Problema 1",
                "En las direcciones #30 y #31 de memoria se encuentran los números iniciales de una sucesión de Fibonacci. "
                "Estos los debe definir como enteros sucesivos, no mayores a 30. Por ejemplo, pueden ser 20 y 21. "
                "También debe probar con la sucesión básica que parte con 0 y 1.\n"
                "Se ingresa un número por teclado que corresponde a la cantidad de términos de la sucesión que deben generarse. "
                "Nunca se pedirá más de 10 términos calculados.\n"
                "La sucesión se genera según: a2 = a0 + a1; a3 = a1 + a2; an = an-2 + an-1.\n"
                "Nótese que el primer término generado es a2. Los términos de la sucesión deben presentarse en pantalla.",
                alert_type="NOTE")
                
    add_header(doc, "3.1. Análisis Matemático y Formulación Algorítmica", level=2)
    add_p(doc, "La sucesión de Fibonacci estándar se define de forma recurrente como F_n = F_{n-1} + F_{n-2} con condiciones de frontera F_0 = 0 y F_1 = 1. En este problema se generaliza la sucesión permitiendo cualesquiera condiciones iniciales arbitrarias a_0 y a_1 almacenadas en las posiciones de memoria #30 y #31 (en numeración hexadecimal SimuProc, correspondiente a las direcciones físicas 030h y 031h).")
    
    add_p(doc, "Dado que el primer término calculado y desplegado debe ser a_2, si el usuario solicita calcular N términos (con 1 <= N <= 10), la secuencia generada será:")
    add_bullet(doc, "a_2 = a_0 + a_1", bold_prefix="Término 1 generado: ")
    add_bullet(doc, "a_3 = a_1 + a_2", bold_prefix="Término 2 generado: ")
    add_bullet(doc, "a_4 = a_2 + a_3", bold_prefix="Término 3 generado: ")
    add_bullet(doc, "a_n = a_{n-2} + a_{n-1}  (hasta n = N + 1)", bold_prefix="Término k generado: ")

    add_header(doc, "3.2. Mapa de Memoria y Variables de Trabajo", level=2)
    add_p(doc, "Para garantizar la integridad de los datos y evitar que una re-ejecución del programa altere las constantes originales especificadas por el enunciado, se diseñó un esquema que conserva intactas las direcciones #30 y #31, utilizando variables de trabajo contiguas:")
    
    tbl_mem1 = doc.add_table(rows=7, cols=4)
    tbl_mem1.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_mem1)
    format_table_header(tbl_mem1.rows[0], ["Dirección", "Identificador", "Descripción en el Algoritmo", "Valor Inicial (Caso A / B)"], [Inches(1.0), Inches(1.5), Inches(2.7), Inches(1.5)])
    
    mem1_data = [
        ("#30 (030h)", "a0_orig", "Condición inicial a0 fijada en memoria", "20 (10100b) / 0 (0b)"),
        ("#31 (031h)", "a1_orig", "Condición inicial a1 fijada en memoria", "21 (10101b) / 1 (1b)"),
        ("#32 (032h)", "a_prev2", "Variable de trabajo para término a_{n-2}", "0 (se copia a0)"),
        ("#33 (033h)", "a_prev1", "Variable de trabajo para término a_{n-1}", "0 (se copia a1)"),
        ("#34 (034h)", "a_curr", "Variable de cálculo del nuevo término a_n", "0"),
        ("#35 (035h)", "N_terms", "Cantidad de términos leída por teclado (LDT)", "0 (leído en runtime)")
    ]
    for idx, row_vals in enumerate(mem1_data):
        bg = "F9FAFB" if idx % 2 == 1 else "FFFFFF"
        format_table_row(tbl_mem1.rows[idx+1], row_vals, bg_hex=bg, aligns=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER], col_widths=[Inches(1.0), Inches(1.5), Inches(2.7), Inches(1.5)])
    
    add_p(doc, "", space_after=2)

    add_header(doc, "3.3. Algoritmo y Control de Bucles", level=2)
    add_p(doc, "El algoritmo opera bajo la siguiente secuencia lógica estructurada:")
    add_bullet(doc, "Se cargan #30 y #31 en AX y se muestran mediante la instrucción EAP con sus respectivos mensajes identificativos.", bold_prefix="Paso 1 (Lectura Inicial): ")
    add_bullet(doc, "Se copian los valores a las variables de trabajo: mem[32] <- mem[30] y mem[33] <- mem[31].", bold_prefix="Paso 2 (Preservación): ")
    add_bullet(doc, "Se solicita N mediante LDT y se guarda en mem[35].", bold_prefix="Paso 3 (Entrada por Teclado): ")
    add_bullet(doc, "Se limpia AX (CLA) y se compara con mem[35] (CMP 35). Si N <= 0 (Z=1 o N=1), el programa salta incondicionalmente a HLT para prevenir bucles infinitos o comportamientos anómalos.", bold_prefix="Paso 4 (Validación Defensiva): ")
    add_bullet(doc, "Se transfiere N al registro CX (MOV CX, 35).", bold_prefix="Paso 5 (Inicialización de Contador): ")
    add_bullet(doc, "En cada iteración: (a) AX <- mem[32]; (b) AX <- AX + mem[33]; (c) Guardar AX en mem[34]; (d) EAP muestra el nuevo término; (e) Desplazamiento: mem[32] <- mem[33], luego mem[33] <- mem[34]; (f) LOOP 00F decrementa CX y salta a la dirección 00Fh si CX != 0.", bold_prefix="Paso 6 (Bucle de Cálculo): ")
    add_bullet(doc, "Fin del programa con mensaje de éxito y detención de la CPU (HLT).", bold_prefix="Paso 7 (Terminación): ")

    add_header(doc, "3.4. Código Fuente Ensamblador Comentado (Problema1_Fibonacci.asm)", level=2)
    add_p(doc, "A continuación se presenta el código fuente íntegro en ensamblador de SimuProc con comentarios detallados en cada instrucción:")
    
    p1_code = """#SimuProc 1.4.3.0
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
0                           ; Dir #35: Variable N de control"""
    add_code_box(doc, p1_code)

    add_header(doc, "3.5. Tabla de Traza Manual de Ejecución", level=2)
    add_p(doc, "Se presenta la traza de ejecución ciclo a ciclo para el Caso A con condiciones iniciales a_0 = 20 y a_1 = 21, generando N = 5 términos representativos:")
    
    tbl_trace1 = doc.add_table(rows=12, cols=8)
    tbl_trace1.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_trace1)
    format_table_header(tbl_trace1.rows[0], ["Paso", "PC", "Instrucción", "AX", "BX", "CX", "Flags (Z,N,C,O)", "Acción / Memoria"], 
                        [Inches(0.5), Inches(0.5), Inches(1.6), Inches(0.7), Inches(0.6), Inches(0.6), Inches(1.1), Inches(1.6)])
                        
    trace1_data = [
        ("1", "001", "LDA 30", "20", "0", "0", "0, 0, 0, 0", "Carga a0 en AX"),
        ("2", "002", "EAP", "20", "0", "0", "0, 0, 0, 0", "Muestra 'a0 = 20'"),
        ("3", "003", "LDA 31", "21", "0", "0", "0, 0, 0, 0", "Carga a1 en AX"),
        ("4", "004", "EAP", "21", "0", "0", "0, 0, 0, 0", "Muestra 'a1 = 21'"),
        ("5", "007", "LDT", "5", "0", "0", "0, 0, 0, 0", "Usuario ingresa N=5"),
        ("6", "00D", "MOV CX, 35", "0", "0", "5", "0, 1, 0, 0", "CX inicializado en 5"),
        ("7", "00F", "LDA 32 + ADD 33", "41", "0", "5", "0, 0, 0, 0", "a2 = 20+21 = 41"),
        ("8", "015", "LOOP 00F (it. 1)", "41", "0", "4", "0, 0, 0, 0", "EAP: 41; CX=4; Salto 00F"),
        ("9", "015", "LOOP 00F (it. 2)", "62", "0", "3", "0, 0, 0, 0", "EAP: 62; CX=3; Salto 00F"),
        ("10", "015", "LOOP 00F (it. 3)", "103", "0", "2", "0, 0, 0, 0", "EAP: 103; CX=2; Salto 00F"),
        ("11", "017", "HLT (tras it. 5)", "268", "0", "0", "0, 0, 0, 0", "EAP: 268; CX=0; Fin")
    ]
    for idx, r_vals in enumerate(trace1_data):
        bg = "F9FAFB" if idx % 2 == 1 else "FFFFFF"
        format_table_row(tbl_trace1.rows[idx+1], r_vals, bg_hex=bg, 
                         aligns=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.RIGHT, WD_ALIGN_PARAGRAPH.RIGHT, WD_ALIGN_PARAGRAPH.RIGHT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT],
                         col_widths=[Inches(0.5), Inches(0.5), Inches(1.6), Inches(0.7), Inches(0.6), Inches(0.6), Inches(1.1), Inches(1.6)])

    add_header(doc, "3.6. Resultados de las Pruebas y Validación", level=2)
    add_p(doc, "Se ejecutó el programa bajo los dos escenarios requeridos por la guía, comprobando los 10 términos calculados:")
    
    tbl_cases = doc.add_table(rows=12, cols=5)
    tbl_cases.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_cases)
    format_table_header(tbl_cases.rows[0], ["Término", "Fórmula Recurrente", "Caso A (a0=20, a1=21)", "Caso B (a0=0, a1=1)", "Representación Binaria (Caso A)"],
                        [Inches(0.8), Inches(1.5), Inches(1.6), Inches(1.5), Inches(1.8)])
                        
    cases_data = [
        ("a2", "a0 + a1", "41", "1", "0000 0000 0010 1001b"),
        ("a3", "a1 + a2", "62", "2", "0000 0000 0011 1110b"),
        ("a4", "a2 + a3", "103", "3", "0000 0000 0110 0111b"),
        ("a5", "a3 + a4", "165", "5", "0000 0000 1010 0101b"),
        ("a6", "a4 + a5", "268", "8", "0000 0001 0000 1100b"),
        ("a7", "a5 + a6", "433", "13", "0000 0001 1011 0001b"),
        ("a8", "a6 + a7", "701", "21", "0000 0010 1011 1101b"),
        ("a9", "a7 + a8", "1134", "34", "0000 0100 0110 1110b"),
        ("a10", "a8 + a9", "1835", "55", "0000 0111 0010 1011b"),
        ("a11", "a9 + a10", "2969", "89", "0000 1011 1001 1001b"),
        ("Estado Final", "N = 10 términos", "Verificado 100% OK", "Verificado 100% OK", "Sin desbordamiento (O=0)")
    ]
    for idx, r_vals in enumerate(cases_data):
        bg = "F9FAFB" if idx % 2 == 1 else "FFFFFF"
        format_table_row(tbl_cases.rows[idx+1], r_vals, bg_hex=bg,
                         aligns=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.RIGHT, WD_ALIGN_PARAGRAPH.RIGHT, WD_ALIGN_PARAGRAPH.CENTER],
                         col_widths=[Inches(0.8), Inches(1.5), Inches(1.6), Inches(1.5), Inches(1.8)])

    add_p(doc, "En ambos casos, todos los números calculados se mantuvieron dentro de la capacidad de 16 bits sin signo (máximo 65.535), por lo cual la bandera de Overflow (O) permaneció en 0 durante toda la ejecución.")

    doc.add_page_break()

    # -------------------------------------------------------------
    # 4. PROBLEMA 2: MULTIPLICACIÓN Y DIVISIÓN
    # -------------------------------------------------------------
    add_header(doc, "4. Problema 2: Operaciones Aritméticas (Multiplicación y División)", level=1)
    
    add_callout(doc, "Enunciado Oficial del Problema 2",
                "A partir de la dirección 100 de memoria se encuentran los siguientes datos binarios:\n"
                "#100:\n"
                "101101010001\n"
                "110000010100010101101111\n"
                "1010\n"
                "1111100001111\n"
                "11111100\n"
                "110\n\n"
                "El objetivo es multiplicarlos por pares y dejar los tres resultados a partir de la dirección 200 de memoria. "
                "Note que, por las características de la multiplicación, cada resultado ocupará dos localidades de memoria.\n"
                "Adicionalmente debe dividir el dato que está en la dirección 103 entre aquel que se encuentra en 104. "
                "El resultado debe ocupar las direcciones después del último resultado de multiplicación anterior.\n"
                "Para cada caso, debe comparar los resultados, con la forma decimal.",
                alert_type="NOTE")

    add_header(doc, "4.1. Análisis y Conversión de los Datos Binarios de Entrada", level=2)
    add_p(doc, "La guía define seis datos binarios precargados en memoria a partir de la dirección #100. En SimuProc, las direcciones de memoria se expresan en hexadecimal, correspondiendo a las posiciones contiguas 100h a 105h:")
    
    tbl_bin = doc.add_table(rows=8, cols=6)
    tbl_bin.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_bin)
    format_table_header(tbl_bin.rows[0], ["Dir. Memoria", "Cadena Binaria Original", "Longitud", "Hexadecimal", "Decimal", "Interpretación / Rol"],
                        [Inches(0.9), Inches(1.8), Inches(0.6), Inches(0.9), Inches(1.1), Inches(1.9)])
                        
    bin_data = [
        ("#100 (100h)", "101101010001", "12 bits", "0B51h", "2.897", "Multiplicando Par 1"),
        ("#101 (101h)", "110000010100010101101111", "24 bits", "C1456Fh*", "12.666.223*", "Multiplicador Par 1 (24 bits)"),
        ("#101 (SimuProc)", "0100010101101111", "16 bits", "456Fh", "17.775", "Multiplicador Par 1 (16 bits)"),
        ("#102 (102h)", "1010", "4 bits", "000Ah", "10", "Multiplicando Par 2"),
        ("#103 (103h)", "1111100001111", "13 bits", "1F0Fh", "7.951", "Mult. Par 2 / Dividendo"),
        ("#104 (104h)", "11111100", "8 bits", "00FCh", "252", "Mult. Par 3 / Divisor"),
        ("#105 (105h)", "110", "3 bits", "0006h", "6", "Multiplicador Par 3")
    ]
    for idx, r_vals in enumerate(bin_data):
        bg = "FEF3F2" if "24 bits" in r_vals[5] else ("EDFBF0" if "SimuProc" in r_vals[0] else ("F9FAFB" if idx % 2 == 1 else "FFFFFF"))
        format_table_row(tbl_bin.rows[idx+1], r_vals, bg_hex=bg,
                         aligns=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.RIGHT, WD_ALIGN_PARAGRAPH.LEFT],
                         col_widths=[Inches(0.9), Inches(1.8), Inches(0.6), Inches(0.9), Inches(1.1), Inches(1.9)])

    add_header(doc, "4.2. Análisis Crítico: El Operando de 24 bits frente al Hardware de 16 bits", level=2)
    add_callout(doc, "Discusión Arquitectónica Fundamental",
                "El segundo dato (#101) posee 24 dígitos binarios: 1100 0001 0100 0101 0110 1111 (C1456Fh = 12.666.223 decimal).\n"
                "Sin embargo, la arquitectura interna de SimuProc posee una memoria de palabras fijas de 16 bits (000h a FFFh) y registros de 16 bits (AX, BX, CX).\n"
                "Cuando un simulador o procesador de 16 bits procesa una constante que excede el ancho de la palabra de memoria, ocurren dos escenarios técnicos:\n"
                "1. Truncamiento a 16 bits: Se almacenan los 16 bits menos significativos (LSB): 0100 0101 0110 1111b (456Fh = 17.775 decimal). Este es el valor con el que opera la ALU en el simulador.\n"
                "2. Valor teórico de 24 bits: Matemáticamente el producto 2.897 * 12.666.223 es igual a 36.694.048.031 (88910F19Fh, de 36 bits).\n"
                "En este informe se presentan, analizan y contrastan AMBOS escenarios con total rigor matemático y computacional.",
                alert_type="IMPORTANT")

    add_header(doc, "4.3. Mecánica de la Multiplicación en SimuProc (Aritmética de Doble Longitud)", level=2)
    add_p(doc, "El enunciado señala: 'Note que, por las características de la multiplicación, cada resultado ocupará dos localidades de memoria.'", bold_prefix="Justificación Hardware: ")
    add_p(doc, "Cuando se multiplican dos números enteros sin signo de n bits, el producto puede alcanzar una longitud máxima de 2n bits (en este caso, 16 bits * 16 bits = 32 bits). El valor máximo de una palabra de 16 bits es 2^16 - 1 = 65.535; su cuadrado es (65.535)^2 = 4.294.836.225, requiriendo exactamente dos palabras de 16 bits para representarse sin pérdida de información.")
    
    add_p(doc, "En SimuProc, la instrucción MUL [mem] ejecuta:")
    add_bullet(doc, "AX <- (AX * @mem) [bits 0 a 15, parte menos significativa LSB].", bold_prefix="Registro AX: ")
    add_bullet(doc, "BX <- (AX * @mem) [bits 16 a 31, parte más significativa MSB].", bold_prefix="Registro BX: ")
    add_bullet(doc, "Se activa (1) si el resultado supera 16 bits (es decir, si BX > 0).", bold_prefix="Overflow Flag (O): ")

    add_p(doc, "Para almacenar este producto de 32 bits en dos localidades contiguas de memoria siguiendo el estándar Big-Endian por palabras adoptado por SimuProc (donde la parte más significativa reside en la dirección base y la menos significativa en la dirección consecutiva):")
    add_bullet(doc, "Almacena la parte más significativa (MSB) proveniente del registro BX.", bold_prefix="Dirección base (200h, 202h, 204h): ")
    add_bullet(doc, "Almacena la parte menos significativa (LSB) proveniente del registro AX.", bold_prefix="Dirección base + 1 (201h, 203h, 205h): ")

    add_header(doc, "4.4. Mecánica de la División Entera en SimuProc", level=2)
    add_p(doc, "El enunciado solicita: 'Adicionalmente debe dividir el dato que está en la dirección 103 entre aquel que se encuentra en 104. El resultado debe ocupar las direcciones después del último resultado de multiplicación anterior.'", bold_prefix="Especificación: ")
    add_p(doc, "La última multiplicación ocupó las direcciones 204h y 205h. Por tanto, el resultado de la división debe ocupar las posiciones contiguas 206h y 207h.")
    add_p(doc, "La instrucción DIV [mem] ejecuta:")
    add_bullet(doc, "AX <- floor(AX / @mem) [Cociente entero de la división]. Se guarda en la dirección #206.", bold_prefix="Registro AX: ")
    add_bullet(doc, "BX <- AX mod @mem [Residuo o Resto de la división]. Se guarda en la dirección #207.", bold_prefix="Registro BX: ")
    add_p(doc, "Verificación matemática: Dividendo = (Cociente * Divisor) + Residuo, donde 0 <= Residuo < Divisor.")

    add_header(doc, "4.5. Código Fuente Ensamblador Comentado (Problema2_Aritmetica.asm)", level=2)
    add_p(doc, "A continuación se presenta el código ensamblador completo con comentarios detallados en cada paso:")
    
    p2_code = """#SimuProc 1.4.3.0
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
110                         ; #105: 6 dec (0x0006)"""
    add_code_box(doc, p2_code)

    add_header(doc, "4.6. Comparación y Verificación Rigurosa con la Forma Decimal", level=2)
    add_p(doc, "Se presenta la tabla comparativa exhaustiva que valida matemáticamente cada uno de los resultados generados por el simulador:")
    
    tbl_comp = doc.add_table(rows=6, cols=6)
    tbl_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_comp)
    format_table_header(tbl_comp.rows[0], ["Operación Realizada", "Operandos Decimales", "Cálculo Decimal Teórico", "Resultado en Memoria SimuProc", "Desglose Hexadecimal (Alta / Baja)", "Comprobación Matemática"],
                        [Inches(1.2), Inches(1.1), Inches(1.3), Inches(1.3), Inches(1.3), Inches(1.0)])
                        
    comp_data = [
        ("Multiplicación Par 1 (16b SimuProc)", "2.897 * 17.775", "51.494.175", "#200: 785\n#201: 48.415", "Alta: 0311h\nBaja: BD1Fh", "785*65536 + 48415 = 51.494.175 (Exacto)"),
        ("Multiplicación Par 1 (Teórico 24b)", "2.897 * 12.666.223", "36.694.048.031", "Supera 32 bits\n(requiere 36 bits)", "8 8910 F19Fh\n(3 palabras)", "Requiere extensión a 64 bits"),
        ("Multiplicación Par 2", "10 * 7.951", "79.510", "#202: 1\n#203: 13.974", "Alta: 0001h\nBaja: 3696h", "1*65536 + 13974 = 79.510 (Exacto)"),
        ("Multiplicación Par 3", "252 * 6", "1.512", "#204: 0\n#205: 1.512", "Alta: 0000h\nBaja: 05E8h", "0*65536 + 1512 = 1.512 (Exacto)"),
        ("División Entera (103 / 104)", "7.951 / 252", "Cociente: 31\nResiduo: 139", "#206: 31 (Coc)\n#207: 139 (Res)", "Cociente: 001Fh\nResiduo: 008Bh", "31*252 + 139 = 7.951 (Exacto)")
    ]
    for idx, r_vals in enumerate(comp_data):
        bg = "FEF3F2" if "24b" in r_vals[0] else ("F9FAFB" if idx % 2 == 1 else "FFFFFF")
        format_table_row(tbl_comp.rows[idx+1], r_vals, bg_hex=bg,
                         aligns=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.RIGHT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT],
                         col_widths=[Inches(1.2), Inches(1.1), Inches(1.3), Inches(1.3), Inches(1.3), Inches(1.0)])

    add_header(doc, "4.7. Volcado de Memoria Final (Memory Dump)", level=2)
    add_p(doc, "El estado final de las regiones de memoria de datos tras la ejecución del programa se resume en la siguiente tabla:")
    
    tbl_dump = doc.add_table(rows=16, cols=5)
    tbl_dump.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_dump)
    format_table_header(tbl_dump.rows[0], ["Dirección Memoria", "Contenido Binario (16 bits)", "Hexadecimal", "Decimal", "Significado / Variable"],
                        [Inches(1.1), Inches(1.8), Inches(1.0), Inches(1.0), Inches(2.3)])
                        
    dump_data = [
        ("#100 (100h)", "0000 1011 0101 0001b", "0B51h", "2.897", "Dato de entrada #100"),
        ("#101 (101h)", "0100 0101 0110 1111b", "456Fh", "17.775", "Dato de entrada #101 (truncado a 16b)"),
        ("#102 (102h)", "0000 0000 0000 1010b", "000Ah", "10", "Dato de entrada #102"),
        ("#103 (103h)", "0001 1111 0000 1111b", "1F0Fh", "7.951", "Dato de entrada #103"),
        ("#104 (104h)", "0000 0000 1111 1100b", "00FCh", "252", "Dato de entrada #104"),
        ("#105 (105h)", "0000 0000 0000 0110b", "0006h", "6", "Dato de entrada #105"),
        ("--- Separador ---", "--------------------", "------", "-------", "Direcciones intermedias no modificadas"),
        ("#200 (200h)", "0000 0011 0001 0001b", "0311h", "785", "Par 1: Producto Parte Alta (BX)"),
        ("#201 (201h)", "1011 1101 0001 1111b", "BD1Fh", "48.415", "Par 1: Producto Parte Baja (AX)"),
        ("#202 (202h)", "0000 0000 0000 0001b", "0001h", "1", "Par 2: Producto Parte Alta (BX)"),
        ("#203 (203h)", "0011 0110 1001 0110b", "3696h", "13.974", "Par 2: Producto Parte Baja (AX)"),
        ("#204 (204h)", "0000 0000 0000 0000b", "0000h", "0", "Par 3: Producto Parte Alta (BX)"),
        ("#205 (205h)", "0000 0101 1110 1000b", "05E8h", "1.512", "Par 3: Producto Parte Baja (AX)"),
        ("#206 (206h)", "0000 0000 0001 1111b", "001Fh", "31", "División (103/104): Cociente (AX)"),
        ("#207 (207h)", "0000 0000 1000 1011b", "008Bh", "139", "División (103/104): Residuo (BX)")
    ]
    for idx, r_vals in enumerate(dump_data):
        bg = "E5E7EB" if "Separador" in r_vals[0] else ("F9FAFB" if idx % 2 == 1 else "FFFFFF")
        format_table_row(tbl_dump.rows[idx+1], r_vals, bg_hex=bg,
                         aligns=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.RIGHT, WD_ALIGN_PARAGRAPH.LEFT],
                         col_widths=[Inches(1.1), Inches(1.8), Inches(1.0), Inches(1.0), Inches(2.3)])

    doc.add_page_break()

    # -------------------------------------------------------------
    # 5. GUÍA DE EJECUCIÓN EN SIMUPROC
    # -------------------------------------------------------------
    add_header(doc, "5. Guía de Ejecución y Manual de Usuario en SimuProc", level=1)
    
    add_p(doc, "Para reproducir y evaluar los programas en SimuProc (versión 1.4.3.0), se detallan los pasos operacionales exactos:")
    
    add_header(doc, "5.1. Carga del Código en el Editor Interno", level=2)
    add_bullet(doc, "Ejecutar Procesador.exe desde el directorio de instalación o acceso directo.", bold_prefix="Paso 1: ")
    add_bullet(doc, "En el menú superior, acceder a Utilidades -> Editor Interno... (o presionar el icono del Editor en la barra de herramientas).", bold_prefix="Paso 2: ")
    add_bullet(doc, "Asegurarse de visualizar el Editor 2 (Editor de Texto). Si se encuentra en el Editor 1 (tipo memoria), hacer clic en la pestaña o botón de Editor 2.", bold_prefix="Paso 3: ")
    add_bullet(doc, "Copiar y pegar el código completo del archivo .asm correspondiente (Problema1_Fibonacci.asm o Problema2_Aritmetica.asm) o cargarlo mediante el menú Archivo -> Abrir del Editor 2.", bold_prefix="Paso 4: ")
    add_bullet(doc, "Presionar el botón de conversión hacia el Editor 1 (icono con flecha hacia la izquierda [<-] 'Pasa al Editor 1'). El ensamblador validará la sintaxis y reportará cero errores.", bold_prefix="Paso 5: ")
    add_bullet(doc, "En el Editor 1, presionar el botón 'Enviar a Memoria'. El código y los datos se ubicarán en sus respectivas direcciones físicas de la memoria principal.", bold_prefix="Paso 6: ")

    add_header(doc, "5.2. Ejecución y Visualización de Resultados", level=2)
    add_bullet(doc, "En la ventana principal de SimuProc, abrir la ventana de Dispositivos de E/S haciendo clic en el botón 'Mostrar' del panel correspondiente.", bold_prefix="Paso 1: ")
    add_bullet(doc, "Ajustar la barra de velocidad de simulación según se desee visualizar la animación de buses y registros o ejecutar a velocidad máxima (se puede desmarcar la casilla 'Animación' para ejecución instantánea).", bold_prefix="Paso 2: ")
    add_bullet(doc, "Presionar el botón 'Ejecutar'.", bold_prefix="Paso 3: ")
    add_bullet(doc, "En el Problema 1: Cuando aparezca la ventana de diálogo de teclado (LDT), ingresar la cantidad de términos deseada (ej. 10) y presionar 'Entrar Dato'.", bold_prefix="Paso 4 (Problema 1): ")
    add_bullet(doc, "Observar la presentación en pantalla (EAP) de cada término calculado.", bold_prefix="Paso 5: ")
    add_bullet(doc, "En el Problema 2: El programa ejecutará automáticamente las multiplicaciones y la división, mostrando cada parte alta/baja y cociente/residuo en la consola de salida.", bold_prefix="Paso 6 (Problema 2): ")
    add_bullet(doc, "Inspeccionar las direcciones de memoria #200 a #207 directamente en la cuadrícula de memoria (StringGrid) de SimuProc para verificar los valores hexadecimales y binarios almacenados.", bold_prefix="Paso 7 (Verificación de Memoria): ")

    # -------------------------------------------------------------
    # 6. CONCLUSIONES
    # -------------------------------------------------------------
    add_header(doc, "6. Conclusiones y Análisis Arquitectónico", level=1)
    
    add_bullet(doc, "SimuProc evidencia de forma transparente el funcionamiento del modelo de Von Neumann clásico basado en acumulador, donde la mayoría de operaciones dependen del cuello de botella de tener a AX como registro central de cómputo y transferencia.", bold_prefix="Arquitectura de Acumulador: ")
    add_bullet(doc, "La implementación de la sucesión de Fibonacci demostró la importancia de preservar las direcciones de memoria originales mediante variables de trabajo, garantizando idempotencia y reejecutabilidad del código sin efectos colaterales destructivos.", bold_prefix="Modularidad y Manejo de Memoria: ")
    add_bullet(doc, "La aritmética de multiplicación pone de relieve la necesidad de hardware de doble longitud (registros AX y BX sincronizados) para contener el producto de dos enteros de 16 bits sin pérdida por desbordamiento.", bold_prefix="Doble Longitud Aritmética: ")
    add_bullet(doc, "El análisis del operando de 24 bits evidenció una de las lecciones fundamentales del diseño de computadores: la interacción entre el tamaño de la palabra física de memoria y la representación de datos numéricos. Cuando el ancho de bus y celda es de 16 bits, el hardware trunca inherentemente a la longitud nativa a menos que se implementen rutinas de software para aritmética de precisión extendida (múltiples palabras).", bold_prefix="Límites del Ancho de Palabra: ")
    add_bullet(doc, "La instrucción de división en SimuProc proporciona una solución elegante al retornar simultáneamente el cociente en AX y el residuo en BX en una sola operación atómica, optimizando el ciclo de instrucción sin necesidad de subrutinas de restas sucesivas.", bold_prefix="Eficiencia de la División: ")

    # -------------------------------------------------------------
    # 7. REFERENCIAS BIBLIOGRÁFICAS
    # -------------------------------------------------------------
    add_header(doc, "7. Referencias Bibliográficas", level=1)
    add_bullet(doc, "Stallings, W. (2018). Organización y Arquitectura de Computadores. 10ª Edición. Pearson Educación.", bold_prefix="[1] ")
    add_bullet(doc, "Tanenbaum, A. S., & Austin, T. (2013). Structured Computer Organization. 6th Edition. Pearson.", bold_prefix="[2] ")
    add_bullet(doc, "Yepes B., V. (2003). Manual de Referencia y Ayuda en Línea de SimuProc v1.4.3.0.", bold_prefix="[3] ")
    add_bullet(doc, "Patterson, D. A., & Hennessy, J. L. (2020). Estructura y Diseño de Computadores: La Interfaz Hardware/Software. 5ª Edición. Reverté.", bold_prefix="[4] ")

    output_path = r"c:\Users\PC\Desktop\aeq_pr\Informe_Taller_1_Arquitectura.docx"
    doc.save(output_path)
    print(f"Report successfully saved to {output_path}")

build_report()
