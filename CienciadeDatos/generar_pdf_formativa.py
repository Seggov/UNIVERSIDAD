import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont('Helvetica', 8.5)
        self.setFillColor(colors.HexColor('#4A5568'))
        
        # Header (Pages 2+)
        if self._pageNumber > 1:
            self.drawString(54, letter[1] - 36, 'Ciencia de Datos - Resumen Teórico y Glosario (Prueba Formativa 1)')
            self.setStrokeColor(colors.HexColor('#CBD5E0'))
            self.setLineWidth(0.5)
            self.line(54, letter[1] - 42, letter[0] - 54, letter[1] - 42)
        
        # Footer
        text = f'Página {self._pageNumber} de {page_count}'
        self.drawRightString(letter[0] - 54, 34, text)
        self.drawString(54, 34, 'Eje Teórico y Conceptual - Preparación para Evaluación')
        self.setStrokeColor(colors.HexColor('#CBD5E0'))
        self.setLineWidth(0.5)
        self.line(54, 46, letter[0] - 54, 46)
        self.restoreState()

pdf_filename = 'c:/Users/PC/Desktop/CienciadeDatos/Resumen_Teorico_Formativa_Ciencia_de_Datos.pdf'
doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=letter,
    leftMargin=48,
    rightMargin=48,
    topMargin=46,
    bottomMargin=46
)

styles = getSampleStyleSheet()

c_primary = colors.HexColor('#0F2942')    # Deep Navy
c_secondary = colors.HexColor('#1E56A0')  # Classic Blue
c_accent = colors.HexColor('#008080')     # Teal
c_bg_box = colors.HexColor('#F4F6F9')     # Clean light grey/blue
c_text = colors.HexColor('#2D3748')       # Charcoal

title_style = ParagraphStyle(
    'TitleStyle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=18,
    leading=22,
    textColor=c_primary,
    alignment=1,
    spaceAfter=3
)

subtitle_style = ParagraphStyle(
    'SubTitleStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=13,
    textColor=c_secondary,
    alignment=1,
    spaceAfter=10
)

h1_style = ParagraphStyle(
    'H1Style',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=11.5,
    leading=15,
    textColor=c_primary,
    spaceBefore=9,
    spaceAfter=3
)

h2_style = ParagraphStyle(
    'H2Style',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=9,
    leading=12,
    textColor=c_secondary,
    spaceBefore=4,
    spaceAfter=2
)

body_style = ParagraphStyle(
    'BodyStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=11.5,
    textColor=c_text,
    spaceAfter=2.5
)

term_title_style = ParagraphStyle(
    'TermTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=8.5,
    leading=11,
    textColor=c_primary
)

term_desc_style = ParagraphStyle(
    'TermDesc',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8,
    leading=10.5,
    textColor=c_text
)

story = []

# Title Banner
story.append(Paragraph('CIENCIA DE DATOS - EVALUACIÓN FORMATIVA 1', subtitle_style))
story.append(Paragraph('Síntesis Teórica y Glosario Conceptual', title_style))
story.append(Paragraph('Compendio de Fundamentos Teóricos de los Enunciados Evaluados', subtitle_style))
story.append(HRFlowable(width='100%', thickness=1.5, color=c_secondary, spaceAfter=8))

# Framing Box
box_text = (
    '<b>Enfoque metodológico:</b> Este documento sistematiza exclusivamente los fundamentos '
    '<b>teóricos, taxonómicos y analíticos</b> de los 21 enunciados de la prueba formativa. '
    'Se excluye el cálculo numérico sobre planillas para consolidar con nitidez conceptual '
    'la metodología CRISP-DM, arquitectura de APIs web, expresiones regulares, imputación de nulos, '
    'transformaciones de variables, NLP, taxonomía de problemas y optimización lineal.'
)
box_table = Table([[Paragraph(box_text, body_style)]], colWidths=[504])
box_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), c_bg_box),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E0')),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
]))
story.append(box_table)
story.append(Spacer(1, 8))

