window.PORTAL_BLOCKS.push(
  /* ================= MIÉRCOLES 25 (3 BLOQUES TARDE) ================= */
  {
    id: 'mie25_b1',
    dayId: 'mie25',
    num: 1,
    time: '14:30–15:30 (60 min · Post-Prueba Arqui)',
    course: 'edd',
    courseLabel: 'Estructura C++ #4',
    title: 'Clase 07.1 — Ejercicios Oficiales de Cátedra (average, getMaxHeight, calcMaxSum)',
    ra: 'RA2 · RA4',
    goal: 'Programar sin mirar apuntes los 3 ejercicios oficiales sobre TNode* dominando acumuladores por referencia y backtracking sobre ramas raíz-hoja.',
    widgetId: null,
    simpleHtml: `
      <p><strong>Los 3 moldes de Clase 07.1 son preguntas directas de certamen:</strong></p>
      <div class="grid-3">
        <div class="v-card"><h4>1. average(root)</h4><p>No dividas en cada nodo: haz un helper <code>void acumular(TNode* r, int&amp; suma, int&amp; cont)</code> y al final retorna <code>cont == 0 ? 0.0f : (float)suma / cont</code>.</p></div>
        <div class="v-card"><h4>2. getMaxHeight(root)</h4><p>En una sola línea base + una recursiva: <code>if (!r) return 0;</code> y <code>return 1 + max(getMaxHeight(r-&gt;left), getMaxHeight(r-&gt;right));</code> (raíz = nivel 1).</p></div>
        <div class="v-card"><h4>3. calcMaxSum (Backtracking)</h4><p>Inicializa <code>maxVal = INT_MIN</code> (por si todo el árbol es negativo!), haz <code>rutaAct.push_back(r-&gt;label)</code> al bajar, evalúa <strong>solo en hojas</strong> (<code>!left &amp;&amp; !right</code>) y haz <code>pop_back()</code> al subir.</p></div>
      </div>
      <pre class="code-box"><code>void dfsMax(TNode* r, int sumaAct, vector&lt;char&gt;&amp; rutaAct, int&amp; maxVal, vector&lt;char&gt;&amp; maxPath) {
    if (!r) return;
    sumaAct += r-&gt;value;
    rutaAct.push_back(r-&gt;label);
    if (!r-&gt;left &amp;&amp; !r-&gt;right) { // ¡SOLO una hoja cierra una rama!
        if (sumaAct &gt; maxVal) { maxVal = sumaAct; maxPath = rutaAct; }
    } else {
        dfsMax(r-&gt;left, sumaAct, rutaAct, maxVal, maxPath);
        dfsMax(r-&gt;right, sumaAct, rutaAct, maxVal, maxPath);
    }
    rutaAct.pop_back(); // Backtracking: deshacer antes de volver al padre
}</code></pre>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">Dibuja el árbol de Clase 07.1 (<code>A[5] → B[4]→D[11]→(G[7], H[2])</code> y <code>C[8]→(E[13], F[4]→I[1])</code>) y pinta con destacador las 4 rutas hasta las hojas: <code>27 (ABDG, ganadora)</code>, <code>22 (ABDH)</code>, <code>26 (ACE)</code> y <code>18 (ACFI)</code>.</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Enunciados Oficiales Clase 07.1 (Abre Main.cpp y resuelve Nivel 1 → 2 → 3)</h4>
        <ul style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li><strong>Nivel 1:</strong> <code>float average(TNode* root)</code> (esperado: <code>6.11111</code>) e <code>int getMaxHeight(TNode* root)</code> (esperado: <code>4</code>).</li>
          <li><strong>Nivel 2:</strong> <code>void calcMaxSum(TNode* root, int&amp; maxValue, vector&lt;char&gt;&amp; maxPath)</code> (esperado: <code>27</code> con <code>A B D G</code>, y en árbol negativo <code>-15</code> con <code>X Y</code>).</li>
          <li><strong>Nivel 3:</strong> <code>bool existeSumaCamino(root, objetivo)</code> y <code>int sumaHojasIzquierdas(root)</code> (esperado: <code>20 = 7 + 13</code>).</li>
        </ul>
      </div>
    `,
    files: [
      'EstructuraDeDatos/Estructura-de-Datos-Cpp/02_Prueba_2/Material_Teorico/07.1 - [U4] Ejercicios Árboles.pdf',
      'EstructuraDeDatos/Estructura-de-Datos-Cpp/02_Prueba_2/Modulos_Practica/03_Clase_07_1_Ejercicios_Arboles/02_Enunciados/Main.cpp'
    ]
  },

  {
    id: 'mie25_b2',
    dayId: 'mie25',
    num: 2,
    time: '16:00–17:00 (60 min)',
    course: 'edd',
    courseLabel: 'Estructura C++ #5',
    title: 'Módulo 04 — Árboles AVL, Factor de Balance, Rotaciones y POO',
    ra: 'RA1 (POO) · RA2 (O(log n)) · RA4 (AVL)',
    goal: 'Dominar las 4 rotaciones AVL (LL, RR, LR, RL) en papel y en código C++ manteniendo altura O(log n) garantizada y encapsulamiento POO.',
    widgetId: 'edd_avl_rotaciones',
    simpleHtml: `
      <p><strong>Por qué existe el AVL:</strong> un ABB común se arruina si le meten datos ordenados (altura <code>n</code>). El AVL vigila en cada nodo su <strong>Factor de Balance <code>FB = altura(izq) − altura(der)</code></strong>. Mientras valga <code>-1, 0 o +1</code> está sano; apenas llega a <code>+2</code> o <code>-2</code> al subir de insertar/borrar, aplica 1 rotación en <code>O(1)</code> y mantiene el árbol siempre en <strong><code>O(log n)</code></strong>.</p>
      <pre class="code-box"><code>NodoAVL* rotarDerecha(NodoAVL* z) {
    NodoAVL* y = z-&gt;izq;
    NodoAVL* T2 = y-&gt;der;
    y-&gt;der = z;
    z-&gt;izq = T2;
    actualizarAltura(z); // ¡REGLA DE ORO: PRIMERO Z (el nodo que bajó)!
    actualizarAltura(y); // DESPUÉS Y (la nueva raíz que subió)
    return y;
}</code></pre>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">Haz una tabla 2×2 de signos en tu cuaderno: <strong>Mismo signo = Rotación Simple</strong> (<code>+2, ≥0 → LL rotDer</code> | <code>-2, ≤0 → RR rotIzq</code>); <strong>Signo opuesto = Rotación Doble</strong> (<code>+2, -1 → LR</code> | <code>-2, +1 → RL</code>, donde siempre el nieto del medio sube como nueva raíz!).</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Enunciados Módulo 04 AVL (Papel + Main.cpp)</h4>
        <ul style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li><strong>Traza en papel:</strong> inserta <code>10, 20, 30, 15, 25, 5, 1</code> anotando qué inserción dispara rotación y qué caso es.</li>
          <li><strong>Código Nivel 1–2:</strong> implementa <code>altura</code>, <code>obtenerFB</code>, <code>rotarDerecha</code>, <code>rotarIzquierda</code>, <code>balancear</code> e <code>insertarNodo</code> (altura final esperada: <code>4</code>).</li>
          <li><strong>Código Nivel 3:</strong> <code>eliminarNodo</code> con rebalanceo y prueba de estrés ascendente <code>1..15</code> (¡altura <code>4</code> en vez de <code>15</code>!).</li>
        </ul>
      </div>
    `,
    files: [
      'EstructuraDeDatos/Estructura-de-Datos-Cpp/02_Prueba_2/Modulos_Practica/04_Arboles_AVL_y_Rotaciones/02_Enunciados/Main.cpp',
      'EstructuraDeDatos/Estructura-de-Datos-Cpp/02_Prueba_2/Talleres/Taller-2_Hospital/src/ArbolAVL.cpp',
      'EstructuraDeDatos/Estructura-de-Datos-Cpp/01_Prueba_1/Material_Teorico/02 - [U1] Conceptos de C++ (Avanzado).pdf'
    ]
  },

  {
    id: 'mie25_b3',
    dayId: 'mie25',
    num: 3,
    time: '17:30–18:30 (60 min)',
    course: 'cd',
    courseLabel: 'Ciencia de Datos #3',
    title: 'Clase 05 — Regresión Lineal, Descenso del Gradiente, Ridge y Lasso',
    ra: 'RA3 · RA4 · RA5',
    goal: 'Interpretar con rigor los pesos w_i, entender cómo baja el Descenso del Gradiente y distinguir matemáticamente y en negocio Ridge (L2) vs. Lasso (L1).',
    widgetId: 'cd_regresion',
    simpleHtml: `
      <div class="grid-3">
        <div class="v-card"><h4>1. Qué significa el peso w₁ (enunciadoClase.txt)</h4><ul>
          <li>En <code>ŷ = b + w₁x₁ + w₂x₂</code>, <code>w₁ = ∂ŷ/∂x₁</code>: cuánto cambia <code>ŷ</code> por cada unidad extra de <code>x₁</code> <strong>manteniendo fijas las demás variables</strong>.</li>
          <li><code>w₁ = 0</code>: <code>x₁</code> no aporta relación lineal. <code>w₁ = 2</code>: subir 1 unidad en <code>x₁</code> sube 2 unidades la predicción.</li>
          <li>¡Ojo con la escala! Un peso grande no implica "más importante" si las variables no están estandarizadas.</li>
        </ul></div>
        <div class="v-card"><h4>2. ECM, OLS y Descenso del Gradiente</h4><ul>
          <li>Buscamos minimizar el <strong>ECM (MSE)</strong>: promedio de <code>(y_real − ŷ)²</code>.</li>
          <li>Se haya exacto con <strong>Mínimos Cuadrados (OLS)</strong> o iterando con <strong>Descenso del Gradiente</strong>: <code>W_t = W_(t-1) − α ∇F</code>.</li>
          <li>Polinomio grado <code>M = 9</code> con pocos datos → curva zigzagueante = <strong>Overfitting</strong>.</li>
        </ul></div>
        <div class="v-card"><h4>3. Parámetros vs. Hiperparámetros (Diap. 96)</h4><ul>
          <li><strong>Parámetros (se aprenden de los datos):</strong> pesos <code>w_i</code> e intercepto <code>b</code>.</li>
          <li><strong>Hiperparámetros (los fijas tú antes):</strong> tasa <code>α</code>, grado polinomial <code>M</code> y penalización <code>λ</code> en Ridge/Lasso.</li>
          <li><strong>Ridge (L2 = λ∑w²):</strong> encoge pesos ante multicolinealidad, nunca llega a 0 exacto. <strong>Lasso (L1 = λ∑|w|):</strong> anula pesos irrelevantes a <code>0</code> (selección automática).</li>
        </ul></div>
      </div>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">Dibuja en tu cuaderno: (1) la U del error con las 3 flechas de <code>α</code> (lento, justo, rebota), y (2) al lado el <strong>círculo de Ridge</strong> vs el <strong>rombo con puntas de Lasso</strong> chocando en el eje <code>w₁ = 0</code>.</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Ponte a Prueba Oficiales de Clase 05</h4>
        <ol style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li>Tienes 50 variables predictoras y sospechas que solo 8 sirven realmente. ¿Usas Ridge o Lasso y por qué?</li>
          <li>¿Qué le pasa al ECM de entrenamiento vs. ECM de prueba cuando subes de un polinomio grado 1 a grado 9 con pocos datos?</li>
        </ol>
        <details class="sol-toggle"><summary>Ver respuestas</summary>
          1) <strong>Lasso (L1)</strong>, porque fuerza exactamente a cero los coeficientes de las ~42 variables irrelevantes, seleccionando características automáticamente.<br/>
          2) El ECM de entrenamiento cae casi a cero (memoriza los puntos), pero el ECM de prueba se dispara por sobreajuste (alta varianza).
        </details>
      </div>
    `,
    files: [
      'CienciadeDatos/Clase 05 - Regresión lineal.pdf (98 diapositivas)',
      'CienciadeDatos/enunciadoClase.txt'
    ]
  },

  /* ================= JUEVES 26 (2 BLOQUES MAÑANA ≤ 13:00) ================= */
  {
    id: 'jue26_b1',
    dayId: 'jue26',
    num: 1,
    time: '09:30–10:30 (60 min · Cronómetro real)',
    course: 'edd',
    courseLabel: 'Estructura C++ #6',
    title: 'Módulo 05 — Simulacro Cronometrado de Prueba 2 en C++',
    ra: 'RA1 · RA2 · RA4 (Ensayo real)',
    goal: 'Rendir 60 minutos reales sin apuntes (Selección múltiple + Trazado en papel + 3 funciones en C++) usando el temporizador de arriba.',
    widgetId: 'edd_simulacro_quiz',
    simpleHtml: `
      <p><strong>Activa el reloj de 60:00 arriba a la derecha y cierra todos tus apuntes:</strong> reparte tu hora en <strong>10 min Parte 1</strong> (quiz interactivo abajo), <strong>15 min Parte 2</strong> (trazado en tu cuaderno) y <strong>35 min Parte 3</strong> (programar y compilar en <code>Main.cpp</code>).</p>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;"><strong>Parte 2 en tu cuaderno (20 pts):</strong> inserta <code>35, 15, 50, 10, 25, 20</code> primero en un <strong>ABB normal</strong> (anota sus 4 recorridos y luego aplica <code>remove(15)</code>) y después en un <strong>AVL vacío</strong> (detecta el caso <code>LR</code> al insertar <code>20</code>!).</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Parte 3 — Programación en C++ (40 pts en 05_Simulacro_Prueba_2/02_Enunciados/Main.cpp)</h4>
        <ol style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li><strong>Nivel 1 (10 pts):</strong> <code>int contarConUnSoloHijo(const TNode* root)</code> — cuenta nodos con exactamente 1 hijo (XOR lógico: <code>(r-&gt;left != nullptr) != (r-&gt;right != nullptr)</code>).</li>
          <li><strong>Nivel 2 (15 pts):</strong> <code>int sumarEnRangoABB(const TNode* root, int low, int high)</code> — suma valores en <code>[low, high]</code> <strong>podando ramas inútiles</strong> (si <code>r-&gt;dato &lt; low</code> solo ve a la derecha; si <code>r-&gt;dato &gt; high</code> solo ve a la izquierda!).</li>
          <li><strong>Nivel 3 (15 pts):</strong> <code>bool esArbolCompleto(const TNode* root)</code> — BFS con <code>queue&lt;const TNode*&gt;</code> encolando también los <code>nullptr</code>: si después de ver el primer <code>nullptr</code> aparece un nodo no nulo, retorna <code>false</code>!</li>
        </ol>
      </div>
    `,
    files: [
      'EstructuraDeDatos/Estructura-de-Datos-Cpp/02_Prueba_2/Modulos_Practica/05_Simulacro_Prueba_2/02_Enunciados/README.md',
      'EstructuraDeDatos/Estructura-de-Datos-Cpp/02_Prueba_2/Modulos_Practica/05_Simulacro_Prueba_2/02_Enunciados/Main.cpp'
    ]
  },

  {
    id: 'jue26_b2',
    dayId: 'jue26',
    num: 2,
    time: '11:00–12:00 (60 min · Cierre obligatorio ≤ 13:00)',
    course: 'edd',
    courseLabel: 'Estructura C++ #7 (Cierre)',
    title: 'Corrección del Simulacro y Checklist Anti-Errores Pre-Prueba',
    ra: 'RA1 · RA2 · RA4 (Listo para las 16:15)',
    goal: 'Corregir cada detalle del simulacro, verificar las 5 trampas clásicas de C++ y cortar estudio a más tardar a las 13:00 (sin bloques post-prueba).',
    widgetId: null,
    simpleHtml: `
      <div class="grid-2">
        <div class="v-card"><h4>Las 5 Trampas que Debes Revisar Antes de Compilar</h4><ol style="margin:0;padding-left:1.2rem;font-size:0.85rem;">
          <li><strong>Acceso a <code>nullptr</code>:</strong> ¿pusiste <code>if (r == nullptr)</code> en la línea 1 de toda función recursiva o iterativa?</li>
          <li><strong>Borrar raíz en <code>ABB::remove</code>:</strong> ¿actualizaste el atributo <code>this-&gt;root</code> de la clase?</li>
          <li><strong>Orden de alturas en AVL:</strong> ¿actualizaste primero el nodo que bajó (<code>Z</code>) y después el que subió (<code>Y</code>)?</li>
          <li><strong>Poda real en ABB:</strong> si no podas ramas fuera de rango en un ABB, te bajan puntaje por hacer <code>O(n)</code> cuando era <code>O(log n + k)</code>.</li>
          <li><strong>Destructor POO:</strong> ¿cada <code>new</code> se libera en Post-orden en <code>~Clase()</code>?</li>
        </ol></div>
        <div class="v-card"><h4>Tabla Flash de Complejidades</h4>
          <table class="clean-tbl">
            <tr><th>Operación</th><th>ABB Prom.</th><th>ABB Peor</th><th>AVL Siempre</th></tr>
            <tr><td><code>find / insert / remove</code></td><td><code>O(log n)</code></td><td><code>O(n)</code></td><td><strong><code>O(log n)</code></strong></td></tr>
            <tr><td>Recorridos (Pre/In/Post/BFS)</td><td colspan="3">Tiempo <code>O(n)</code> · Espacio <code>O(h)</code> (Enhebrado: <code>O(1)</code>)</td></tr>
          </table>
        </div>
      </div>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">Revisa los dibujos de tu Parte 2 del simulacro: al insertar <code>20</code> en el AVL <code>{35, 15, 50, 10, 25}</code>, <code>FB(35)=+2</code> y <code>FB(15)=-1</code> → rotación <strong>LR</strong> (<code>rotIzq(15)</code> luego <code>rotDer(35)</code>), quedando <strong><code>25</code> como nueva raíz</strong>. ¡A las 12:00–13:00 cierra todo, almuerza tranquilo y después de la prueba de las 16:15 tarde libre!</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Solución de Referencia — Nivel 3 (esArbolCompleto con Cola)</h4>
        <pre class="code-box"><code>bool esArbolCompleto(const TNode* root) {
    if (!root) return true;
    queue&lt;const TNode*&gt; q;
    q.push(root);
    bool vioNulo = false;
    while (!q.empty()) {
        const TNode* act = q.front(); q.pop();
        if (act == nullptr) vioNulo = true;
        else {
            if (vioNulo) return false; // ¡Había un hueco antes de un nodo real!
            q.push(act-&gt;left);
            q.push(act-&gt;right);
        }
    }
    return true;
}</code></pre>
      </div>
    `,
    files: [
      'EstructuraDeDatos/Estructura-de-Datos-Cpp/02_Prueba_2/Modulos_Practica/05_Simulacro_Prueba_2/README.md',
      'EstructuraDeDatos/Estructura-de-Datos-Cpp/GLOSARIO_SINTAXIS.md'
    ]
  },

  /* ================= VIERNES 27 (5 BLOQUES) ================= */
  {
    id: 'vie27_b1',
    dayId: 'vie27',
    num: 1,
    time: '09:00–10:00 (60 min)',
    course: 'cd',
    courseLabel: 'Ciencia de Datos #4',
    title: 'Clase 06 — Clasificación Lineal, Regresión Logística y SVM',
    ra: 'RA3 · RA4 · RA5',
    goal: 'Entender la función sigmoide y Odds Ratios en Regresión Logística, el margen máximo + C/γ/Kernel en SVM, y resolver matrices de confusión con clases desbalanceadas.',
    widgetId: 'cd_clasificacion',
    simpleHtml: `
      <div class="grid-3">
        <div class="v-card"><h4>1. Regresión Logística (¡Clasifica, no regresa!)</h4><ul>
          <li>Pasa la recta <code>z = b + w·x</code> por la <strong>sigmoide</strong> <code>σ(z) = 1 / (1 + e⁻ᶻ)</code> para aplastarla entre <code>0 y 1</code> (probabilidad).</li>
          <li><strong>Odds Ratio (Taller 2 H&amp;M):</strong> <code>OR = e^(w_i)</code>. Si <code>OR &gt; 1</code> aumenta los odds de alta demanda; si <code>OR &lt; 1</code> los reduce.</li>
        </ul></div>
        <div class="v-card"><h4>2. Support Vector Machines (SVM)</h4><ul>
          <li>Busca la calle (hiperplano) con el <strong>máximo margen</strong> de separación entre clases.</li>
          <li><strong><code>C</code> (Regularización):</strong> <code>C</code> grande = calle angosta estricta (riesgo overfitting); <code>C</code> chico = margen ancho permisivo.</li>
          <li><strong><code>γ</code> (Gamma):</strong> alcance de cada punto (<code>γ</code> alto = islas apretadas alrededor de cada dato → overfitting).</li>
          <li><strong>Kernel:</strong> proyecta datos no separables (ej. anillos concéntricos 2D) a mayor dimensión donde sí los corta un plano.</li>
        </ul></div>
        <div class="v-card"><h4>3. Desbalanceo de Clases (Diap. 52–53)</h4><ul>
          <li>Si 95% es clase 0, predecir siempre 0 da 95% de Accuracy pero 0% de utilidad.</li>
          <li><strong>Soluciones de muestreo:</strong> <em>Undersampling</em> (bajar clase mayoritaria) u <em>Oversampling / SMOTE</em> (aumentar minoritaria) + mirar Precision, Recall y F1.</li>
        </ul></div>
      </div>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">Dibuja: (1) la S de la sigmoide entre 0 y 1 cortando en <code>0.5</code>; (2) dos nubes de puntos separadas por una avenida ancha con puntos en la vereda (<strong>vectores de soporte</strong>); y (3) un círculo de puntos azules rodeado de rojos en 2D → flecha <strong>Kernel</strong> → montaña 3D cortada por una hoja plana.</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Preguntas Clave de Clase 06</h4>
        <ol style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li>En diagnóstico médico de cáncer maligno (clase 1), ¿qué error es más grave (FP o FN) y qué métrica priorizas maximizar?</li>
          <li>¿Qué ocurre en una SVM con kernel RBF si subes exageradamente tanto <code>C</code> como <code>gamma</code>?</li>
        </ol>
        <details class="sol-toggle"><summary>Ver respuestas</summary>
          1) El <strong>Falso Negativo (FN)</strong> (mandar a casa a un paciente enfermo). Por eso priorizas alto <strong>Recall / Sensitivity = TP / (TP + FN)</strong> (incluso bajando el umbral por debajo de 0.5).<br/>
          2) Cae en severo <strong>overfitting</strong>: fronteras ultra retorcidas encerrando cada punto individual de entrenamiento sin generalizar.
        </details>
      </div>
    `,
    files: [
      'CienciadeDatos/Clase 06 - Clasificación Lineal.pdf (57 diapositivas)',
      'CienciadeDatos/Taller 2/Ciencia-de-Datos-2/entrega_final/Informe_Laboratorio_2_HM.pdf'
    ]
  },

  {
    id: 'vie27_b2',
    dayId: 'vie27',
    num: 2,
    time: '10:30–11:30 (60 min)',
    course: 'cd',
    courseLabel: 'Ciencia de Datos #5',
    title: 'Clase 07 — Evaluación de Modelos, Validación, Sesgo–Varianza y ROC/PR',
    ra: 'RA4 · RA5 · RA6',
    goal: 'Dominar Holdout/k-Fold/LOOCV/Bootstrap, evitar Data Leakage, leer residuos/R² ajustado en regresión y curvas ROC vs. PR en clasificación.',
    widgetId: 'cd_evaluacion',
    simpleHtml: `
      <p><strong>Mandamiento n.º 1 de Clase 07:</strong> jamás evalúes un modelo ni calcules umbrales/escaladores sobre los datos de prueba (eso es <strong>Data Leakage</strong>, justo lo que evitaste en el Taller 2 calculando P75 solo en Train!).</p>
      <div class="grid-3" style="margin-top:0.75rem;">
        <div class="v-card"><h4>Muestreo y Validación</h4><ul>
          <li><strong>Holdout (Train/Val/Test):</strong> rápido, pero depende de la suerte del corte si hay pocos datos (usar <em>estratificado</em> si hay desbalance).</li>
          <li><strong>k-Fold CV:</strong> usa todos los datos para entrenar y validar en <code>k</code> rondas. Variante extrema: <strong>LOOCV</strong> (deja 1 fuera, muy costoso).</li>
          <li><strong>Bootstrap:</strong> muestreo aleatorio <strong>con reemplazo</strong> para estimar incertidumbre.</li>
        </ul></div>
        <div class="v-card"><h4>Métricas de Regresión</h4><ul>
          <li><strong>MSE vs MAE:</strong> MSE eleva al cuadrado (castiga durísimo outliers); MAE está en la unidad original.</li>
          <li><strong>R² vs R² Ajustado (Diap. 32):</strong> <code>R²</code> sube artificialmente cada vez que metes variables basura; <strong><code>R² ajustado</code> penaliza por <code>k</code> variables</strong> inútiles!</li>
          <li><strong>Gráfico de residuos y Q-Q plot:</strong> residuos deben verse como nube sin forma (homocedástica) y alineados en el Q-Q plot (normalidad).</li>
        </ul></div>
        <div class="v-card"><h4>Umbrales, ROC-AUC y Curva PR</h4><ul>
          <li>Mover el umbral de probabilidad intercambia Precision por Recall.</li>
          <li><strong>Curva ROC (TPR vs FPR):</strong> diagonal = azar (<code>AUC = 0.5</code>), esquina sup-izq = perfecto (<code>AUC = 1.0</code>).</li>
          <li><strong>Curva PR (Precision vs Recall):</strong> mucho más honesta que ROC cuando la clase positiva es muy escasa (ej. fraude/spam raro).</li>
        </ul></div>
      </div>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">Dibuja: (1) las 4 dianas de Sesgo–Varianza, (2) el cuadrado de la <strong>Curva ROC</strong> con la diagonal punteada <code>AUC = 0.5</code> y una curva arqueada arriba hacia <code>(0,1)</code>, y (3) un gráfico de residuos sano (nube aleatoria alrededor de 0) vs uno enfermo (forma de U o embudo).</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Preguntas Trampa de Profesor Estricto (Clase 07)</h4>
        <ol style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li>"Usé 10-Fold Cross-Validation, así que obtuve 10 modelos y me quedo con el mejor de los 10". ¿Verdadero o Falso? Justifica.</li>
          <li>Agregaste 4 columnas aleatorias a tu regresión lineal y el <code>R²</code> subió de 0.71 a 0.73. ¿Mejoró el modelo?</li>
        </ol>
        <details class="sol-toggle"><summary>Ver respuestas</summary>
          1) <strong>¡Falso!</strong> (Diap. 17 textual): Validación cruzada evalúa qué tan bien generaliza la metodología/hiperparámetros promediando las 10 particiones; el modelo final se entrena luego con todos los datos de entrenamiento disponibles.<br/>
          2) <strong>No:</strong> el <code>R²</code> común nunca baja al añadir variables; debes mirar el <strong><code>R² ajustado</code></strong> (o validación fuera de muestra), que bajará al penalizar predictores sin poder explicativo.
        </details>
      </div>
    `,
    files: [
      'CienciadeDatos/Clase 07 - Evaluación de modelos.pdf (59 diapositivas)',
      'CienciadeDatos/Taller 2/Ciencia-de-Datos-2/docs/Resumen_Resultados_y_Mejoras.md'
    ]
  },

  {
    id: 'vie27_b3',
    dayId: 'vie27',
    num: 3,
    time: '12:00–13:00 (60 min)',
    course: 'cd',
    courseLabel: 'Ciencia de Datos #6',
    title: 'Clase 08 — Árboles de Decisión, Entropía, Gini, Poda y Random Forest',
    ra: 'RA3 · RA4 · RA5',
    goal: 'Calcular a mano Impureza Gini y Ganancia de Información, explicar cómo se elige α en la Poda y por qué Random Forest vence al árbol individual.',
    widgetId: 'cd_arboles_gini',
    simpleHtml: `
      <p><strong>Cómo piensa un Árbol de Decisión (juego del "Adivina Quién"):</strong> en cada nodo busca la pregunta que deje a los dos grupos hijos <strong>lo más puros posible</strong> (todos de una misma clase). Si lo dejas crecer hasta el fondo sin freno, crea una hoja por cada dato y cae en <strong>Overfitting extremo</strong>.</p>
      <div class="grid-3" style="margin-top:0.75rem;">
        <div class="v-card"><h4>Entropía vs. Impureza Gini</h4><ul>
          <li><strong>Entropía:</strong> <code>H = −∑ p_i log₂(p_i)</code>. Elegimos el atributo con mayor <strong>Ganancia de Información</strong> (mayor caída de entropía).</li>
          <li><strong>Impureza Gini:</strong> <code>Gini = 1 − ∑ p_i²</code>. Nodo 100% puro → <code>Gini = 0</code>; mezcla 50/50 → <code>Gini = 0.5</code>.</li>
        </ul></div>
        <div class="v-card"><h4>Pruning (Poda con α, Diap. 33–37)</h4><ul>
          <li>Recorta ramas que aportan poca mejora penalizando la cantidad de hojas con un costo <code>α</code>.</li>
          <li>¿Cómo se elige el mejor <code>α</code>? Empíricamente mediante <strong>Validación Cruzada (Cross-Validation)</strong>.</li>
        </ul></div>
        <div class="v-card"><h4>Random Forest (Diap. 40–45)</h4><ul>
          <li><strong>Sabiduría de la multitud (Ensamble):</strong> entrena cientos de árboles distintos dándole a cada uno una <strong>muestra aleatoria de filas y de columnas</strong>.</li>
          <li>Predice por <strong>votación mayoritaria</strong> (clasificación) o promedio (regresión), desplomando la varianza/overfitting.</li>
        </ul></div>
      </div>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">Dibuja: (1) un nodo padre mixto <code>[5 Sí, 5 No] (Gini=0.5)</code> dividiéndose en dos hijos puros <code>[5 Sí] (Gini=0)</code> y <code>[5 No] (Gini=0)</code>; y (2) 3 arbolitos distintos alimentados con muestras al azar convergiendo en una urna de <strong>Votación = Random Forest</strong>.</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Ejercicios Exactos de las Diapositivas 28 y 29 (Clase 08)</h4>
        <ol style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li>¿Cuál es la impureza Gini cuando todas las muestras de un nodo pertenecen a una sola clase?</li>
          <li>En un nodo hay 70% de muestras de clase A y 30% de clase B. Calcula su impureza Gini sin calculadora.</li>
          <li>Menciona 1 ventaja de un Árbol único frente a Random Forest, y 1 ventaja de Random Forest frente al Árbol único.</li>
        </ol>
        <details class="sol-toggle"><summary>Ver respuestas</summary>
          1) <code>1 − 1² = 0</code> (pureza total).<br/>
          2) <code>Gini = 1 − (0,7² + 0,3²) = 1 − (0,49 + 0,09) = 1 − 0,58 = 0,42</code>.<br/>
          3) El árbol único es 100% <strong>interpretable</strong> visualmente (reglas claras Si-Entonces); Random Forest pierde interpretabilidad directa pero logra mucha <strong>mayor precisión y resistencia al overfitting</strong>.
        </details>
      </div>
    `,
    files: [
      'CienciadeDatos/Clase 08 - Arboles de decision.pdf (47 diapositivas)'
    ]
  },

  {
    id: 'vie27_b4',
    dayId: 'vie27',
    num: 4,
    time: '15:00–16:00 (60 min)',
    course: 'ciber',
    courseLabel: 'Ciberseguridad #1',
    title: 'Auditoría de Seguridad (X.816), Logging / SIEM (Wazuh) y Operación de un SOC',
    ra: 'Nota 2 · SIEM + SOC',
    goal: 'Traducir el PDF denso de SIEM y SOC a un mapa mental cristalino: qué registrar, cómo opera Syslog/WinEvent/Wazuh y cómo se organiza un SOC/CERT.',
    widgetId: 'ciber_siem_soc',
    simpleHtml: `
      <p><strong>La analogía de las cámaras del edificio:</strong> las cámaras y lectores de tarjeta en cada puerta son el <strong>Logging</strong> (generan el <em>rastro de auditoría</em> cronológico, RFC 4949). La sala de pantallas que junta todas las cámaras, detecta si alguien fuerza 3 puertas seguidas y suena la sirena es el <strong>SIEM (ej. Wazuh)</strong>. Y el equipo humano de guardias por turnos que investiga la alarma y responde al robo es el <strong>SOC</strong>.</p>
      <div class="grid-3" style="margin-top:0.75rem;">
        <div class="v-card"><h4>1. Auditoría y Rastros (X.816 / RFC 4949)</h4><ul>
          <li><strong>4 niveles de rastro:</strong> Sistema (logins, red), Aplicación (fallos internos/BD), Usuario (comandos de una persona) y Físico (tarjetas de acceso).</li>
          <li><strong>¿Dónde guardar logs?</strong> En el mismo host es rápido pero un hacker con root los borra; en un <strong>servidor central dedicado (SIEM)</strong> quedan protegidos.</li>
        </ul></div>
        <div class="v-card"><h4>2. Captura y Análisis (NIST SP 800-92)</h4><ul>
          <li><strong>Windows Event Log:</strong> encabezado (hora, fuente, ID) + descripción (ej. inicio de sesión exitoso/rechazado).</li>
          <li><strong>Syslog (UNIX/Linux):</strong> estándar ligero de texto (ej. <code>sshd: Accepted publickey</code>).</li>
          <li><strong>Apps sin fuente:</strong> bibliotecas interponibles o reescritura binaria interceptan llamadas.</li>
          <li><strong>3 enfoques de análisis:</strong> Alertas básicas por firma, <strong>Línea base</strong> (qué es normal) y detección de anomalías / correlación (<strong>Wazuh</strong>).</li>
        </ul></div>
        <div class="v-card"><h4>3. SOC vs. CERT/CSIRT</h4><ul>
          <li><strong>SOC:</strong> unidad central (técnica + organizativa) que monitorea y defiende 24/7 a la empresa ("¡el gobierno no protegerá tu negocio!").</li>
          <li><strong>CERT / CSIRT sectorial:</strong> coordina respuesta a incidentes e inteligencia de amenazas entre organizaciones de un sector.</li>
          <li><strong>Mínimo indispensable (Diap. 15 SOC):</strong> SIEM + escáner de vulnerabilidades + analistas capacitados ("los pilotos del SOC").</li>
        </ul></div>
      </div>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">Dibuja en tu cuaderno un <strong>embudo de 3 pisos</strong>: arriba 4 circulitos (<code>Sistema · App · Usuario · Físico</code>) → al medio <code>Syslog / Event Log</code> entrando a una caja fuerte central <strong>SIEM (Wazuh)</strong> → abajo una flecha hacia 3 círculos de personas (<code>Tier 1 → Tier 2 → Tier 3 / CERT</code>).</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Preguntas Tipo Prueba Fácil-Directa de Ciberseguridad</h4>
        <ol style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li>¿Qué ventaja crítica tiene enviar los rastros de auditoría a un servidor SIEM centralizado en vez de dejarlos solo localmente en cada servidor?</li>
          <li>¿Por qué los datos de auditoría a nivel de sistema no bastan para aplicaciones privilegiadas críticas, y para qué sirve establecer una "línea base" (baseline)?</li>
          <li>¿Por qué comprar el mejor SIEM fracasa si descuidas el factor humano y los turnos del SOC?</li>
        </ol>
        <details class="sol-toggle"><summary>Ver respuestas</summary>
          1) Evita que un atacante que comprometa un host modifique o borre sus propias huellas, y permite correlacionar ataques que cruzan múltiples máquinas.<br/>
          2) El S.O. solo ve "el proceso leyó un archivo", mientras el log de aplicación ve "qué transacción interna o registro se alteró". La línea base define el tráfico/uso normal para descubrir picos o conductas anómalas.<br/>
          3) Porque las herramientas solo generan alertas; sin analistas entrenados ("pilotos del SOC") y procesos claros, el equipo sufre fatiga de alertas o ignora incidentes reales.
        </details>
      </div>
    `,
    files: [
      'Cibseguridad/Nota2-20261123T031544Z-1-001.zip → Nota2/SIEM_ES_fiel_final2.pdf (31 pp.)',
      'Cibseguridad/Nota2-20261123T031544Z-1-001.zip → Nota2/SOC.pdf (16 pp.)'
    ]
  },

  {
    id: 'vie27_b5',
    dayId: 'vie27',
    num: 5,
    time: '16:30–17:30 (60 min · Cierre Ciber)',
    course: 'ciber',
    courseLabel: 'Ciberseguridad #2 (Cierre)',
    title: 'Zero Trust Architecture (ZTA) en Simple + Conexión ISO 27001 / Cloud',
    ra: 'Nota 2 · Paper Syed et al. (ZTA) + Temario Austranet',
    goal: 'Dominar el paper de 37 páginas de Zero Trust en 10 ideas visuales claras (PE/PA/PEP, Auth continua, ABAC, Microsegmentación/SDP) y descansar temprano.',
    widgetId: 'ciber_zta',
    simpleHtml: `
      <p><strong>El paper de 37 páginas traducido a español simple:</strong> antes la seguridad era un castillo con foso (firewall perimetral): afuera malo, adentro todos amigos. Con la nube, teletrabajo e IoT el borde desapareció, y si un atacante robaba 1 VPN se paseaba por toda la empresa. <strong>Zero Trust (ZTA)</strong> dice: <em>"Asume que el atacante YA está adentro: nunca confíes por estar en la LAN, verifica identidad + salud del equipo + contexto en CADA petición y abre acceso solo a 1 recurso diminuto"</em>.</p>
      <div class="grid-3" style="margin-top:0.75rem;">
        <div class="v-card"><h4>1. Las 3 Piezas NIST (PE, PA, PEP)</h4><ul>
          <li><strong>PE (Policy Engine):</strong> el juez que calcula el puntaje de confianza (usa políticas, SIEM, amenaza, estado del equipo).</li>
          <li><strong>PA (Policy Administrator):</strong> el secretario que genera el token/credencial de esa sesión o ordena cortar.</li>
          <li><strong>PEP (Policy Enforcement Point):</strong> el guardia en la puerta del recurso que deja pasar o bloquea el tráfico de datos.</li>
        </ul></div>
        <div class="v-card"><h4>2. Auth Continua, ABAC y Microsegmentación</h4><ul>
          <li><strong>Auth Context-Aware y Continua:</strong> no basta la clave a las 08:00; evalúa ubicación, hora, postura del laptop y biometría/conducta durante toda la sesión.</li>
          <li><strong>ABAC / RbAC:</strong> permisos finos por atributos y riesgo (mínimo privilegio).</li>
          <li><strong>Microsegmentación y SDP:</strong> divide la red en burbujas minúsculas aisladas y oculta los servidores (<em>Software Defined Perimeter</em>: "oscuros" hasta autenticarse) para frenar el movimiento lateral.</li>
        </ul></div>
        <div class="v-card"><h4>3. Puente con ISO 27001 y Microsoft Cloud</h4><ul>
          <li>En el caso Austranet + UCN: políticas SGSI e ISO 27001 aterrizan Zero Trust en la nube real con:</li>
          <li><strong>Entra ID:</strong> Acceso Condicional + MFA + revisión de cuentas inactivas.</li>
          <li><strong>Intune:</strong> verifica que el dispositivo esté sano/cumpla normas.</li>
          <li><strong>Defender / Purview:</strong> telemetría de amenazas y protección/clasificación de datos.</li>
        </ul></div>
      </div>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">Dibuja dos mundos separados por una línea punteada horizontal: arriba <strong>Plano de Control</strong> (<code>PE ➔ PA</code>, alimentado por <code>SIEM + Políticas + Salud Equipo</code>) y abajo <strong>Plano de Datos</strong> (<code>Usuario/Equipo ➔ PEP ➔ Microsegmento único</code>). ¡Ese dibujo resume las 37 páginas del paper!</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Preguntas Tipo Prueba sobre Zero Trust e ISO 27001</h4>
        <ol style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li>¿Qué diferencia hay entre el Plano de Control (PE + PA) y el Plano de Datos (PEP) en Zero Trust, y por qué deben estar separados?</li>
          <li>¿Cómo detiene la microsegmentación un ataque de ransomware en comparación con una red plana tradicional detrás de un firewall?</li>
          <li>Da un ejemplo concreto de política Zero Trust usando Acceso Condicional en Entra ID + Intune.</li>
        </ol>
        <details class="sol-toggle"><summary>Ver respuestas</summary>
          1) Por el Plano de Control solo viajan decisiones y señales de autorización (PE decide, PA ordena), mientras el tráfico de usuario viaja por el Plano de Datos pasando por el PEP; separarlos impide que el usuario toque o ataque directamente al motor de políticas ni vea recursos antes de ser autorizado.<br/>
          2) En una red plana, al infectar 1 PC el ransomware salta libremente a los demás servidores internos; con microsegmentación cada carga está aislada y el PEP bloquea cualquier conexión lateral no autorizada.<br/>
          3) Exigir MFA resistente al phishing + equipo enrolado y saludable en Intune + ubicación permitida antes de abrir sesión administrativa, revocando sesión si sube el riesgo de identidad.
        </details>
      </div>
    `,
    files: [
      'Cibseguridad/Nota2-20261123T031544Z-1-001.zip → Nota2/Syed et al. - 2022 - Zero Trust Architecture (ZTA)...pdf',
      'Cibseguridad/Nota2-20261123T031544Z-1-001.zip → Nota2/Temario propuesto.docx'
    ]
  }
);
