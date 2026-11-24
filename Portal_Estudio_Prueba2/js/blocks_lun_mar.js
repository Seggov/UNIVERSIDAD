window.PORTAL_BLOCKS.push(
  /* ================= LUNES 23 (4 BLOQUES) ================= */
  {
    id: 'lun23_b1',
    dayId: 'lun23',
    num: 1,
    time: '09:00–10:00 (60 min)',
    course: 'arqui',
    courseLabel: 'Arquitectura #1',
    title: 'Clase 6 — Sistema de Memoria (Primaria, Caché, Disco y Virtual)',
    ra: 'RA4 · Componentes internos',
    goal: 'Explicar en simple por qué existe la jerarquía, diferenciar SRAM vs DRAM, calcular T_AC sin confundir unidades y sacar la víctima en NRU/Reloj.',
    widgetId: 'arqui_memoria',
    simpleHtml: `
      <p><strong>La analogía del chef:</strong> la CPU pica cebollas rapidísimo (se duplica cada 18 meses), pero la despensa grande (disco/RAM) queda lejos (la RAM solo acelera ~10% al año). Como hacer toda la memoria ultra-rápida sería impagable y enorme, armamos una <strong>pirámide en equipo</strong>: poquito espacio ultra-rápido arriba (Registros y Caché SRAM) y mucho espacio barato abajo (RAM DRAM y Disco/SSD).</p>
      <div class="grid-3" style="margin-top:0.8rem;">
        <div class="v-card"><h4>SRAM vs. DRAM</h4><ul>
          <li><strong>SRAM (Caché):</strong> flip-flops (transistores). 8–16× más rápida, <strong>no necesita refresco</strong>, cara y ocupa 4× más espacio.</li>
          <li><strong>DRAM (RAM principal):</strong> condensadores que se descargan solos en ms → requiere <strong>refresco periódico</strong> (pausa lectura), barata y densa.</li>
          <li>Siempre <code>t_ciclo > t_acceso</code> (por recuperación).</li>
        </ul></div>
        <div class="v-card"><h4>Caché y Localidad</h4><ul>
          <li><strong>Temporal:</strong> lo recién usado se volverá a usar (variable <code>i</code> e instrucciones de un <code>for</code>).</li>
          <li><strong>Espacial:</strong> se usarán posiciones vecinas (recorrer <code>A[1], A[2]...</code> → trae el bloque entero).</li>
          <li>Métodos acceso: Aleatorio (RAM), Directo (Disco), Secuencial (Cinta), Asociativo (Caché).</li>
        </ul></div>
        <div class="v-card"><h4>Memoria Virtual y MMU</h4><ul>
          <li>Hace creer al proceso que tiene toda la RAM continua, cargando solo su <strong>Working Set</strong> activo.</li>
          <li>La <strong>MMU</strong> protege y traduce <code>(página p, despl d) → (marco m, despl d)</code>; <code>d</code> nunca cambia.</li>
          <li><strong>Página óptima:</strong> <code>p_opt = √(2W)</code> (elegir potencia de 2 mayor más cercana).</li>
        </ul></div>
      </div>
    `,
    sketchHtml: `
      <ol style="margin:0;padding-left:1.2rem;font-size:0.88rem;color:#fde68a;">
        <li><strong>Dibuja un triángulo de 4 pisos:</strong> Registros (~1ns) → Caché SRAM (5–20ns) → RAM DRAM (60–80ns) → Disco (10ms = 10.000.000ns), con flecha hacia arriba "Más rápido y caro/bit".</li>
        <li><strong>Dibuja la caja del MBR (512 B en C0, H0, S1):</strong> <code>[ 446 B Arranque | 64 B (4×16B Particiones) | 2 B (55h AAh) ]</code> y al lado la fórmula <code>T_total = T_seek + T_latencia(0.5×60/RPM) + T_transf</code>.</li>
        <li><strong>Dibuja un reloj circular de 4 páginas</strong> (<code>R=1</code> pasa a <code>0</code> y avanza; <code>R=0</code> sale) y anota al margen: <em>Paginación = frag. interna (p/2) | Segmentación pura (S,D) = frag. externa | Seg+Pag (S,P,D) = sin frag. externa</em>.</li>
      </ol>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Preguntas de Prueba del Capítulo 1 (Responde en tu cuaderno antes de abrir)</h4>
        <ol style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li>¿Por qué la SRAM va en caché y la DRAM en memoria principal? (Cita celda física, refresco, velocidad y densidad).</li>
          <li>Con <code>T_MP = 50 ns</code>, <code>T_MS = 10 ms</code> y <code>P_MP = 0,99</code>, calcula <code>T_AC = T_MP + T_MS·(1 − P_MP)</code>.</li>
          <li>En NRU tienes <code>A(R=1,M=0)</code>, <code>B(R=0,M=1)</code> y <code>C(R=1,M=1)</code>. ¿Cuál sale primero y por qué?</li>
          <li>¿Qué es el <em>Thrashing</em> (hiperpaginación) y qué diferencia hay entre fragmentación interna y externa?</li>
        </ol>
        <details class="sol-toggle"><summary>Ver solución explicada</summary>
          1) SRAM = flip-flop, sin refresco, 8–16× más rápida pero 4× menos densa y cara. DRAM = condensador, barata/densa pero se descarga y pide refresco.<br/>
          2) <code>10 ms = 10.000.000 ns</code> → <code>T_AC = 50 + 10.000.000 × 0,01 = 100.050 ns</code> (~2000× más lento por solo 1% de fallos!).<br/>
          3) Sale <strong>B (Clase 1)</strong> antes que A (Clase 2) y C (Clase 3), porque NRU prioriza sacar páginas NO referenciadas recientemente aunque estén modificadas.<br/>
          4) Thrashing = muy pocos marcos → vive intercambiando con disco sin avanzar. Interna = sobra espacio dentro del último marco fijo; Externa = huecos sueltos entre segmentos variables.
        </details>
      </div>
    `,
    files: [
      'Arquitectura Computadores/Guia_Lectura_Prueba_2_Arquitectura.pdf (Cap. 1, pp. 2–8)',
      'Arquitectura Computadores/01_Clases/6. memoria primaria y secundaria y virtual 2026.pptx'
    ]
  },

  {
    id: 'lun23_b2',
    dayId: 'lun23',
    num: 2,
    time: '10:30–11:30 (60 min)',
    course: 'arqui',
    courseLabel: 'Arquitectura #2',
    title: 'Clases 7 y 8 — Arreglos RAID y Módulo de Entrada/Salida',
    ra: 'RA4 · Componentes internos y tolerancia a fallos',
    goal: 'Dominar la fórmula Markoviana TRT, distinguir RAID 0 a 6 (especialmente Hot Swap en Clase 7) y trazar las 3 técnicas de E/S + protocolo DMA 8237A.',
    widgetId: 'arqui_raid_dma',
    simpleHtml: `
      <div class="grid-2">
        <div class="v-card"><h4>Clase 7 · RAID en 4 reglas</h4><ul>
          <li>Une discos físicos en 1 disco lógico para ganar <strong>velocidad</strong> y <strong>continuidad 24/7</strong> (decisión económica frente al costo de <em>downtime</em>).</li>
          <li><strong>RAID 0:</strong> reparte bloques (striping), balancea carga para que <code>λ·s</code> no llegue a 1, pero <strong>no tolera fallos</strong>.</li>
          <li><strong>RAID 1:</strong> espejo exacto (50% útil, caro, permite <strong>Hot Swap</strong>).</li>
          <li><strong>RAID 3 (byte) y RAID 4 (bloque):</strong> 1 disco fijo de paridad XOR → cuello de botella y <strong>NO permiten Hot Swap</strong> según la clase.</li>
          <li><strong>RAID 5:</strong> paridad XOR rotativa en todos los discos → lecturas/escrituras concurrentes y <strong>SÍ permite Hot Swap</strong>. (RAID 10 = 1+0, RAID 6 = 1+5).</li>
        </ul></div>
        <div class="v-card"><h4>Clase 8 · Entrada/Salida sin dolor</h4><ul>
          <li><strong>Controlador E/S:</strong> puente que abstrae velocidades y formatos distintos (control, comunicación, buffering, errores).</li>
          <li><strong>Asignada en memoria</strong> (usa instrucciones de RAM, resta espacio) vs <strong>Aislada</strong> (líneas aparte, pocas instrucciones).</li>
          <li><strong>3 Técnicas:</strong> (1) <em>Polling</em> (CPU atrapada preguntando), (2) <em>Interrupciones</em> (PUSH PC/PSW → ISR → RTI; usa Daisy Chain o <code>82C59A</code> de 8/64 líneas; datos aún pasan por CPU), (3) <em>DMA</em> (<code>8237A</code> mueve directo E/S ↔ RAM por <strong>robo de ciclo</strong> sin guardar contexto).</li>
          <li><strong>Canales E/S:</strong> Selector (1 rápido a la vez) vs Multiplexor (varios a la vez por byte/bloque).</li>
        </ul></div>
      </div>
    `,
    sketchHtml: `
      <ol style="margin:0;padding-left:1.2rem;font-size:0.88rem;color:#fde68a;">
        <li><strong>Dibuja 4 cajitas de discos para RAID 3/4 vs RAID 5:</strong> en RAID 3/4 pinta el 4.º disco entero morado ("Paridad fija · NO Hot Swap"); en RAID 5 pinta una escalera diagonal <code>P1, P2, P3, P4</code> ("Paridad distribuida · SÍ Hot Swap").</li>
        <li><strong>Dibuja la curva Markoviana exponencial</strong> que sube vertical en <code>λ·s = 1</code> y escribe al lado <code>TRT = s / (1 − λ·s)</code>.</li>
        <li><strong>Dibuja las 3 cajas del DMA 8237A</strong> (Periférico — 8237A — CPU) con las 4 flechas numeradas en zigzag: <code>1.DREQ → 2.HRQ → 3.HLDA → 4.DACK</code>.</li>
      </ol>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Autoevaluación Directa (Capítulos 2 y 3)</h4>
        <ol style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li>Con <code>s = 10 ms (0,01 s)</code>, compara el <code>TRT</code> cuando llegan <code>λ = 50 req/s</code> vs <code>λ = 99 req/s</code>.</li>
          <li>¿Por qué el robo de ciclo de bus en DMA <strong>no</strong> es una interrupción?</li>
          <li>Diferencia rápida entre Daisy Chain, Intel 82C59A, Intel 82C55A e Intel 8237A.</li>
        </ol>
        <details class="sol-toggle"><summary>Ver solución</summary>
          1) Con λ=50: <code>TRT = 0,01/(1−0,5) = 20 ms</code>. Con λ=99: <code>TRT = 0,01/(1−0,99) = 1000 ms (1 s)</code> (¡50× peor!).<br/>
          2) Porque la CPU no guarda <code>PC/PSW</code> en la pila ni salta a ninguna rutina ISR; solo pausa 1 ciclo de bus.<br/>
          3) Daisy Chain = cadena hardware por cercanía a CPU; <code>82C59A</code> = árbitro de interrupciones (8 a 64 líneas); <code>82C55A</code> = interfaz periférica programable (3 puertos A,B,C de 8 bits); <code>8237A</code> = controlador DMA al vuelo (4 canales).
        </details>
      </div>
    `,
    files: [
      'Arquitectura Computadores/Guia_Lectura_Prueba_2_Arquitectura.pdf (Cap. 2–3, pp. 9–13)',
      'Arquitectura Computadores/index.html',
      'Arquitectura Computadores/01_Clases/7. Arreglos de discos RAID.pptx',
      'Arquitectura Computadores/01_Clases/8 Modulo Entrada salida 2026.pptx'
    ]
  },

  {
    id: 'lun23_b3',
    dayId: 'lun23',
    num: 3,
    time: '14:30–15:30 (60 min)',
    course: 'edd',
    courseLabel: 'Estructura C++ #1',
    title: 'Práctica Código — Complejidad (Clase 05) y Árboles Binarios / Recorridos (Clase 06)',
    ra: 'RA1 (POO) · RA2 (Complejidad) · RA4 (Árboles)',
    goal: 'Programar desde cero en C++ los 4 recorridos, conteos recursivos y destructor Post-orden sin errores de nullptr, anotando su Big-O.',
    widgetId: 'edd_recorridos',
    simpleHtml: `
      <p><strong>Ya viste la teoría de Clase 06; aquí vamos directo a soltar la mano en C++ y medir Big-O:</strong> toda función recursiva en árboles sigue exactamente el mismo molde de 2 líneas: <code>1) if (root == nullptr) return caso_base;</code> y <code>2) combinar(root->dato, llamada(left), llamada(right));</code>. Como visitas cada nodo una sola vez haciendo trabajo constante, el tiempo es <strong><code>O(n)</code></strong> y la pila recursiva gasta espacio <strong><code>O(h)</code></strong> (<code>O(log n)</code> equilibrado, <code>O(n)</code> degenerado).</p>
      <pre class="code-box"><code>// Molde maestro de destructor seguro (SIEMPRE Post-orden)
void liberar(BTNode&lt;int&gt;* r) {
    if (r == nullptr) return;
    liberar(r-&gt;left);
    liberar(r-&gt;right);
    delete r; // Recién borras el padre cuando ya borraste sus dos hijos
}</code></pre>
    `,
    sketchHtml: `
      <ol style="margin:0;padding-left:1.2rem;font-size:0.88rem;color:#fde68a;">
        <li><strong>Dibuja un nodo con 3 puntitos alrededor:</strong> punto a la izquierda = <strong>Pre-orden</strong> (al bajar), punto abajo = <strong>In-orden</strong> (entre hijos), punto a la derecha = <strong>Post-orden</strong> (al subir/borrar). ¡Con ese truco visual sacas cualquier recorrido en 10 segundos pasando el lápiz alrededor del árbol!</li>
        <li><strong>Anota las 3 fórmulas de arreglo indexado en 1:</strong> <code>izq = 2*i</code> · <code>der = 2*i + 1</code> · <code>padre = i / 2</code>, y las cotas: nivel <code>i</code> tiene máx <code>2^(i-1)</code> nodos; altura <code>K</code> tiene máx <code>2^K - 1</code>.</li>
      </ol>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Enunciados Reales de Clase 06 (Abre Main.cpp y resuelve Nivel 1 → 2 → 3)</h4>
        <ul style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li><strong>Nivel 1 (Básico):</strong> <code>preorden(root)</code>, <code>inorden(root)</code>, <code>postorden(root)</code> y <code>porNivel(root)</code> con <code>std::queue</code>.</li>
          <li><strong>Nivel 2 (Intermedio):</strong> <code>int contarHojas(root)</code>, <code>int contarEnNivel(root, nivelObjetivo)</code> (raíz = nivel 1) e <code>inordenArreglo(tree, idx)</code> en vector base 1 (<code>-1</code> = vacío).</li>
          <li><strong>Nivel 3 (Reto):</strong> <code>bool esLleno(root)</code> y <code>bool sonIsomorfos(a, b)</code> (misma forma estructural aunque cambien valores).</li>
        </ul>
        <details class="sol-toggle"><summary>Ver pauta de salidas esperadas para verificar tu código</summary>
          • Recorridos árbol prueba: Pre <code>40 8 12 80 67 102</code> | In <code>8 12 40 67 80 102</code> | Post <code>12 8 67 102 80 40</code> | Nivel <code>40 8 80 12 67 102</code>.<br/>
          • <code>contarHojas(root) = 3</code> · <code>contarEnNivel(root, 3) = 3</code> · <code>inordenArreglo = 33 12 48 20 81 61</code>.<br/>
          • <code>esLleno(root) = false</code>, <code>esLleno(lleno) = true</code> · <code>sonIsomorfos(lleno, lleno2) = true</code>.
        </details>
      </div>
    `,
    files: [
      'EstructuraDeDatos/Estructura-de-Datos-Cpp/02_Prueba_2/Material_Teorico/05 - [U3] Complejidad Algorítmica.pdf',
      'EstructuraDeDatos/Estructura-de-Datos-Cpp/02_Prueba_2/Modulos_Practica/01_Clase_06_TDA_Arbol_y_Binarios/02_Enunciados/Main.cpp',
      'EstructuraDeDatos/Estructura-de-Datos-Cpp/02_Prueba_2/Modulos_Practica/Guia_Grafica_Prueba_2.pdf (pp. 2–3)'
    ]
  },

  {
    id: 'lun23_b4',
    dayId: 'lun23',
    num: 4,
    time: '16:00–17:00 (60 min)',
    course: 'cd',
    courseLabel: 'Ciencia de Datos #1',
    title: 'Clases 01 y 02 (+ PLN) — CRISP-DM, Obtención, Limpieza, Outliers y NLP',
    ra: 'RA1 · RA2 (Base acumulativa)',
    goal: 'Asegurar el 100% de las preguntas conceptuales sobre fases de CRISP-DM, APIs REST, imputación de nulos, outliers, log(X) y procesamiento de texto.',
    widgetId: 'cd_crispdm',
    simpleHtml: `
      <div class="grid-3">
        <div class="v-card"><h4>Clase 01 · Obtención y APIs</h4><ul>
          <li><strong>CRISP-DM:</strong> 6 fases iterativas (puedes volver atrás siempre).</li>
          <li><strong>4 vías de obtención:</strong> descarga manual, Base de Datos, <strong>API REST</strong> (HTTP, URI, JSON, <em>stateless</em> sin estado y autenticación por token en header) y Web Scraping.</li>
          <li><strong>Regex:</strong> patrones para validar/extraer correos, fechas o códigos en texto crudo.</li>
        </ul></div>
        <div class="v-card"><h4>Clase 02 · Limpieza y Calidad</h4><ul>
          <li><strong>4 problemas clásicos:</strong> faltantes, duplicados, outliers y formato.</li>
          <li><strong>Outliers:</strong> <code>|Z-Score| &gt; 3</code> (si es simétrica) o rango intercuartílico <code>IQR = Q3 − Q1</code> (robusto ante extremos).</li>
          <li><strong>Sesgo positivo (cola derecha, ej. sueldos):</strong> aplicar <code>log(X)</code> compacta valores gigantes y simetriza.</li>
        </ul></div>
        <div class="v-card"><h4>PLN / NLP (Ayudantía 2 y Formativa)</h4><ul>
          <li><strong>Bag of Words (BoW):</strong> cuenta frecuencias ignorando el orden gramatical.</li>
          <li><strong>¡Ojo con Stopwords y Trigramas!</strong> Si borras las <em>stopwords</em> ("de", "no", "la") <strong>antes</strong> de armar bigramas/trigramas, unes palabras que nunca estuvieron juntas y destruyes expresiones reales ("no me gusta" → "gusta").</li>
        </ul></div>
      </div>
    `,
    sketchHtml: `
      <ol style="margin:0;padding-left:1.2rem;font-size:0.88rem;color:#fde68a;">
        <li><strong>Dibuja un círculo con las 6 fases de CRISP-DM</strong> y flechas de ida y vuelta entre pares (especialmente Business ↔ Data Understanding y Data Prep ↔ Modeling, más la flecha grande Evaluation → Business).</li>
        <li><strong>Dibuja una curva asimétrica estirada a la derecha</strong> (ingresos) → flecha <code>log(X)</code> → campana simétrica bonita.</li>
      </ol>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Preguntas Tipo Prueba Formativa (Clases 01–02 + NLP)</h4>
        <ol style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li>¿A qué fase de CRISP-DM pertenece ajustar una regresión lineal, y a cuál pertenece detectar problemas iniciales de calidad e hipótesis?</li>
          <li>¿Qué significa que una API REST sea <em>stateless</em>?</li>
          <li>¿Por qué la mediana y el IQR son preferibles a la media y desviación estándar cuando hay errores extremos en los datos (ej. presupuesto = $1 en <code>peliculas.csv</code>)?</li>
        </ol>
        <details class="sol-toggle"><summary>Ver respuestas</summary>
          1) Ajustar regresión = <strong>Fase IV (Modeling)</strong>; explorar calidad e hipótesis iniciales = <strong>Fase II (Data Understanding)</strong> (mientras que imputar/limpiar es Fase III Data Preparation).<br/>
          2) El servidor no guarda memoria de peticiones pasadas del cliente; cada request debe llevar toda la información necesaria (incluido el token).<br/>
          3) Porque un solo valor extremo arrastra la media y dispara la desviación estándar, mientras la mediana y el 50% central (<code>IQR = Q3 − Q1</code>) casi no se mueven.
        </details>
      </div>
    `,
    files: [
      'CienciadeDatos/clase01_text.txt',
      'CienciadeDatos/clase02_text.txt',
      'CienciadeDatos/Glosario_Ciencia_de_Datos_Clases_1_y_2.pdf',
      'CienciadeDatos/Resumen_Teorico_Formativa_Ciencia_de_Datos.pdf',
      'CienciadeDatos/Ayudantía 2.pdf'
    ]
  },

  /* ================= MARTES 24 (6 BLOQUES) ================= */
  {
    id: 'mar24_b1',
    dayId: 'mar24',
    num: 1,
    time: '09:00–10:00 (60 min)',
    course: 'arqui',
    courseLabel: 'Arquitectura #3',
    title: 'Clase 9 — Arquitecturas Paralelas, Pipeline, Flynn, Superescalar y Multicore',
    ra: 'RA5 · Arquitecturas de alto rendimiento',
    goal: 'Explicar como cuento sencillo Pipeline (y el problema de los saltos), Superescalar, Flynn, Ganancia Paralela, Hyperthreading y cachés Multicore.',
    widgetId: 'arqui_flynn_amdahl',
    simpleHtml: `
      <p><strong>La analogía de la lavandería:</strong> lavar, secar y doblar 1 carga antes de empezar la siguiente es secuencial. Meter la 2.ª carga a lavar apenas la 1.ª pasa a la secadora es <strong>Pipeline</strong>. Comprar 3 lavadoras distintas es <strong>Superescalar</strong>. Meter ropa de 2 hermanos en los huecos libres de las mismas máquinas es <strong>Hyperthreading (SMT)</strong>. Y tener 4 lavanderías completas en el mismo edificio es <strong>Multicore (MIMD)</strong>.</p>
      <div class="grid-3" style="margin-top:0.8rem;">
        <div class="v-card"><h4>1. Pipeline y Saltos (Branches)</h4><ul>
          <li>6 etapas CPU: <code>FI → DI → CO → FO → EI → WO</code> (en RISC: 5 etapas).</li>
          <li><strong>Enemigo n.º 1:</strong> saltos condicionales (<code>if/loop</code>) porque vacían la tubería si adivinas mal.</li>
          <li><strong>Soluciones de la clase:</strong> Múltiples flujos (IBM), Salto retardado, <em>Loop buffer</em> (Motorola) y <strong>Predicción de saltos</strong> (4 estados en Pentium).</li>
        </ul></div>
        <div class="v-card"><h4>2. Superescalar vs. Hyperthreading</h4><ul>
          <li><strong>Superescalar:</strong> varias unidades funcionales especializadas (ALU, FPU) operando en paralelo en un núcleo.</li>
          <li><strong>Threading:</strong> <em>Time-slicing</em> (turnos fijos, caro cambiar), <em>Switch-on-event</em> (cambia en esperas largas) y <strong>SMT / Hyperthreading</strong> (2 hilos usan a la vez las unidades funcionales libres sin cambiar contexto; ej. Power5 usa solo 2 hilos porque con 4 satura registros/caché y crece 24% el chip).</li>
        </ul></div>
        <div class="v-card"><h4>3. Multicore y Cachés (Diap. 63–67)</h4><ul>
          <li>Varios procesadores completos en un solo chip (<strong>MIMD</strong>).</li>
          <li><strong>L1 siempre es privada</strong> de cada núcleo (máxima velocidad).</li>
          <li><strong>L2 puede ser privada o compartida</strong> (compartida reparte espacio dinámicamente y facilita compartir datos, pero exige cuidar coherencia con <em>writeback</em>).</li>
        </ul></div>
      </div>
    `,
    sketchHtml: `
      <ol style="margin:0;padding-left:1.2rem;font-size:0.88rem;color:#fde68a;">
        <li><strong>Dibuja una escalera de 4 peldaños desfasados</strong> (Instrucción 1, 2, 3, 4 avanzando por <code>FI-DI-EI-WO</code>) y marca un rayo rojo en un salto condicional ("vacía el pipeline").</li>
        <li><strong>Dibuja la cruz 2×2 de Flynn:</strong> arriba <code>SISD | SIMD (vectores)</code>, abajo <code>MISD (raro) | MIMD (multicore)</code>.</li>
        <li><strong>Dibuja 2 núcleos arriba con su circulito L1 propio</strong> conectados a un rectángulo grande abajo <strong>L2 Compartida</strong>.</li>
      </ol>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Preguntas Clave de Clase 9 para Argumentar como Experto</h4>
        <ol style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li>¿Cuál es la diferencia entre <em>Time-slicing</em> y <em>Simultaneous Multi-Threading (Hyper-Threading)</em>?</li>
          <li>¿Por qué en el diseño IBM Power5 se eligieron 2 hilos por núcleo y no 4?</li>
          <li>Si el 50% de un programa es paralelizable (<code>B = 0,5</code>) y tienes <code>N = 4</code> núcleos, ¿cuál es la ganancia paralela?</li>
        </ol>
        <details class="sol-toggle"><summary>Ver respuestas</summary>
          1) Time-slicing alterna hilos por tajadas de tiempo (un hilo a la vez, pagando costo de cambio); Hyper-Threading ejecuta instrucciones de varios hilos <strong>en el mismo ciclo</strong> aprovechando unidades funcionales ociosas.<br/>
          2) Porque con 4 hilos los recursos compartidos (registros físicos, caché y ancho de banda a memoria) se vuelven cuello de botella.<br/>
          3) <code>Ganancia = 1 / ((1 − 0,5) + 0,5/4) = 1 / (0,5 + 0,125) = 1,6×</code>.
        </details>
      </div>
    `,
    files: [
      'Arquitectura Computadores/01_Clases/9. multiproc  2025.pptx (67 diapositivas)'
    ]
  },

  {
    id: 'mar24_b2',
    dayId: 'mar24',
    num: 2,
    time: '10:30–11:30 (60 min)',
    course: 'arqui',
    courseLabel: 'Arquitectura #4',
    title: 'Consolidación y Autoevaluación Escrita (Clases 6, 7, 8 y 9)',
    ra: 'RA4 · RA5 (Práctica argumentativa)',
    goal: 'Escribir con tus palabras y sin mirar apuntes las respuestas completas de desarrollo y cálculos de las 4 clases para asegurar nota alta.',
    widgetId: null,
    simpleHtml: `
      <p><strong>Cómo ganar puntos con un profe que valora buena teoría:</strong> nunca respondas con 3 palabras sueltas. Usa siempre la estructura de 3 pasos: <strong>(1) Qué problema físico resuelve</strong> → <strong>(2) Cómo funciona por dentro</strong> → <strong>(3) Cuál es su ventaja y su costo/límite</strong>.</p>
      <table class="clean-tbl">
        <tr><th>Si te preguntan por...</th><th>1. Problema que ataca</th><th>2. Mecanismo clave</th><th>3. Costo / Trade-off</th></tr>
        <tr><td><strong>Jerarquía / Caché</strong></td><td>Brecha velocidad CPU vs RAM</td><td>SRAM rápida + localidad espacial/temporal</td><td>SRAM ocupa 4× área y es cara</td></tr>
        <tr><td><strong>Memoria Virtual</strong></td><td>Programas mayores que RAM y multiprogramación</td><td>MMU traduce (p,d)→(m,d) + Working Set</td><td>Si faltan marcos cae en <em>Thrashing</em></td></tr>
        <tr><td><strong>RAID 5 vs 3/4</strong></td><td>Disponibilidad 24/7 y cuello de paridad</td><td>Paridad XOR distribuida en todos los discos</td><td>Permite Hot Swap y escritura concurrente</td></tr>
        <tr><td><strong>DMA (8237A)</strong></td><td>CPU desperdiciada moviendo bloques grandes</td><td>Robo de ciclo al vuelo (DREQ→HRQ→HLDA→DACK)</td><td>1 sola interrupción al final del bloque</td></tr>
        <tr><td><strong>Pipeline + SMT</strong></td><td>Unidades internas ociosas en cada instrucción</td><td>Solapar etapas + rellenar huecos con 2 hilos</td><td>Riesgos de salto y contención de caché/bus</td></tr>
      </table>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">Toma una hoja en blanco, divídela en 4 cuadrantes (<strong>Memoria · RAID · E/S · Paralelismo</strong>) y escribe de memoria las <strong>6 fórmulas del curso</strong> (<code>t_ciclo &gt; t_acceso</code>, capacidad/latencia disco, <code>T_AC</code>, <code>p_opt = √(2W)</code>, <code>TRT = s/(1−λs)</code> y Ganancia Paralela).</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Simulacro Escrito de 4 Preguntas de Desarrollo (12 min c/u en tu cuaderno)</h4>
        <ol style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li>Explica paso a paso qué ocurre desde que la CPU emite una dirección virtual <code>(p, d)</code> cuyo bit <code>P/A = 0</code> en una RAM llena, usando algoritmo NRU.</li>
          <li>Un banco duda entre RAID 0, RAID 1, RAID 4 y RAID 5 para su servidor transaccional. Argumenta cuál recomiendas usando balance de carga, XOR y Hot Swap.</li>
          <li>Compara E/S por Interrupciones frente a DMA en la lectura de un archivo de 50 MB desde disco, detallando qué hace el procesador en cada caso.</li>
          <li>Explica por qué un procesador moderno combina Pipeline + Superescalar + Hyperthreading + Multicore en lugar de solo subir los GHz del reloj.</li>
        </ol>
      </div>
    `,
    files: [
      'Arquitectura Computadores/Guia_Lectura_Prueba_2_Arquitectura.pdf (pp. 8, 10, 13–15)',
      'Arquitectura Computadores/01_Clases/9. multiproc  2025.pptx'
    ]
  },

  {
    id: 'mar24_b3',
    dayId: 'mar24',
    num: 3,
    time: '12:00–13:00 (60 min)',
    course: 'edd',
    courseLabel: 'Estructura C++ #2',
    title: 'Clase 07 (Parte 1) — Árboles Enhebrados y ABB (insert y find)',
    ra: 'RA1 · RA2 · RA4',
    goal: 'Entender las hebras In-orden (espacio O(1)) y programar en C++ con POO las operaciones insert, find, minimo/maximo e inorden de un ABB.',
    widgetId: null,
    simpleHtml: `
      <div class="grid-2">
        <div class="v-card"><h4>1. Árbol Binario Enhebrado (En simple)</h4>
          <p>En un árbol de <code>n</code> nodos sobran <code>n + 1</code> punteros <code>nullptr</code>. ¡No los desperdicies! Si <code>rightThread == true</code>, el puntero <code>right</code> es una <strong>hebra</strong> que salta directo al <strong>sucesor In-orden</strong>; si <code>leftThread == true</code>, apunta al <strong>predecesor In-orden</strong>. Así recorres todo el árbol con un simple <code>while</code> en <strong>espacio O(1)</strong> (sin recursión ni pila).</p>
        </div>
        <div class="v-card"><h4>2. Propiedad de Oro del ABB (BST)</h4>
          <p>En <strong>todo</strong> nodo <code>N</code>: todo su subárbol izquierdo es <code>&lt; N</code> y todo su subárbol derecho es <code>&gt; N</code>. Búsqueda e inserción bajan como búsqueda binaria: <strong><code>O(log n)</code> promedio</strong>, pero si insertas datos ya ordenados (<code>10, 20, 30, 40</code>) se vuelve un fideo inclinado de costo <strong><code>O(n)</code></strong>.</p>
        </div>
      </div>
      <pre class="code-box"><code>// Recorrido In-orden iterativo en Árbol Enhebrado — O(n) tiempo y O(1) espacio!
void inordenEnhebrado(const TBTNode* root) {
    if (!root) return;
    const TBTNode* act = root;
    while (!act-&gt;leftThread) act = act-&gt;left; // 1. Ir al extremo izquierdo
    while (act != nullptr) {
        cout &lt;&lt; act-&gt;value &lt;&lt; " ";
        if (act-&gt;rightThread) act = act-&gt;right; // 2. Saltar directo por la hebra al sucesor
        else {
            act = act-&gt;right;                   // 3. Entrar al subárbol derecho real...
            while (act &amp;&amp; !act-&gt;leftThread) act = act-&gt;left; // ...y bajar al menor
        }
    }
}</code></pre>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">Dibuja el árbol <code>A</code> (izq <code>B</code> con hijos <code>D, E</code>; der <code>C</code> con izq <code>F</code>). Escribe abajo su In-orden: <code>D - B - E - A - F - C</code>. Ahora de cada hijo nulo saca una <strong>flecha punteada verde</strong> hacia su vecino en esa lista (ej. <code>E->right</code> sube a <code>A</code>; <code>F->left</code> sube a <code>A</code> y <code>F->right</code> sube a <code>C</code>).</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Enunciados Clase 07 — Parte 1 y Reto Enhebrado (Programa en Main.cpp)</h4>
        <ul style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li><strong>Nivel 1:</strong> implementa en la clase <code>ABB</code>: <code>bool insert(int value)</code> (sin duplicados), <code>bool find(int value) const</code>, <code>int minimo() const</code>, <code>int maximo() const</code> y <code>void inorden(vector&lt;int&gt;&amp; out) const</code>.</li>
          <li><strong>Nivel 3 (Enhebrado):</strong> implementa <code>void inordenEnhebrado(const TBTNode* root)</code> sin recursión ni <code>stack</code> (debe imprimir <code>D B E A F C</code>).</li>
        </ul>
      </div>
    `,
    files: [
      'EstructuraDeDatos/Estructura-de-Datos-Cpp/02_Prueba_2/Material_Teorico/07 - [U4] Árboles Binarios Enhebrados, ABB.pdf',
      'EstructuraDeDatos/Estructura-de-Datos-Cpp/02_Prueba_2/Modulos_Practica/02_Clase_07_Enhebrados_y_ABB/01_Practica_y_Apuntes/Main.cpp',
      'EstructuraDeDatos/Estructura-de-Datos-Cpp/02_Prueba_2/Modulos_Practica/02_Clase_07_Enhebrados_y_ABB/02_Enunciados/Main.cpp'
    ]
  },

  {
    id: 'mar24_b4',
    dayId: 'mar24',
    num: 4,
    time: '15:00–16:00 (60 min)',
    course: 'edd',
    courseLabel: 'Estructura C++ #3',
    title: 'Clase 07 (Parte 2) — Práctica Intensiva de ABB::remove y Validación',
    ra: 'RA1 · RA4',
    goal: 'Programar sin apuntes los 3 casos de ABB::remove y esABBValido(min, max), superando los dos casos trampa de certamen.',
    widgetId: 'edd_abb_remove',
    simpleHtml: `
      <p><strong>Por qué dedicamos 1 bloque entero a <code>remove</code>:</strong> es la función donde cae el 80% del curso en la prueba. Si la escribes de forma recursiva devolviendo <code>Nodo*</code> (el nuevo subárbol actualizado), ¡los casos borde de eliminar la raíz y reconectar al padre del sucesor quedan limpísimos en 20 líneas!</p>
      <pre class="code-box"><code>Nodo* eliminarRec(Nodo* r, int val, bool&amp; borrado) {
    if (!r) return nullptr;
    if (val &lt; r-&gt;dato) r-&gt;izq = eliminarRec(r-&gt;izq, val, borrado);
    else if (val &gt; r-&gt;dato) r-&gt;der = eliminarRec(r-&gt;der, val, borrado);
    else {
        borrado = true;
        if (!r-&gt;izq) { Nodo* tmp = r-&gt;der; delete r; return tmp; } // Caso 0 o 1 hijo der
        if (!r-&gt;der) { Nodo* tmp = r-&gt;izq; delete r; return tmp; } // Caso 1 hijo izq
        // Caso 2 hijos: buscar menor del subárbol derecho (sucesor inorden)
        Nodo* suc = r-&gt;der;
        while (suc-&gt;izq) suc = suc-&gt;izq;
        r-&gt;dato = suc-&gt;dato; // Copiar clave del sucesor
        bool dummy = false;
        r-&gt;der = eliminarRec(r-&gt;der, suc-&gt;dato, dummy); // Borrar sucesor (tendrá 0 o 1 hijo der!)
    }
    return r;
}</code></pre>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">Dibuja los 3 mini-dibujos en fila en tu cuaderno: <strong>(1) Hoja:</strong> tijera corta cable y <code>nullptr</code>; <strong>(2) 1 Hijo:</strong> cable hace puente directo del abuelo al nieto; <strong>(3) 2 Hijos:</strong> das 1 paso a la derecha (<code>r-&gt;der</code>) y todo a la izquierda hasta topar (ese es el sucesor <code>S</code>; recuerda que <code>S</code> puede tener hijo derecho).</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Enunciados Nivel 2 de Clase 07 (Compila y pasa todos los tests)</h4>
        <ol style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li>Implementa <code>bool remove(int value)</code> probando en secuencia sobre <code>{50,30,70,20,40,60,80,65}</code>: borrar hoja <code>20</code>, borrar 1-hijo <code>60</code> y borrar la raíz <code>50</code> (debe quedar In-orden <code>30 40 65 70 80</code>).</li>
          <li>Implementa <code>bool esABBValido() const</code> usando cotas recursivas <code>(long long minVal, long long maxVal)</code> (¡ojo: no basta comparar solo con el padre inmediato!).</li>
        </ol>
      </div>
    `,
    files: [
      'EstructuraDeDatos/Estructura-de-Datos-Cpp/02_Prueba_2/Modulos_Practica/02_Clase_07_Enhebrados_y_ABB/02_Enunciados/README.md',
      'EstructuraDeDatos/Estructura-de-Datos-Cpp/02_Prueba_2/Modulos_Practica/02_Clase_07_Enhebrados_y_ABB/02_Enunciados/Main.cpp'
    ]
  },

  {
    id: 'mar24_b5',
    dayId: 'mar24',
    num: 5,
    time: '16:30–17:30 (60 min)',
    course: 'cd',
    courseLabel: 'Ciencia de Datos #2',
    title: 'Clase 04 — Exploración de Datos, Tipos de Variables y Visualización',
    ra: 'RA1 · RA2 · RA6 (Comunicar análisis)',
    goal: 'Clasificar sin dudar cualquier variable en las 4 escalas y elegir el gráfico exacto 1D/2D/3D evitando errores de integridad visual.',
    widgetId: 'cd_visualizacion',
    simpleHtml: `
      <p><strong>La moraleja del Datasaurus Dozen (Diap. 11):</strong> 13 datasets distintos (¡uno con forma de dinosaurio!) tienen exactamente la misma media, varianza y correlación. <strong>Moraleja para la prueba:</strong> mirar solo promedios sin graficar te deja ciego; siempre explora visualmente antes de modelar.</p>
      <div class="grid-2" style="margin-top:0.75rem;">
        <div class="v-card"><h4>Exploración vs. Presentación</h4><ul>
          <li><strong>Exploración:</strong> para ti como analista, descubrir qué es verdad (rápida, prueba hipótesis, detecta anomalías).</li>
          <li><strong>Presentación:</strong> para convencer/comunicar al cliente o gerencia con claridad e integridad gráfica (RA6).</li>
        </ul></div>
        <div class="v-card"><h4>Intervalo vs. Razón (La duda típica)</h4><ul>
          <li><strong>Intervalo:</strong> numérico sin cero absoluto (<code>0 °C</code> no es "ausencia de calor"; no puedes decir que 20°C es el doble de calor que 10°C).</li>
          <li><strong>Razón:</strong> tiene <strong>cero absoluto real</strong> (sueldo $0, 0 hijos, distancia 0 km → $200 sí es el doble de $100).</li>
        </ul></div>
      </div>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">Dibuja los <strong>4 círculos uno dentro de otro</strong> (Nominal → Ordinal → Intervalo → Razón) y al lado una tablita rápida: <code>1 Cat → Barras</code> · <code>1 Num → Histograma</code> · <code>Cat+Num → Boxplot/Violín</code> · <code>2 Num → Scatter</code> · <code>2 Num + 1 Cat → Scatter con color</code>.</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Casos Tipo Prueba (Clase 04 + Ayudantía 3 Películas)</h4>
        <ol style="margin:0;padding-left:1.2rem;font-size:0.86rem;">
          <li>Clasifica: (a) Estado civil, (b) Nivel socioeconómico (Bajo/Medio/Alto), (c) Temperatura en °C, (d) Recaudación en USD de una película.</li>
          <li>¿Por qué la cátedra desaconseja el gráfico de torta cuando hay varias categorías parecidas, y por qué está mal unir con una línea las barras de "Carrera Universitaria"?</li>
        </ol>
        <details class="sol-toggle"><summary>Ver respuestas</summary>
          1) (a) Nominal, (b) Ordinal, (c) Intervalo, (d) Razón continua.<br/>
          2) El ojo humano compara mucho mejor longitudes alineadas (barras) que ángulos/áreas (torta). Unir barras nominales con líneas sugiere falsamente una tendencia continua u orden inexistente entre categorías.
        </details>
      </div>
    `,
    files: [
      'CienciadeDatos/CLASE 04.pdf (64 diapositivas)',
      'CienciadeDatos/Ayudantia3.pdf'
    ]
  },

  {
    id: 'mar24_b6',
    dayId: 'mar24',
    num: 6,
    time: '18:30–19:30 (60 min · Movido del Mié mañana)',
    course: 'arqui',
    courseLabel: 'Arquitectura #5 (Cierre)',
    title: 'Repaso Final Pre-Prueba de Arquitectura (Clases 6, 7, 8 y 9)',
    ra: 'RA4 · RA5 (Listo para mañana 10:00)',
    goal: 'Cerrar la preparación de Arquitectura la tarde-noche del martes (15 min por clase, sin materia nueva) para llegar descansado el miércoles a las 10:00.',
    widgetId: null,
    simpleHtml: `
      <p><strong>Estrategia de estos 60 minutos (4 bloques de 15 min con tus propios dibujos en mano):</strong> como mañana miércoles en la mañana no hay bloque de estudio, hoy dejas todo abrochado y te vas a descansar a las 19:30.</p>
      <div class="grid-4">
        <div class="v-card"><h4>Min 00–15 · Clase 6</h4><p>Repasa pirámide, SRAM vs DRAM, localidad, disco/MBR, <code>T_AC</code>, NRU/Reloj, <code>p_opt=√(2W)</code>, Thrashing y Seg+Pag.</p></div>
        <div class="v-card"><h4>Min 15–30 · Clase 7</h4><p>Repasa <code>TRT = s/(1−λs)</code>, tabla RAID 0 a 6/10, reconstrucción XOR y qué niveles aceptan <strong>Hot Swap</strong> (1, 2, 5, 6, 10 sí; 3 y 4 no).</p></div>
        <div class="v-card"><h4>Min 30–45 · Clase 8</h4><p>Repasa Asignada vs Aislada, Polling vs INT vs DMA, Daisy Chain, <code>82C59A</code>, secuencia <code>DREQ→HRQ→HLDA→DACK</code> y Selector vs Multiplexor.</p></div>
        <div class="v-card"><h4>Min 45–60 · Clase 9</h4><p>Repasa Pipeline y saltos, matriz de Flynn, Ganancia Paralela, Superescalar vs Hyperthreading y cachés Multicore (L1 privada, L2 priv/comp).</p></div>
      </div>
    `,
    sketchHtml: `
      <p style="margin:0;font-size:0.88rem;color:#fde68a;">No hagas apuntes largos nuevos: solo pasa destacador sobre tus <strong>6 fórmulas</strong> y tus <strong>4 dibujos clave</strong> del cuaderno para fotografiarlos mentalmente antes de dormir.</p>
    `,
    practiceHtml: `
      <div class="enunciado-box">
        <h4>Chequeo Relámpago de 60 Segundos antes de Cerrar</h4>
        <p style="margin:0;font-size:0.86rem;">Di en voz alta sin mirar: (1) las 4 clases de NRU en orden, (2) las 4 señales del 8237A en orden, (3) las 4 siglas de Flynn con un ejemplo de cada una. ¡Si salen fluidas, estás listo para mañana a las 10:00!</p>
      </div>
    `,
    files: [
      'Arquitectura Computadores/Guia_Lectura_Prueba_2_Arquitectura.pdf (pp. 1 y 14)',
      'Arquitectura Computadores/index.html',
      'Tus dibujos y resúmenes de Clases 6–9'
    ]
  }
);
