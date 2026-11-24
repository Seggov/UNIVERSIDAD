window.PORTAL_BLOCKS.push(
  /* ================= SÁBADO 28 (1 BLOQUE TARDE) ================= */
  {
    id: 'sab28_b1',
    dayId: 'sab28',
    num: 1,
    time: '15:00–16:00 (60 min · Post-Prueba Ciber y descanso)',
    course: 'cd',
    courseLabel: 'Ciencia de Datos #7',
    title: 'Clase 09 — Redes Neuronales, Perceptrón, Feedforward y Backpropagation',
    ra: 'RA3 · RA4 · RA5',
    goal: 'Entender el límite lineal del Perceptrón, el rol de la activación no lineal y ejecutar a mano un paso de Feedforward + Backpropagation.',
    widgetId: 'cd_redes',
    simpleHtml: `
      <div class="grid-3">
        <div class="v-card"><h4>1. Perceptrón y Época (Epoch)</h4><ul>
          <li>Suma ponderada <code>z = ∑ w_i x_i + b</code> + función escalón.</li>
          <li><strong>Época (Epoch, Diap. 19):</strong> una pasada completa de <strong>todos</strong> los ejemplos de entrenamiento por la red.</li>
          <li><strong>Problema fatal:</strong> solo traza 1 frontera lineal → incapaz de resolver problemas no linealmente separables (ej. XOR).</li>
        </ul></div>
        <div class="v-card"><h4>2. Capa Oculta y No Linealidad</h4><ul>
          <li>Apilar capas sin función de activación no lineal equivale a una sola recta (combinación lineal de lineales sigue siendo lineal!).</li>
          <li>Al meter <code>f(Σ)</code> no lineal (sigmoide, tanh, ReLU), una red con <strong>1 sola capa oculta</strong> y suficientes neuronas puede aproximar cualquier función continua (Teorema de Aproximación Universal, Diap. 36).</li>
        </ul></div>
        <div class="v-card"><h4>3. Feedforward + Backprop</h4><ul>
          <li><strong>Feedforward:</strong> empuja entradas <code>x</code> hacia adelante hasta obtener <code>ŷ</code> y medir el error <code>E</code>.</li>
          <li><strong>Backpropagation:</strong> aplica la <strong>regla de la cadena</strong> desde la salida hacia atrás para saber cuánto culpar a cada peso <code>w</code> y actualizarlo: <code>w_nuevo = w_viejo − α · (∂E/∂w)</code>.</li>
        </ul></div>
      </div>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">Dibuja la red chiquita de Clase 09: 2 círculos de entrada (<code>x₁, x₂</code>) → 2 círculos ocultos (<code>h₁, h₂</code> con pesos <code>w₁..w₄</code>) → 1 círculo salida (<code>ŷ</code> con pesos <code>w₅, w₆</code>). Pinta una flecha verde arriba hacia la derecha (<strong>1. Feedforward: calcula ŷ y error</strong>) y una flecha roja abajo hacia la izquierda (<strong>2. Backprop: ajusta primero w₅,w₆ y luego w₁..w₄</strong>).</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Ejercicios Reales de Clase 09 (Diapositivas 44 y 51–61)</h4>
        <ol style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li>Queremos predecir la nota final de un alumno usando <code>x₁ = horas estudiadas</code> y <code>x₂ = promedio parcial</code>. Si la red arroja <code>ŷ = 5.2</code> y la nota real fue <code>y = 6.0</code>, ¿cuál es el error simple <code>(y − ŷ)</code> y el error cuadrático medio <code>½(y − ŷ)²</code>?</li>
          <li>Si el gradiente respecto al peso <code>w₆</code> dio <code>∂E/∂w₆ = −0.40</code>, el peso actual es <code>w₆ = 0.50</code> y la tasa de aprendizaje es <code>α = 0.1</code>, ¿cuánto vale el nuevo <code>w₆</code>?</li>
        </ol>
        <details class="sol-toggle"><summary>Ver solución paso a paso</summary>
          1) Error simple = <code>6.0 − 5.2 = 0.8</code>; error cuadrático = <code>0.5 × (0.8)² = 0.32</code>.<br/>
          2) <code>w₆_nuevo = w₆_actual − α · (∂E/∂w₆) = 0.50 − 0.1 × (−0.40) = 0.50 + 0.04 = 0.54</code> (¡cuidado con el doble signo menos!).
        </details>
      </div>
    `,
    files: [
      'CienciadeDatos/Clase 09 - Redes Neuronales.pdf (65 diapositivas)'
    ]
  },

  /* ================= DOMINGO 29 (4 BLOQUES DE CIERRE TOTAL) ================= */
  {
    id: 'dom29_b1',
    dayId: 'dom29',
    num: 1,
    time: '09:30–10:30 (60 min)',
    course: 'cd',
    courseLabel: 'Ciencia de Datos #8',
    title: 'Práctica de Casos Completos: NLP 150 Docs, Ayudantía 5 (auto_mpg) y Taller 2 (H&M)',
    ra: 'RA2 · RA3 · RA4 · RA5 · RA6',
    goal: 'Resolver casos abiertos de principio a fin como pide un profesor estricto: desde preparar datos sin leakage hasta interpretar coeficientes y comunicar.',
    widgetId: null,
    simpleHtml: `
      <div class="grid-3">
        <div class="v-card"><h4>Caso 1 · 150 Documentos (enunciadoClase.txt)</h4><ul>
          <li>50 Política, 50 Deporte, 50 Internacional (balanceado!).</li>
          <li><strong>Flujo ganador:</strong> 1) Limpiar texto (minúsculas, puntuación, cuidado con stopwords si usas n-gramas), 2) Vectorizar con <strong>Bag of Words / TF-IDF</strong>, 3) Dividir con <strong>Holdout estratificado o k-Fold CV</strong> (ajustando vocabulario SOLO en Train!), 4) Entrenar clasificador multiclase (Regresión Logística / SVM / Random Forest), 5) Evaluar con <strong>Matriz de Confusión 3×3 + Precision/Recall/F1 macro</strong>.</li>
        </ul></div>
        <div class="v-card"><h4>Caso 2 · Ayudantía 5 (auto_mpg, 5 Modelos)</h4><ul>
          <li>Predecir rendimiento <code>mpg</code> (continua → Regresión Lineal).</li>
          <li><strong>Pregunta clave pág. 7:</strong> ¿por qué cambia el peso de <code>horsepower</code> al meter <code>weight_k</code> juntos en M3? ¡Por <strong>multicolinealidad</strong> (autos más pesados suelen tener más HP)! Ahora cada peso mide el efecto dejando fija la otra variable.</li>
          <li>Para comparar M1 (1 var) vs M4/M5 (más vars), usa <strong><code>R² ajustado</code></strong> y ECM en Test.</li>
        </ul></div>
        <div class="v-card"><h4>Caso 3 · Taller 2 H&amp;M (Demanda Estacional)</h4><ul>
          <li>Umbral P75 calculado <strong>exclusivo en Train</strong> (Año 1) para evitar <em>data leakage</em> temporal.</li>
          <li>Categorías base omitidas en One-Hot (<code>enero</code>, <code>Lunes</code>, <code>inicio_mes</code>) para evitar colinealidad perfecta (trampa de variables dummy).</li>
          <li>Modelo 4 logra mejor <code>AUC-ROC = 0.724</code> y <code>F1 = 0.414</code>.</li>
        </ul></div>
      </div>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">Dibuja la tubería universal anti-errores para cualquier pregunta de caso abierto: <code>Datos Crudos → Split Train/Test PRIMERO → Limpiar/Escalar/Vectorizar (fit en Train, transform en Test) → Entrenar + CV → Evaluar en Test → Interpretar en lenguaje del dominio</code>.</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Redacta en tu Cuaderno (Práctica de Comunicación RA5–RA6)</h4>
        <p style="margin:0;font-size:0.86rem;">En el modelo de <code>auto_mpg</code>, supón que <code>origen_Japon</code> (con referencia EE.UU.) tiene coeficiente <code>w = +2.8</code> manteniendo fijos peso, potencia y año. Escribe en 2 líneas exactas qué significa ese <code>+2.8</code> para la agencia automotriz.</p>
        <details class="sol-toggle"><summary>Ver redacción modelo de 7.0</summary>
          "A igual peso, potencia y año del vehículo, un automóvil de origen japonés rinde en promedio <strong>2,8 millas por galón más</strong> que un automóvil equivalente de origen estadounidense (categoría de referencia)."
        </details>
      </div>
    `,
    files: [
      'CienciadeDatos/enunciadoClase.txt',
      'CienciadeDatos/05 - Ayudantía-20261123T031057Z-1-001.zip → 05 - Ayudantía/Ayudantía 5.pdf',
      'CienciadeDatos/Taller 2/Ciencia-de-Datos-2/entrega_final/Informe_Laboratorio_2_HM.pdf'
    ]
  },

  {
    id: 'dom29_b2',
    dayId: 'dom29',
    num: 2,
    time: '11:00–12:00 (60 min)',
    course: 'cd',
    courseLabel: 'Ciencia de Datos #9',
    title: 'Repaso Integrador de Teoría Completa (Mapa Maestro Clases 01 a 09)',
    ra: 'RA1 · RA2 · RA3 · RA4 · RA5 · RA6',
    goal: 'Construir en 1 hoja tu Tabla Maestra comparativa de los 8 modelos del curso (tarea, pérdida, hiperparámetros, fortalezas y trampas).',
    widgetId: null,
    simpleHtml: `
      <p><strong>Aquí tienes la radiografía completa del semestre en una sola tabla para pasar en limpio a tu hoja estrella:</strong></p>
      <table class="clean-tbl">
        <tr><th>Modelo</th><th>Tarea</th><th>Qué optimiza / Criterio</th><th>Hiperparámetros clave</th><th>Cuándo brilla / Cuándo sufre</th></tr>
        <tr><td><strong>Reg. Lineal (OLS)</strong></td><td>Regresión</td><td>Minimiza ECM (MSE)</td><td>Ninguno (o <code>α</code> si usa GD)</td><td>Muy interpretable; sufre con outliers y no linealidad.</td></tr>
        <tr><td><strong>Ridge (L2)</strong></td><td>Regresión</td><td>ECM + <code>λ ∑ w²</code></td><td><code>λ</code> (penalización)</td><td>Ideal con <strong>multicolinealidad</strong>; NO anula variables.</td></tr>
        <tr><td><strong>Lasso (L1)</strong></td><td>Regresión</td><td>ECM + <code>λ ∑ |w|</code></td><td><code>λ</code> (penalización)</td><td>Hace <code>w = 0</code> → <strong>selección automática</strong> de variables.</td></tr>
        <tr><td><strong>Reg. Logística</strong></td><td>Clasificación</td><td>Entropía cruzada / Sigmoide</td><td>Umbral, regularización</td><td>Entrega probabilidades calibradas y Odds Ratios.</td></tr>
        <tr><td><strong>SVM</strong></td><td>Clasificación</td><td>Máximo margen entre clases</td><td><code>C</code>, <code>γ</code>, tipo de <strong>Kernel</strong></td><td>Potente en alta dimensión y no lineal (con Kernel).</td></tr>
        <tr><td><strong>Árbol Decisión</strong></td><td>Clasif. / Reg.</td><td>Ganancia Info (Entropía) o <strong>Gini</strong></td><td>Profundidad máx, <code>α</code> (Poda)</td><td>Caja blanca interpretable; sin poda sufre grave overfitting.</td></tr>
        <tr><td><strong>Random Forest</strong></td><td>Clasif. / Reg.</td><td>Ensamble de árboles (votación)</td><td>N° árboles, vars por corte</td><td>Reduce varianza y resiste overfitting; menos interpretable.</td></tr>
        <tr><td><strong>Red Neuronal (MLP)</strong></td><td>Clasif. / Reg.</td><td>Error vía <strong>Backpropagation</strong></td><td>Capas, neuronas, <code>α</code>, épocas</td><td>Captura patrones no lineales complejos; requiere muchos datos.</td></tr>
      </table>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">Copia esta tabla resumida con tus colores en una hoja limpia y añade abajo las 5 fórmulas relámpago: <code>Gini = 1 − ∑p²</code> · <code>Precision = TP/(TP+FP)</code> · <code>Recall = TP/(TP+FN)</code> · <code>F1 = 2PR/(P+R)</code> · <code>W_nuevo = W − α∇F</code>.</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Autotest Rápido de Discriminación de Modelos</h4>
        <p style="margin:0;font-size:0.86rem;">Di al instante qué modelo eliges si: (a) el gerente exige reglas explícitas fáciles de auditar, (b) tienes 100 predictores muy correlacionados entre sí y todos aportan un poco, (c) tienes dos clases con frontera circular en 2D, (d) necesitas probabilidades e impacto multiplicativo (Odds Ratio) de cada mes.</p>
        <details class="sol-toggle"><summary>Ver respuestas</summary>
          (a) Árbol de decisión podado · (b) Regresión Ridge (L2) · (c) SVM con Kernel RBF/polinomial (o MLP con capa oculta) · (d) Regresión Logística.
        </details>
      </div>
    `,
    files: [
      'Todas las clases: clase01_text.txt, clase02_text.txt, CLASE 04.pdf y Clases 05 a 09'
    ]
  },

  {
    id: 'dom29_b3',
    dayId: 'dom29',
    num: 3,
    time: '14:30–15:30 (60 min · Cronómetro real)',
    course: 'cd',
    courseLabel: 'Ciencia de Datos #10',
    title: 'Simulacro Cronometrado de Prueba 2 (60 min Sin Apuntes)',
    ra: 'RA1–RA6 (Condiciones reales de examen)',
    goal: 'Resolver un examen completo exigente en 60 minutos exactos (Teoría crítica + Cálculos a mano + Caso aplicado) sin abrir ningún PDF.',
    widgetId: null,
    simpleHtml: `
      <p><strong>Pon el temporizador de arriba en 60:00, guarda el celular y tus apuntes, y responde en papel este certamen simulado completo:</strong></p>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">Administra el reloj como en el certamen real: <strong>18 min Parte A</strong> · <strong>24 min Parte B (cálculos)</strong> · <strong>18 min Parte C (diseño y comunicación)</strong>.</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Examen Simulado Completo (100 pts)</h4>
        <p style="font-size:0.85rem;margin:0 0 0.5rem;"><strong>Parte A — Conceptos Críticos (30 pts):</strong></p>
        <ol style="margin:0 0 0.6rem;padding-left:1.2rem;font-size:0.85rem;">
          <li>Explica por qué eliminar <em>stopwords</em> antes de generar trigramas altera el análisis lingüístico y por qué <code>log(X)</code> corrige asimetría positiva.</li>
          <li>Compara alto sesgo vs. alta varianza e indica cómo cambian al podar un árbol con parámetro <code>α</code> o al pasar a Random Forest.</li>
          <li>¿Por qué en fraude bancario (0,5% positivos) un Accuracy de 99,5% es engañoso y conviene usar curva Precision-Recall en vez de solo Accuracy?</li>
        </ol>
        <p style="font-size:0.85rem;margin:0 0 0.5rem;"><strong>Parte B — Cálculos a Mano (40 pts):</strong></p>
        <ol start="4" style="margin:0 0 0.6rem;padding-left:1.2rem;font-size:0.85rem;">
          <li>Matriz de confusión: <code>TP = 40, FP = 10, FN = 20, TN = 130</code>. Calcula <strong>Accuracy, Precision, Recall y F1-Score</strong>.</li>
          <li>Un nodo padre con 10 muestras <code>(5 Sí, 5 No)</code> se divide por el atributo "Clima" en Hijo Izq <code>(4 Sí, 1 No)</code> e Hijo Der <code>(1 Sí, 4 No)</code>. Calcula el <strong>Gini del padre</strong>, el <strong>Gini de cada hijo</strong> y el <strong>Gini ponderado del corte</strong>.</li>
          <li>En una neurona de salida lineal <code>ŷ = w·h</code> con <code>h = 2</code>, peso inicial <code>w = 1.5</code>, valor real <code>y = 5</code>, error <code>E = ½(y − ŷ)²</code> y tasa <code>α = 0.1</code>, calcula <code>ŷ</code>, el gradiente <code>∂E/∂w = −(y − ŷ)·h</code> y el <strong>nuevo peso <code>w</code></strong>.</li>
        </ol>
        <p style="font-size:0.85rem;margin:0 0 0.5rem;"><strong>Parte C — Diseño y Comunicación CRISP-DM (30 pts):</strong></p>
        <ol start="7" style="margin:0;padding-left:1.2rem;font-size:0.85rem;">
          <li>Una clínica quiere predecir si un paciente faltará a su hora médica (<em>no-show</em>) usando historial, edad, distancia, especialidad y día de la semana (20% falta, 80% asiste). Diseña el flujo completo sin <em>data leakage</em>, justifica 2 modelos candidatos, elige la métrica principal y explica cómo presentarías los hallazgos al director médico (qué gráficos de Clase 04 usarías).</li>
        </ol>
        <details class="sol-toggle"><summary>Abrir Pauta de Corrección (SOLO en el Bloque 4 a las 16:00!)</summary>
          • <strong>P4 (Matriz):</strong> Total = 200. <code>Accuracy = 170/200 = 85%</code> · <code>Precision = 40/50 = 80%</code> · <code>Recall = 40/60 = 66,7%</code> · <code>F1 = 2×0,8×0,667 / (1,467) = 0,727</code>.<br/>
          • <strong>P5 (Gini):</strong> Padre = <code>1 − (0,5²+0,5²) = 0,50</code>. Hijo Izq (80%/20%) = <code>1 − (0,64+0,04) = 0,32</code>. Hijo Der (20%/80%) = <code>0,32</code>. Gini ponderado = <code>(5/10)×0,32 + (5/10)×0,32 = 0,32</code> (bajó la impureza de 0,50 a 0,32!).<br/>
          • <strong>P6 (Gradiente/Backprop):</strong> <code>ŷ = 1,5 × 2 = 3</code>. Error <code>y − ŷ = 2</code>. Gradiente <code>∂E/∂w = −2 × 2 = −4</code>. Nuevo peso: <code>w_nuevo = 1,5 − 0,1 × (−4) = 1,9</code> (con <code>w=1,9</code> la nueva predicción sube a <code>3,8</code>, acercándose a <code>5</code>!).<br/>
          • <strong>P7 (Clínica):</strong> Partición temporal o estratificada antes de imputar/codificar; One-Hot con categoría base omitida; comparar Regresión Logística (Odds Ratios interpretables para médicos) vs Random Forest; optimizar Recall/F1 y curva PR por desbalance 20/80; comunicar con barras de tasa de inasistencia por especialidad y boxplot/scatter de distancia/edad.
        </details>
      </div>
    `,
    files: [
      'Hoja en blanco + lápiz + cronómetro de 60 minutos'
    ]
  },

  {
    id: 'dom29_b4',
    dayId: 'dom29',
    num: 4,
    time: '16:00–17:00 (60 min · Cierre Definitivo)',
    course: 'cd',
    courseLabel: 'Ciencia de Datos #11 (Cierre)',
    title: 'Corrección del Simulacro, Refuerzo de Errores y Cierre Final',
    ra: 'RA1–RA6 (Listo para mañana 11:40)',
    goal: 'Corregir con lupa tu simulacro, rehacer cualquier cálculo dudoso y cerrar el estudio a las 17:00 (mañana lunes en la mañana NO hay bloques).',
    widgetId: null,
    simpleHtml: `
      <p><strong>Última hora de estudio de toda la semana:</strong> como mañana lunes 30 tienes la mañana sin bloques antes de las <strong>11:40</strong>, hoy a las 17:00 queda todo cerrado.</p>
      <div class="grid-2">
        <div class="v-card"><h4>Checklist de Precisión Conceptual</h4><ul>
          <li>¿Distingo parámetro aprendido (<code>w, b</code>) de hiperparámetro (<code>α, λ, C, γ, k</code>)?</li>
          <li>¿Recuerdo que <strong>Lasso (L1)</strong> selecciona variables (<code>w=0</code>) y <strong>Ridge (L2)</strong> solo encoge?</li>
          <li>¿Recuerdo que <strong><code>R² ajustado</code></strong> penaliza predictores basura y que <strong>CV no entrena el modelo final</strong>?</li>
          <li>¿Sé explicar <em>Data Leakage</em> y por qué todo preprocesamiento se ajusta solo en <code>Train</code>?</li>
        </ul></div>
        <div class="v-card"><h4>Checklist de Cálculos sin Calculadora</h4><ul>
          <li>Gini <code>1 − ∑p_i²</code> (100/0 → <code>0</code>; 70/30 → <code>0.42</code>; 50/50 → <code>0.50</code>).</li>
          <li>Precision, Recall y <code>F1 = 2·P·R / (P+R)</code>.</li>
          <li>Actualización con signo correcto: <code>w_nuevo = w − α · gradiente</code>.</li>
        </ul></div>
      </div>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">Escribe en media carilla tus <strong>"3 cuidados personales"</strong> según lo que te costó en el simulacro de recién, léela una vez con calma, cierra el cuaderno a las 17:00 y descansa bien para romperla mañana a las 11:40.</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>¡Semana Completada!</h4>
        <p style="margin:0;font-size:0.86rem;">Marca este bloque como completado arriba a la derecha para llegar al <strong>100% (25 / 25 bloques)</strong>. Si cualquier concepto o ejercicio te genera duda mientras estudias, pregúntame directo en el chat y lo destrabamos al instante.</p>
      </div>
    `,
    files: [
      'Tu Hoja Maestra del Bloque #9 + Pauta del Simulacro Bloque #10',
      'CienciadeDatos/Glosario_Ciencia_de_Datos_Clases_1_y_2.pdf'
    ]
  }
);
