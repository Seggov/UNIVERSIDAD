import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

pdf_path = "output/pdf/Estadisticas_Auditoria_Usuarios_ISO27001.pdf"
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=landscape(letter),
    leftMargin=36,
    rightMargin=36,
    topMargin=30,
    bottomMargin=30
)

styles = getSampleStyleSheet()

# Custom styles
style_title = ParagraphStyle(
    'DocTitle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=18,
    leading=22,
    textColor=colors.HexColor('#1A365D')
)

style_subtitle = ParagraphStyle(
    'DocSubTitle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#4A5568')
)

style_section = ParagraphStyle(
    'SectionHeader',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=16,
    textColor=colors.HexColor('#2B6CB0'),
    spaceAfter=6
)

style_card_title = ParagraphStyle(
    'CardTitle',
    fontName='Helvetica-Bold',
    fontSize=8.5,
    leading=11,
    textColor=colors.HexColor('#4A5568'),
    alignment=1
)

style_card_value = ParagraphStyle(
    'CardValue',
    fontName='Helvetica-Bold',
    fontSize=18,
    leading=22,
    alignment=1
)

style_card_sub = ParagraphStyle(
    'CardSub',
    fontName='Helvetica',
    fontSize=7.5,
    leading=10,
    textColor=colors.HexColor('#718096'),
    alignment=1
)

style_cell = ParagraphStyle(
    'CellText',
    fontName='Helvetica',
    fontSize=8.5,
    leading=11,
    textColor=colors.HexColor('#2D3748')
)

style_cell_bold = ParagraphStyle(
    'CellTextBold',
    fontName='Helvetica-Bold',
    fontSize=8.5,
    leading=11,
    textColor=colors.HexColor('#1A202C')
)

story = []

# =========================================================================
# PÁGINA 1: DASHBOARD EJECUTIVO Y DIAGNÓSTICO GENERAL
# =========================================================================
# Header
header_data = [
    [
        Paragraph("<b>UNIVERSIDAD CATÓLICA DEL NORTE · AUSTRANET</b><br/>"
                  "<font color='#2B6CB0'><b>Auditoría de Seguridad Cloud · Grupo 1: Identidades y Accesos</b></font>", style_subtitle),
        Paragraph("<font color='#718096'>Corte de Evaluación: <b>28 de Octubre de 2026</b><br/>"
                  "Estándar: <b>ISO/IEC 27001:2022</b></font>", ParagraphStyle('HRight', parent=style_subtitle, alignment=2))
    ]
]
t_head = Table(header_data, colWidths=[450, 270])
t_head.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
]))
story.append(t_head)
story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#CBD5E1'), spaceBefore=8, spaceAfter=10))

story.append(Paragraph("INFORME ESTADÍSTICO DE GOBERNANZA DE IDENTIDADES EN LA NUBE", style_title))
story.append(Paragraph("Evaluación de cumplimiento de políticas SGSI-POL-04, PRO-06 y PRO-07 sobre 495 cuentas Microsoft Entra ID", style_subtitle))
story.append(Spacer(1, 10))

# KPI Cards
kpi_data = [
    [
        [Paragraph("UNIVERSO AUDITADO", style_card_title),
         Paragraph("<font color='#1A365D'>495</font>", style_card_value),
         Paragraph("189 Internos / 306 Guests", style_card_sub)],
        
        [Paragraph("ZONA CRÍTICA (ROJO)", style_card_title),
         Paragraph("<font color='#E53E3E'>108</font>", style_card_value),
         Paragraph("21.8% Población Total", style_card_sub)],
        
        [Paragraph("INTERNOS IRREGULARES", style_card_title),
         Paragraph("<font color='#E53E3E'>57.1%</font>", style_card_value),
         Paragraph("108 de 189 Miembros", style_card_sub)],
        
        [Paragraph("AHORRO DE LICENCIAS", style_card_title),
         Paragraph("<font color='#6B46C1'>46 Cuentas</font>", style_card_value),
         Paragraph("Bloqueadas &gt; 60 días", style_card_sub)],
        
        [Paragraph("URGENCIA PREVENTIVA", style_card_title),
         Paragraph("<font color='#DD6B20'>235</font>", style_card_value),
         Paragraph("47.5% (Terceros y Cuarentena)", style_card_sub)]
    ]
]
t_kpis = Table(kpi_data, colWidths=[144, 144, 144, 144, 144])
t_kpis.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (0,0), colors.HexColor('#F8FAFC')),
    ('BACKGROUND', (1,0), (1,0), colors.HexColor('#FFF5F5')),
    ('BACKGROUND', (2,0), (2,0), colors.HexColor('#FFF5F5')),
    ('BACKGROUND', (3,0), (3,0), colors.HexColor('#FAF5FF')),
    ('BACKGROUND', (4,0), (4,0), colors.HexColor('#FFFAF0')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#E2E8F0')),
    ('INNERGRID', (0,0), (-1,-1), 1, colors.HexColor('#E2E8F0')),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
]))
story.append(t_kpis)
story.append(Spacer(1, 15))

# Fila con los 2 primeros gráficos (Donut y Comparativa)
charts_row1 = [
    [
        Image("tmp/charts/chart1_donut_urgencia.png", width=3.7*inch, height=2.4*inch),
        Image("tmp/charts/chart3_comparativa.png", width=4.3*inch, height=2.4*inch)
    ]
]
t_charts1 = Table(charts_row1, colWidths=[360, 360])
t_charts1.setStyle(TableStyle([
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ('TOPPADDING', (0,0), (-1,-1), 0),
]))
story.append(t_charts1)