# SECTION 1: METHODOLOGY & TAXONOMY
story.append(Paragraph('Módulo 1: Metodología CRISP-DM y Taxonomía de Problemas', h1_style))
story.append(Paragraph('Enunciados de referencia: Preguntas 4, 7, 16 y 17', h2_style))
story.append(Paragraph(
    '• <b>Fase de Modelado (Modeling) en CRISP-DM:</b> Es la etapa donde se seleccionan y calibran algoritmos matemáticos. El desarrollo de una regresión lineal pertenece inequívocamente a <b>Modelado</b> (Pregunta 7).<br/>'
    '• <b>Comprensión del Negocio (Business Understanding):</b> Fase inicial donde se definen objetivos estratégicos del cliente y se traducen en un problema analítico formal.<br/>'
    '• <b>Comprensión de los Datos (Data Understanding):</b> Exploración preliminar, diagnóstico de calidad e hipótesis iniciales.<br/>'
    '• <b>Preparación de Datos (Data Preparation):</b> Limpieza, filtrado, transformación e imputación del conjunto analítico.<br/>'
    '• <b>Taxonomía de Machine Learning (Supervisado vs. No Supervisado):</b> Si disponemos de un dataset histórico con una variable objetivo etiquetada (ej. producto \"exitoso\" vs. \"no exitoso\"), el problema es de <b>Aprendizaje Supervisado</b>. Al tener dos clases cualitativas, corresponde a una <b>Clasificación Binaria</b> (Preguntas 16 y 17).',
    body_style
))
story.append(Spacer(1, 4))

# SECTION 2: WEB, APIS & FORMATS
story.append(Paragraph('Módulo 2: Formatos de Datos y Arquitectura de APIs Web', h1_style))
story.append(Paragraph('Enunciados de referencia: Preguntas 4, 8 y 9', h2_style))
story.append(Paragraph(
    '• <b>Formato basado en Clave y Valor (JSON):</b> Estructura de texto semiestructurada organizada en pares clave-valor y arreglos. Difiere de CSV (tabular plano) y XML (etiquetas jerárquicas) (Pregunta 8).<br/>'
    '• <b>Arquitectura REST Stateless (Sin Estado):</b> El servidor <b>no recuerda</b> transacciones previas del cliente. Cada petición HTTP debe ser autosuficiente e incluir credenciales (Pregunta 9).<br/>'
    '• <b>Método HTTP GET:</b> Verbo estándar para solicitar y recuperar datos desde el servidor sin modificar su estado.<br/>'
    '• <b>Autenticación por Token:</b> Envío de un token seguro en cada solicitud (header Authorization) para validar acceso.',
    body_style
))
story.append(Spacer(1, 4))

# SECTION 3: REGEX PATTERNS
story.append(Paragraph('Módulo 3: Expresiones Regulares (Regex) y Reconocimiento de Patrones', h1_style))
story.append(Paragraph('Enunciados de referencia: Preguntas 4 y 5', h2_style))
story.append(Paragraph(
    'Patrones canónicos evaluados:<br/>'
    '• <b>\\+\\d{2}-\\d-\\d{8}:</b> Teléfono con prefijo internacional (ej. +56-9-12345678).<br/>'
    '• <b>[A-Z]{2}-\\d{4}-[A-Z]{2}:</b> Placa patente o código alfanumérico segmentado (ej. CL-1234-AB).<br/>'
    '• <b>-?\\d+:</b> Número entero con signo negativo opcional (ej. -25).<br/>'
    '• <b>\\d{4}-\\d{2}-\\d{2}:</b> Fecha estándar ISO año-mes-día (ej. 2026-04-23).<br/>'
    '• <b>\\d{7,8}-[\\dkK]:</b> Identificador nacional tipo RUT chileno con dígito verificador (ej. 12345678-9).<br/>'
    '• <b>[A-Z][a-z]+:</b> Palabra que inicia con mayúscula seguida de minúsculas (ej. Hola).<br/>'
    '• <b>[a-f0-9]{8}-[a-f0-9]{8}:</b> Cadena hexadecimal segmentada tipo identificador/hash (ej. a3f9c2d1-9b7e4a2c).<br/>'
    '• <b>[\\w.-]+@[\\w.-]+\\.\\w+:</b> Dirección de correo electrónico válida (ej. correo123@gmail.com).<br/>'
    '• <b>-?\\d+\\.\\d+:</b> Número decimal con punto flotante (ej. 3.1416).',
    body_style
))

story.append(PageBreak())

# SECTION 4: DATA CLEANING & PREPROCESSING
story.append(Paragraph('Módulo 4: Limpieza, Imputación y Transformación de Variables', h1_style))
story.append(Paragraph('Enunciados de referencia: Preguntas 2, 11 y 14', h2_style))
story.append(Paragraph(
    '• <b>Tratamiento de Datos Faltantes (Pregunta 2):</b> Las 3 vías estructuradas son: <i>Omitir</i> (eliminar registros), <i>Reemplazo por Media</i> (imputación estadística simple), y técnicas de estructuración como <i>Normalización</i> o <i>Clustering</i>.<br/>'
    '• <b>Imputación BFILL (Backward Fill):</b> Técnica que rellena un valor nulo copiando el valor válido inmediatamente posterior en la secuencia ordenada (Pregunta 11). Se contrapone a FFILL (Forward Fill).<br/>'
    '• <b>Reducción de Sesgo Positivo con log(X):</b> Cuando una variable (ej. ingresos) está sesgada hacia la derecha por valores extremos grandes, la función matemática más adecuada para compactar la distribución, mitigar extremos y simetrizarla es <b>log(X)</b> (Pregunta 14).',
    body_style
))
story.append(Spacer(1, 4))

# SECTION 5: EDA & DATA VISUALIZATION
story.append(Paragraph('Módulo 5: Estadística Descriptiva y Buenas Prácticas de Visualización', h1_style))
story.append(Paragraph('Enunciados de referencia: Preguntas 6, 10, 12, 20 y 21', h2_style))
story.append(Paragraph(
    '• <b>Rango Intercuartílico (IQR):</b> Diferencia estadística IQR = Q3 - Q1. Cuantifica la dispersión del 50% central y es una medida <b>robusta</b> frente a outliers (Pregunta 6).<br/>'
    '• <b>Selección de Gráficos (Horas vs. Nota vs. Carrera):</b> Para estudiar la relación entre dos variables numéricas continuas y una categórica, la combinación más adecuada es un <b>Scatter plot con color por categoría</b> (Pregunta 10).<br/>'
    '• <b>Buenas Prácticas de Color:</b> Se debe utilizar una <b>paleta de colores coherente y significativa</b>, evitando colores aleatorios o saturados en exceso (Pregunta 12).',
    body_style
))
story.append(Spacer(1, 4))

# SECTION 6: NLP FUNDAMENTALS
story.append(Paragraph('Módulo 6: Procesamiento de Lenguaje Natural (PLN)', h1_style))
story.append(Paragraph('Enunciados de referencia: Preguntas 3 y 15', h2_style))
story.append(Paragraph(
    '• <b>Token:</b> Unidad mínima en la que se segmenta un texto (palabras o símbolos).<br/>'
    '• <b>Corpus:</b> Conjunto completo de documentos utilizados para el análisis.<br/>'
    '• <b>Stopwords:</b> Palabras comunes sin significado discriminante relevante (artículos, preposiciones).<br/>'
    '• <b>Bag of Words (BoW):</b> Representación de un texto basada en la frecuencia de sus palabras sin considerar su orden sintáctico.<br/>'
    '• <b>TF (Term Frequency):</b> Cantidad de veces que aparece una palabra en un documento específico.<br/>'
    '• <b>IDF (Inverse Document Frequency):</b> Medida que penaliza palabras ubicuas en el corpus, asignando mayor peso a los términos distintivos (Preguntas 3 y 15).',
    body_style
))
story.append(Spacer(1, 4))

# SECTION 7: LINEAR MODELS, REGULARIZATION & GRADIENT DESCENT
story.append(Paragraph('Módulo 7: Regresión Lineal, Regularización Lasso y Descenso de Gradiente', h1_style))
story.append(Paragraph('Enunciados de referencia: Preguntas 1, 13, 18 y 19', h2_style))
story.append(Paragraph(
    '• <b>Modelo de Regresión Lineal Múltiple:</b> Ecuación y^ = w0 + w1*x + w2*z. El intercepto w0 es el valor esperado cuando las entradas son nulas; los pesos w1 y w2 reflejan el aporte marginal de cada característica (Pregunta 13).<br/>'
    '• <b>Regularización Lasso (L1):</b> Incorpora la suma de los valores absolutos de los coeficientes a la función de pérdida (Costo = RSS + lambda * sum(|w_i|)). Induce coeficientes nulos, actuando como selector de variables (Pregunta 1).<br/>'
    '• <b>Descenso de Gradiente y Actualización de Pesos:</b> Para una función de costo cuadrática J = 1/2*(y^ - y)^2, la derivada parcial respecto al peso w4 asociado al término cuadrático x1^2 es dJ/dw4 = (y^ - y) * x1^2. La regla formal de actualización es: <b>w4 := w4 - alpha * (y^ - y) * x1^2</b> (Preguntas 18 y 19).',
    body_style
))

story.append(PageBreak())

# SECTION 8: GLOSARIO EXCLUSIVO DE LA FORMATIVA
story.append(Paragraph('Glosario Conceptual de la Prueba Formativa', h1_style))
story.append(Paragraph('Términos y definiciones canónicas evaluadas directamente en el cuestionario.', body_style))
story.append(Spacer(1, 6))