story.append(PageBreak())

# =========================================================================
# PÁGINA 2: ZOOM COLABORADORES INTERNOS Y TABLA DE DATOS
# =========================================================================
story.append(Paragraph("DIAGNÓSTICO CRÍTICO: COLABORADORES INTERNOS (189 CUENTAS)", style_title))
story.append(Paragraph("Foco prioritario de la Fase 1 del proyecto: El 57.1% de las identidades internas requiere acción inmediata", style_subtitle))
story.append(Spacer(1, 8))

# Gráfico 2 + Tabla Resumen lado a lado
table_members_data = [
    [
        Paragraph("<b>Nivel</b>", style_cell_bold),
        Paragraph("<b>Categoría de Auditoría</b>", style_cell_bold),
        Paragraph("<b>Cuentas</b>", style_cell_bold),
        Paragraph("<b>% Interno</b>", style_cell_bold)
    ],
    [
        Paragraph("<font color='#E53E3E'><b>ROJO</b></font>", style_cell),
        Paragraph("Inactivos &gt; 60 días (Habilitados)", style_cell),
        Paragraph("53", style_cell_bold),
        Paragraph("28.0%", style_cell)
    ],
    [
        Paragraph("<font color='#E53E3E'><b>ROJO</b></font>", style_cell),
        Paragraph("Bloqueados &ge; 60d (Offboarding pendiente)", style_cell),
        Paragraph("46", style_cell_bold),
        Paragraph("24.3%", style_cell)
    ],
    [
        Paragraph("<font color='#E53E3E'><b>ROJO</b></font>", style_cell),
        Paragraph("Especiales / Admin con Inactividad", style_cell),
        Paragraph("9", style_cell_bold),
        Paragraph("4.8%", style_cell)
    ],
    [
        Paragraph("<font color='#DD6B20'><b>AMARILLO</b></font>", style_cell),
        Paragraph("Nuevos sin Login (Regla 5 días)", style_cell),
        Paragraph("5", style_cell_bold),
        Paragraph("2.6%", style_cell)
    ],
    [
        Paragraph("<font color='#DD6B20'><b>AMARILLO</b></font>", style_cell),
        Paragraph("Alerta Preventiva (30 a 59 días)", style_cell),
        Paragraph("3", style_cell_bold),
        Paragraph("1.6%", style_cell)
    ],
    [
        Paragraph("<font color='#38A169'><b>VERDE</b></font>", style_cell),
        Paragraph("Bloqueados Recientes (&lt; 60d retención)", style_cell),
        Paragraph("16", style_cell_bold),
        Paragraph("8.5%", style_cell)
    ],
    [
        Paragraph("<font color='#38A169'><b>VERDE</b></font>", style_cell),
        Paragraph("Especiales / Admin Activos", style_cell),
        Paragraph("9", style_cell_bold),
        Paragraph("4.8%", style_cell)
    ],
    [
        Paragraph("<font color='#38A169'><b>VERDE</b></font>", style_cell),
        Paragraph("Activos Regulares (&lt; 30 días)", style_cell),
        Paragraph("48", style_cell_bold),
        Paragraph("25.4%", style_cell)
    ],
    [
        Paragraph("<b>TOTAL</b>", style_cell_bold),
        Paragraph("<b>Colaboradores Internos Auditados</b>", style_cell_bold),
        Paragraph("<b>189</b>", style_cell_bold),
        Paragraph("<b>100.0%</b>", style_cell_bold)
    ]
]
t_members = Table(table_members_data, colWidths=[65, 175, 45, 55])
t_members.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#EDF2F7')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
    ('ROWBACKGROUNDS', (0,1), (-1,-2), [colors.white, colors.HexColor('#F8FAFC')]),
    ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#E2E8F0')),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
]))

row2_content = [
    [
        Image("tmp/charts/chart2_internos_bar.png", width=4.8*inch, height=2.8*inch),
        t_members
    ]
]
t_row2 = Table(row2_content, colWidths=[380, 340])
t_row2.setStyle(TableStyle([
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 0),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
]))
story.append(t_row2)
story.append(Spacer(1, 15))

# Hallazgo clave en tarjeta inferior
callout_data = [
    [
        Paragraph("<b>⚠️ HALLAZGO DE AUDITORÍA PRINCIPAL PARA AUSTRANET (Cláusulas 9.1 y 9.2 de ISO 27001):</b><br/>"
                  "El <b>57.1% de las identidades internas de la organización presenta incumplimientos normativos directos</b>: "
                  "53 cuentas continúan habilitadas a pesar de superar el umbral de 60 días de inactividad estipulado en SGSI-PRO-06, "
                  "mientras que 46 cuentas ya bloqueadas han sobrepasado la ventana de retención sin que se complete el offboarding "
                  "(generando costos innecesarios de licencias Microsoft 365). Se justifica plenamente la implementación inmediata "
                  "del Runbook de PowerShell en Azure Automation Account para ejecutar el bloqueo y retiro automatizado.", style_cell)
    ]
]
t_callout = Table(callout_data, colWidths=[720])
t_callout.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFF5F5')),
    ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#E53E3E')),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 12),
    ('RIGHTPADDING', (0,0), (-1,-1), 12),
]))
story.append(t_callout)

doc.build(story)
print(f"PDF generado exitosamente en: {pdf_path}")