terms_glossary = [
    ('API REST', 'Arquitectura de servicios web basada en HTTP, sin estado (stateless) y con recursos direccionables por URI.'),
    ('Aprendizaje Supervisado', 'Paradigma donde el modelo aprende a partir de datos históricos con etiquetas o salidas objetivo conocidas.'),
    ('Autenticación por Token', 'Mecanismo de seguridad que envía una clave o token en el header de cada petición para validar acceso.'),
    ('Bag of Words (BoW)', 'Representación vectorial de un documento según la frecuencia de sus palabras sin considerar el orden gramatical.'),
    ('BFILL (Backward Fill)', 'Método de imputación secuencial que propaga hacia atrás el valor válido inmediatamente posterior.'),
    ('Business Understanding', 'Fase inicial de CRISP-DM donde se formulan los objetivos de negocio y se define el problema de minería de datos.'),
    ('Clasificación Binaria', 'Problema supervisado donde la variable de salida consta exactamente de dos clases cualitativas discretas.'),
    ('Corpus', 'Conjunto estructurado de documentos textuales utilizado para entrenamiento y procesamiento de texto.'),
    ('CRISP-DM', 'Metodología estándar de 6 fases iterativas para estructurar proyectos integrales de ciencia de datos.'),
    ('CSV', 'Formato plano de almacenamiento tabular delimitado por comas, con o sin fila de cabecera.'),
    ('Data Preparation', 'Fase de CRISP-DM dedicada a la limpieza, transformación, imputación y codificación del conjunto de datos.'),
    ('Data Understanding', 'Fase de CRISP-DM enfocada en la recolección inicial, exploración y detección de problemas de calidad en los datos.'),
    ('Descenso de Gradiente', 'Algoritmo de optimización que ajusta parámetros iterativamente en sentido opuesto al gradiente de la función de costo.'),
    ('Expresión Regular (Regex)', 'Patrón formal de búsqueda y validación utilizado para identificar secuencias específicas de texto.'),
    ('HTTP GET', 'Método HTTP para solicitar y consultar recursos del servidor sin alterar su estado.'),
    ('IDF', 'Frecuencia Inversa de Documento; penaliza palabras muy repetidas en el corpus para resaltar términos relevantes.'),
    ('JSON', 'Formato de intercambio de datos basado en pares clave-valor (diccionarios) y listas ordenadas.'),
    ('Lasso (L1)', 'Técnica de regularización que suma penalización por valor absoluto de los coeficientes, forzando variables a cero.'),
    ('Modelado (Modeling)', 'Fase de CRISP-DM donde se entrenan, calibran y ajustan algoritmos matemáticos como regresiones.'),
    ('One-Hot Encoding', 'Codificación binaria que crea columnas indicadoras (0 o 1) para cada categoría nominal evitando inducir orden.'),
    ('Rango Intercuartílico (IQR)', 'Medida de dispersión robusta calculada como Q3 - Q1, representativa del 50% central de los datos.'),
    ('Stateless (Sin Estado)', 'Propiedad de las APIs donde el servidor no recuerda peticiones previas; cada solicitud es autosuficiente.'),
    ('Stopwords', 'Palabras gramaticales comunes (artículos, preposiciones) que se descartan por no aportar valor semántico.'),
    ('TF', 'Frecuencia de Término; número de apariciones de una palabra dentro de un documento particular.'),
    ('TF-IDF', 'Ponderación estadística calculada como TF multiplicado por IDF para determinar la importancia relativa de una palabra.'),
    ('Token', 'Unidad mínima en la que se divide un texto (palabras o símbolos) para su procesamiento computacional.'),
    ('Transformación log(X)', 'Función matemática para comprimir la cola de valores altos en variables sesgadas a la derecha y simetrizarlas.')
]

t_data = [[Paragraph('<b>Término / Concepto</b>', term_title_style), Paragraph('<b>Definición Conceptual y Fundamento Teórico</b>', term_title_style)]]
for term, desc in terms_glossary:
    t_data.append([Paragraph(term, term_title_style), Paragraph(desc, term_desc_style)])

glossary_table = Table(t_data, colWidths=[120, 384])
glossary_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#E2E8F0')),
    ('LINEBELOW', (0,0), (-1,0), 1.5, c_secondary),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E0')),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(glossary_table)

doc.build(story, canvasmaker=NumberedCanvas)
print('PDF generated successfully at:', pdf_filename)
