window.WIDGETS = {

  /* 1. ARQUI #1 (Lun B1): Jerarquía + Calculadora T_AC + Simulador NRU/Reloj */
  arqui_memoria: function(el) {
    el.innerHTML = `
      <div class="grid-2">
        <div class="widget-box">
          <h4 style="margin:0 0 0.5rem;color:#38bdf8;">Pirámide de Jerarquía y Calculadora T_AC</h4>
          <svg viewBox="0 0 360 165" width="100%">
            <polygon points="180,10 225,45 135,45" fill="#0ea5e9" opacity="0.88"/>
            <text x="180" y="34" fill="#fff" font-size="10.5" font-weight="bold" text-anchor="middle">Registros (~1ns)</text>
            <polygon points="132,49 228,49 262,84 98,84" fill="#38bdf8" opacity="0.78"/>
            <text x="180" y="71" fill="#0f172a" font-size="11" font-weight="bold" text-anchor="middle">Caché SRAM (5-20 ns)</text>
            <polygon points="95,88 265,88 302,123 58,123" fill="#818cf8" opacity="0.8"/>
            <text x="180" y="110" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">RAM Principal DRAM (60-80 ns)</text>
            <polygon points="55,127 305,127 345,160 15,160" fill="#a78bfa" opacity="0.75"/>
            <text x="180" y="148" fill="#0f172a" font-size="11" font-weight="bold" text-anchor="middle">Disco / SSD (~10 ms = 10.000.000 ns)</text>
          </svg>
          <div style="font-size:0.82rem;margin-top:0.4rem;">
            <label style="display:flex;justify-content:space-between;">Acierto en RAM (P_MP): <strong id="pmpLbl">99.0%</strong></label>
            <input id="pmpRange" type="range" min="900" max="1000" value="990" style="width:100%;accent-color:#38bdf8;"/>
          </div>
          <div class="w-stat-row">
            <div class="w-stat"><div class="v" id="tacOut">100.050 ns</div><div class="k">T_AC (T_MP=50ns, T_MS=10ms)</div></div>
            <div class="w-stat"><div class="v" id="tacMult">2001×</div><div class="k">Frente a solo RAM</div></div>
          </div>
        </div>

        <div class="widget-box">
          <h4 style="margin:0 0 0.5rem;color:#fbbf24;">Simulador de Víctima NRU (Bits R y M)</h4>
          <p style="font-size:0.8rem;color:#94a3b8;margin:0 0 0.5rem;">Haz clic en los bits R/M de cada página y mira cuál expulsa primero NRU:</p>
          <div id="nruTableWrap"></div>
          <div id="nruVictimOut" style="margin-top:0.65rem;padding:0.5rem 0.7rem;border-radius:8px;background:#1e293b;font-size:0.84rem;color:#fde68a;"></div>
        </div>
      </div>
    `;
    const pmpRange = el.querySelector('#pmpRange');
    function updTac() {
      const p = Number(pmpRange.value) / 1000;
      el.querySelector('#pmpLbl').textContent = (p * 100).toFixed(1) + '%';
      const tac = 50 + 10000000 * (1 - p);
      el.querySelector('#tacOut').textContent = Math.round(tac).toLocaleString('es-CL') + ' ns';
      el.querySelector('#tacMult').textContent = Math.round(tac / 50) + '× más lento';
    }
    pmpRange.addEventListener('input', updTac);
    updTac();

    const pages = [
      { id: 'Pág A', r: 1, m: 0 },
      { id: 'Pág B', r: 0, m: 1 },
      { id: 'Pág C', r: 1, m: 1 }
    ];
    function renderNRU() {
      const wrap = el.querySelector('#nruTableWrap');
      pages.forEach(p => { p.cls = p.r * 2 + p.m; });
      const minCls = Math.min(...pages.map(p => p.cls));
      const victim = pages.find(p => p.cls === minCls);
      wrap.innerHTML = `<table class="clean-tbl"><tr><th>Página</th><th>R (Ref)</th><th>M (Mod)</th><th>Clase NRU</th></tr>` +
        pages.map((p, idx) => `<tr style="${p === victim ? 'background:rgba(248,113,113,0.16);' : ''}">
          <td><strong>${p.id}</strong> ${p === victim ? '👈 Víctima' : ''}</td>
          <td><button class="w-btn" data-i="${idx}" data-f="r">${p.r}</button></td>
          <td><button class="w-btn" data-i="${idx}" data-f="m">${p.m}</button></td>
          <td>Clase <strong>${p.cls}</strong></td>
        </tr>`).join('') + `</table>`;
      wrap.querySelectorAll('button').forEach(b => {
        b.onclick = () => {
          const i = Number(b.dataset.i), f = b.dataset.f;
          pages[i][f] = pages[i][f] ? 0 : 1;
          renderNRU();
        };
      });
      el.querySelector('#nruVictimOut').innerHTML = `Sale <strong>${victim.id}</strong> (Clase ${victim.cls}: R=${victim.r}, M=${victim.m}). <em>Ojo: Clase 1 (R=0,M=1) sale ANTES que Clase 2 (R=1,M=0) porque importa más que no se esté usando recién.</em>`;
    }
    renderNRU();
  },

  /* 2. ARQUI #2 (Lun B2): Curva Markoviana RAID + Stepper DMA Intel 8237A */
  arqui_raid_dma: function(el) {
    el.innerHTML = `
      <div class="grid-2">
        <div class="widget-box">
          <h4 style="margin:0 0 0.45rem;color:#38bdf8;">Curva Markoviana RAID: TRT = s / (1 − λ·s)</h4>
          <svg id="mkSvg" viewBox="0 0 380 170" width="100%">
            <line x1="40" y1="15" x2="40" y2="145" stroke="#475569"/>
            <line x1="40" y1="145" x2="355" y2="145" stroke="#475569"/>
            <line x1="340" y1="15" x2="340" y2="145" stroke="#f87171" stroke-dasharray="4,3"/>
            <text x="335" y="25" fill="#f87171" font-size="9.5" text-anchor="end">λ·s = 1 (Colapso)</text>
            <path id="mkPath" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
            <circle id="mkDot" r="5.5" fill="#fbbf24"/>
          </svg>
          <label style="font-size:0.8rem;display:flex;justify-content:space-between;">Llegadas λ (req/s) [con s = 10 ms]: <strong id="mkLamLbl">50 req/s</strong></label>
          <input id="mkLam" type="range" min="5" max="99" value="50" style="width:100%;accent-color:#38bdf8;"/>
          <div class="w-stat-row">
            <div class="w-stat"><div class="v" id="mkRho">0.50</div><div class="k">Demanda λ·s</div></div>
            <div class="w-stat"><div class="v" id="mkTrt">20.0 ms</div><div class="k">TRT Total</div></div>
          </div>
        </div>

        <div class="widget-box">
          <h4 style="margin:0 0 0.45rem;color:#34d399;">Protocolo Intel 8237A (DMA "al vuelo")</h4>
          <svg viewBox="0 0 420 110" width="100%">
            <rect x="8" y="22" width="105" height="65" rx="8" fill="#1e293b" stroke="#a78bfa" stroke-width="1.8"/>
            <text x="60" y="52" fill="#fff" font-size="10.5" font-weight="bold" text-anchor="middle">Periférico</text>
            <text x="60" y="68" fill="#94a3b8" font-size="9" text-anchor="middle">(Disco E/S)</text>

            <rect x="157" y="18" width="106" height="72" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.8"/>
            <text x="210" y="48" fill="#34d399" font-size="10.5" font-weight="bold" text-anchor="middle">Intel 8237A</text>
            <text x="210" y="64" fill="#cbd5e1" font-size="8.8" text-anchor="middle">DMA (4 canales)</text>

            <rect x="307" y="22" width="105" height="65" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.8"/>
            <text x="360" y="52" fill="#fff" font-size="10.5" font-weight="bold" text-anchor="middle">CPU</text>
            <text id="wCpuSt" x="360" y="68" fill="#94a3b8" font-size="8.8" text-anchor="middle">Normal</text>

            <line id="wDmaLn" x1="113" y1="52" x2="157" y2="52" stroke="#fbbf24" stroke-width="3"/>
            <text id="wDmaTxt" x="135" y="42" fill="#fbbf24" font-size="9.5" font-weight="bold" text-anchor="middle">1. DREQ →</text>
          </svg>
          <div class="w-controls" id="dmaBtns"></div>
          <div id="dmaExplain" style="font-size:0.82rem;color:#fde68a;min-height:38px;"></div>
        </div>
      </div>
    `;
    const mkLam = el.querySelector('#mkLam');
    function drawMk() {
      const lam = Number(mkLam.value);
      const sMs = 10, rho = lam * 0.01;
      el.querySelector('#mkLamLbl').textContent = lam + ' req/s';
      let d = '';
      for (let i = 2; i <= 96; i += 2) {
        const r = i / 100;
        const trt = sMs / (1 - r);
        const x = 40 + r * 300;
        const y = 145 - Math.min(trt, 220) / 220 * 125;
        d += (i === 2 ? 'M' : 'L') + x.toFixed(1) + ',' + y.toFixed(1) + ' ';
      }
      el.querySelector('#mkPath').setAttribute('d', d);
      const trt = sMs / (1 - rho);
      el.querySelector('#mkRho').textContent = rho.toFixed(2);
      el.querySelector('#mkTrt').textContent = trt >= 1000 ? (trt / 1000).toFixed(2) + ' s' : trt.toFixed(1) + ' ms';
      el.querySelector('#mkDot').setAttribute('cx', (40 + rho * 300).toFixed(1));
      el.querySelector('#mkDot').setAttribute('cy', (145 - Math.min(trt, 220) / 220 * 125).toFixed(1));
    }
    mkLam.addEventListener('input', drawMk);
    drawMk();

    const steps = [
      { n: '1. DREQ', x1: 113, x2: 157, txt: '1. DREQ →', cpu: 'Ejecutando', d: '1. DREQ: El periférico pide servicio DMA al 8237A.' },
      { n: '2. HRQ', x1: 263, x2: 307, txt: '2. HRQ →', cpu: 'Petición bus', d: '2. HRQ: El 8237A pide prestados los buses a la CPU.' },
      { n: '3. HLDA', x1: 307, x2: 263, txt: '← 3. HLDA', cpu: 'Idle (cede bus)', d: '3. HLDA: La CPU suelta los buses (robo de ciclo, SIN guardar PC/PSW).' },
      { n: '4. DACK', x1: 157, x2: 113, txt: '← 4. DACK', cpu: 'Idle', d: '4. DACK: El 8237A avisa al periférico que transmita directo.' },
      { n: '5. Al vuelo', x1: 113, x2: 307, txt: '5. IOR+MEMW ⇄', cpu: 'Idle', d: '5. Al vuelo: El dato viaja directo Periférico ↔ RAM por el bus sin entrar al 8237A.' },
      { n: '6. Fin', x1: 263, x2: 307, txt: '6. HRQ=0 + INT', cpu: 'Retoma bus', d: '6. Fin: Contador llega a 0, baja HRQ y manda 1 sola interrupción final.' }
    ];
    const btnWrap = el.querySelector('#dmaBtns');
    function pickStep(idx) {
      btnWrap.querySelectorAll('button').forEach((b, i) => b.classList.toggle('active', i === idx));
      const st = steps[idx];
      const ln = el.querySelector('#wDmaLn');
      ln.setAttribute('x1', st.x1); ln.setAttribute('x2', st.x2);
      const tx = el.querySelector('#wDmaTxt');
      tx.setAttribute('x', (st.x1 + st.x2) / 2); tx.textContent = st.txt;
      el.querySelector('#wCpuSt').textContent = st.cpu;
      el.querySelector('#dmaExplain').textContent = st.d;
    }
    steps.forEach((s, i) => {
      const b = document.createElement('button');
      b.className = 'w-btn'; b.textContent = s.n;
      b.onclick = () => pickStep(i);
      btnWrap.appendChild(b);
    });
    pickStep(0);
  },

  /* 3. EDD #1 (Lun B3): Animador de los 4 Recorridos sobre el árbol del enunciado */
  edd_recorridos: function(el) {
    // Árbol del enunciado Clase 06: A(1) -> B(2)[D(4)->der G(9)], C(3)[E(6)->der H(13), F(7)]
    const nodes = {
      A: { x: 190, y: 26, idx: 1 },
      B: { x: 105, y: 72, idx: 2 },
      C: { x: 275, y: 72, idx: 3 },
      D: { x: 60,  y: 120, idx: 4 },
      E: { x: 230, y: 120, idx: 6 },
      F: { x: 325, y: 120, idx: 7 },
      G: { x: 95,  y: 168, idx: 9 },
      H: { x: 265, y: 168, idx: 13 }
    };
    const edges = [['A','B'],['A','C'],['B','D'],['D','G'],['C','E'],['C','F'],['E','H']];
    const orders = {
      pre:  { name: 'Pre-orden (Raíz → Izq → Der)', seq: ['A','B','D','G','C','E','H','F'], tip: 'Útil para clonar o serializar el árbol.' },
      in:   { name: 'In-orden (Izq → Raíz → Der)',  seq: ['D','G','B','A','E','H','C','F'], tip: 'En un ABB entrega los datos de menor a mayor.' },
      post: { name: 'Post-orden (Izq → Der → Raíz)', seq: ['G','D','B','H','E','F','C','A'], tip: 'OBLIGATORIO en el destructor (~Arbol) para hacer delete de hijos antes que el padre.' },
      bfs:  { name: 'Por Nivel / BFS (std::queue)', seq: ['A','B','C','D','E','F','G','H'], tip: 'Recorre piso por piso usando una cola; clave para ver si es completo.' }
    };

    el.innerHTML = `
      <div class="widget-box">
        <h4 style="margin:0 0 0.4rem;color:#34d399;">Simulador Interactivo: Árbol Oficial de Enunciados Clase 06 (con índices de vector base 1)</h4>
        <div class="w-controls">
          <button class="w-btn active" data-k="pre">Pre-orden</button>
          <button class="w-btn" data-k="in">In-orden</button>
          <button class="w-btn" data-k="post">Post-orden (delete)</button>
          <button class="w-btn" data-k="bfs">Por Nivel (queue)</button>
        </div>
        <svg id="tree06Svg" viewBox="0 0 385 198" width="100%" style="max-height:240px;">
          ${edges.map(([u,v]) => `<line x1="${nodes[u].x}" y1="${nodes[u].y}" x2="${nodes[v].x}" y2="${nodes[v].y}" stroke="#475569" stroke-width="2"/>`).join('')}
          ${Object.entries(nodes).map(([k, n]) => `
            <g id="nd_${k}">
              <circle cx="${n.x}" cy="${n.y}" r="16" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
              <text x="${n.x}" y="${n.y+4}" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">${k}</text>
              <text x="${n.x+22}" y="${n.y+4}" fill="#94a3b8" font-size="9.5">[${n.idx}]</text>
            </g>
          `).join('')}
        </svg>
        <div id="ordSeq" style="font-size:0.92rem;font-weight:700;color:#a7f3d0;margin-top:0.3rem;"></div>
        <div id="ordTip" style="font-size:0.82rem;color:#94a3b8;margin-top:0.2rem;"></div>
      </div>
    `;

    let timer = null;
    function playOrder(key) {
      if (timer) clearInterval(timer);
      el.querySelectorAll('.w-btn').forEach(b => b.classList.toggle('active', b.dataset.k === key));
      Object.keys(nodes).forEach(k => {
        el.querySelector(`#nd_${k} circle`).setAttribute('fill', '#1e293b');
      });
      const o = orders[key];
      el.querySelector('#ordTip').textContent = `${o.name} — ${o.tip}`;
      let step = 0;
      const shown = [];
      el.querySelector('#ordSeq').textContent = 'Orden: ';
      timer = setInterval(() => {
        if (step >= o.seq.length) { clearInterval(timer); return; }
        const k = o.seq[step++];
        shown.push(k);
        el.querySelector(`#nd_${k} circle`).setAttribute('fill', '#059669');
        el.querySelector('#ordSeq').textContent = 'Orden: ' + shown.join(' → ');
      }, 360);
    }
    el.querySelectorAll('.w-btn').forEach(b => { b.onclick = () => playOrder(b.dataset.k); });
    playOrder('pre');
  },

  /* 4. CD #1 (Lun B4): Rueda Circular Interactiva CRISP-DM + Simulador Imputación */
  cd_crispdm: function(el) {
    const phases = [
      { n: '1. Business Understanding', c: 'Definir objetivo del negocio y traducirlo a problema de datos (ej. reducir quiebres de stock).' },
      { n: '2. Data Understanding', c: 'Recolectar datos iniciales, explorar calidad, detectar vacíos y formular hipótesis preliminares.' },
      { n: '3. Data Preparation', c: 'Limpiar nulos (FFILL/BFILL/media), quitar duplicados, tratar outliers (Z-Score/IQR), transformar log(X) y armar tabla final.' },
      { n: '4. Modeling', c: 'Elegir y entrenar algoritmos matemáticos (Regresión Lineal, Logística, SVM, Árboles, Redes Neuronales).' },
      { n: '5. Evaluation', c: 'Validar fuera de entrenamiento (Holdout / k-Fold CV) con métricas (MSE, R², F1, ROC-AUC) y revisar si cumple negocio.' },
      { n: '6. Deployment', c: 'Poner en producción, pipeline automatizado, reporte o toma de decisiones y monitoreo.' }
    ];
    el.innerHTML = `
      <div class="grid-2">
        <div class="widget-box">
          <h4 style="margin:0 0 0.45rem;color:#a78bfa;">Rueda Circular Interactiva CRISP-DM (No es lineal: puedes volver atrás)</h4>
          <div class="w-controls" id="crispBtns">
            ${phases.map((p, i) => `<button class="w-btn ${i===0?'active':''}" data-i="${i}">Fase ${i+1}</button>`).join('')}
          </div>
          <div id="crispDetail" style="background:#1e293b;border-left:4px solid #a78bfa;padding:0.75rem;border-radius:8px;font-size:0.86rem;"></div>
        </div>
        <div class="widget-box">
          <h4 style="margin:0 0 0.45rem;color:#38bdf8;">Simulador Rápido: FFILL vs BFILL vs Media</h4>
          <p style="font-size:0.8rem;color:#94a3b8;margin:0 0 0.5rem;">Serie temporal de temperaturas: <code>[20, NULL, 30, 50]</code>. Prueba cada método:</p>
          <div class="w-controls" id="impBtns">
            <button class="w-btn active" data-m="orig">Original</button>
            <button class="w-btn" data-m="ffill">FFILL (Forward)</button>
            <button class="w-btn" data-m="bfill">BFILL (Backward)</button>
            <button class="w-btn" data-m="mean">Media</button>
          </div>
          <div id="impResult" style="font-size:0.9rem;padding:0.65rem;background:#1e293b;border-radius:8px;color:#e2e8f0;"></div>
        </div>
      </div>
    `;
    const det = el.querySelector('#crispDetail');
    function setPhase(i) {
      el.querySelectorAll('#crispBtns button').forEach((b, idx) => b.classList.toggle('active', idx === i));
      det.innerHTML = `<strong style="color:#ddd6fe;">${phases[i].n}</strong><br/>${phases[i].c}`;
    }
    el.querySelectorAll('#crispBtns button').forEach(b => { b.onclick = () => setPhase(Number(b.dataset.i)); });
    setPhase(0);

    const impMap = {
      orig:  '<code>[20, <span style="color:#f87171">NULL</span>, 30, 50]</code> — Falta el segundo registro.',
      ffill: '<code>[20, <strong style="color:#34d399">20</strong>, 30, 50]</code> — <strong>FFILL:</strong> copia el último dato válido anterior (ideal en series de tiempo).',
      bfill: '<code>[20, <strong style="color:#fbbf24">30</strong>, 30, 50]</code> — <strong>BFILL:</strong> copia el siguiente valor válido posterior en la secuencia.',
      mean:  '<code>[20, <strong style="color:#38bdf8">33.33</strong>, 30, 50]</code> — <strong>Media:</strong> (20+30+50)/3 = 33.33 (sensible a outliers; mediana daría 30).'
    };
    const impRes = el.querySelector('#impResult');
    el.querySelectorAll('#impBtns button').forEach(b => {
      b.onclick = () => {
        el.querySelectorAll('#impBtns button').forEach(x => x.classList.remove('active'));
        b.classList.add('active');
        impRes.innerHTML = impMap[b.dataset.m];
      };
    });
    impRes.innerHTML = impMap.orig;
  },

  /* 5. ARQUI #3 (Mar B1): Matriz de Flynn 2x2 + Calculadora Ganancia Paralela (Amdahl) */
  arqui_flynn_amdahl: function(el) {
    el.innerHTML = `
      <div class="grid-2">
        <div class="widget-box">
          <h4 style="margin:0 0 0.5rem;color:#38bdf8;">Matriz Visual 2×2: Taxonomía de Flynn</h4>
          <table class="clean-tbl">
            <tr><th></th><th>1 Flujo de Datos (SD)</th><th>Múltiples Datos (MD)</th></tr>
            <tr>
              <th>1 Flujo Instrucción (SI)</th>
              <td><strong style="color:#38bdf8;">SISD</strong><br/>Monoprocesador clásico Von Neumann.</td>
              <td><strong style="color:#34d399;">SIMD</strong><br/>1 instrucción opera vectores/arreglos a la vez (GPU / vectorial).</td>
            </tr>
            <tr>
              <th>Múltiples Instrucciones (MI)</th>
              <td><strong style="color:#fbbf24;">MISD</strong><br/>Teórico / arreglos sistólicos (casi sin uso comercial).</td>
              <td><strong style="color:#a78bfa;">MIMD</strong><br/>Multiprocesadores y <strong>Multicore</strong> actuales.</td>
            </tr>
          </table>
        </div>

        <div class="widget-box">
          <h4 style="margin:0 0 0.45rem;color:#34d399;">Simulador Ganancia Paralela (Diapositiva 47)</h4>
          <p style="font-size:0.78rem;color:#94a3b8;margin:0 0 0.45rem;"><code>Ganancia = 1 / ((1 − B) + B / N)</code> donde <code>B</code> es la fracción paralelizable y <code>N</code> núcleos:</p>
          <label style="font-size:0.8rem;display:flex;justify-content:space-between;">Fracción paralelizable B: <strong id="bVal">80%</strong></label>
          <input id="bRange" type="range" min="0" max="100" value="80" style="width:100%;accent-color:#34d399;"/>
          <label style="font-size:0.8rem;display:flex;justify-content:space-between;margin-top:0.35rem;">Procesadores N: <strong id="nVal">4</strong></label>
          <input id="nRange" type="range" min="1" max="32" value="4" style="width:100%;accent-color:#38bdf8;"/>
          <div class="w-stat-row">
            <div class="w-stat"><div class="v" id="spOut">2.50×</div><div class="k">Ganancia real</div></div>
            <div class="w-stat"><div class="v" id="spLim">5.00×</div><div class="k">Tope si N → ∞</div></div>
          </div>
        </div>
      </div>
    `;
    const bR = el.querySelector('#bRange'), nR = el.querySelector('#nRange');
    function upd() {
      const b = Number(bR.value) / 100, n = Number(nR.value);
      el.querySelector('#bVal').textContent = Math.round(b * 100) + '%';
      el.querySelector('#nVal').textContent = n;
      const sp = 1 / ((1 - b) + b / n);
      el.querySelector('#spOut').textContent = sp.toFixed(2) + '×';
      el.querySelector('#spLim').textContent = b === 1 ? '∞ (N)' : (1 / (1 - b)).toFixed(2) + '×';
    }
    bR.addEventListener('input', upd); nR.addEventListener('input', upd);
    upd();
  },

  /* 6. EDD #2 & #3 (Mar B3/B4): Simulador Visual de los 3 casos de ABB::remove */
  edd_abb_remove: function(el) {
    const states = [
      {
        title: 'Inicial: {50, 30, 70, 20, 40, 60, 80, 65}',
        desc: 'In-orden SIEMPRE ordenado: 20, 30, 40, 50, 60, 65, 70, 80.',
        svg: `
          <line x1="190" y1="25" x2="105" y2="68" stroke="#475569" stroke-width="2"/><line x1="190" y1="25" x2="275" y2="68" stroke="#475569" stroke-width="2"/>
          <line x1="105" y1="68" x2="60" y2="115" stroke="#475569" stroke-width="2"/><line x1="105" y1="68" x2="145" y2="115" stroke="#475569" stroke-width="2"/>
          <line x1="275" y1="68" x2="230" y2="115" stroke="#475569" stroke-width="2"/><line x1="275" y1="68" x2="320" y2="115" stroke="#475569" stroke-width="2"/>
          <line x1="230" y1="115" x2="255" y2="158" stroke="#475569" stroke-width="2"/>
          <circle cx="190" cy="25" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="190" y="29" fill="#fff" font-size="11" text-anchor="middle">50</text>
          <circle cx="105" cy="68" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="105" y="72" fill="#fff" font-size="11" text-anchor="middle">30</text>
          <circle cx="275" cy="68" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="275" y="72" fill="#fff" font-size="11" text-anchor="middle">70</text>
          <circle cx="60" cy="115" r="15" fill="#7f1d1d" stroke="#f87171" stroke-width="2"/><text x="60" y="119" fill="#fff" font-size="11" text-anchor="middle">20</text>
          <circle cx="145" cy="115" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="145" y="119" fill="#fff" font-size="11" text-anchor="middle">40</text>
          <circle cx="230" cy="115" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="230" y="119" fill="#fff" font-size="11" text-anchor="middle">60</text>
          <circle cx="320" cy="115" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="320" y="119" fill="#fff" font-size="11" text-anchor="middle">80</text>
          <circle cx="255" cy="158" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="255" y="162" fill="#fff" font-size="11" text-anchor="middle">65</text>
        `
      },
      {
        title: 'Paso 1: remove(20) — Caso Hoja (0 hijos)',
        desc: '20 no tiene hijos: el puntero left de 30 pasa a nullptr y hacemos delete del nodo 20.',
        svg: `
          <line x1="190" y1="25" x2="105" y2="68" stroke="#475569" stroke-width="2"/><line x1="190" y1="25" x2="275" y2="68" stroke="#475569" stroke-width="2"/>
          <line x1="105" y1="68" x2="145" y2="115" stroke="#475569" stroke-width="2"/>
          <line x1="275" y1="68" x2="230" y2="115" stroke="#475569" stroke-width="2"/><line x1="275" y1="68" x2="320" y2="115" stroke="#475569" stroke-width="2"/>
          <line x1="230" y1="115" x2="255" y2="158" stroke="#475569" stroke-width="2"/>
          <circle cx="190" cy="25" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="190" y="29" fill="#fff" font-size="11" text-anchor="middle">50</text>
          <circle cx="105" cy="68" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="105" y="72" fill="#fff" font-size="11" text-anchor="middle">30</text>
          <circle cx="275" cy="68" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="275" y="72" fill="#fff" font-size="11" text-anchor="middle">70</text>
          <circle cx="145" cy="115" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="145" y="119" fill="#fff" font-size="11" text-anchor="middle">40</text>
          <circle cx="230" cy="115" r="15" fill="#7f1d1d" stroke="#f87171" stroke-width="2"/><text x="230" y="119" fill="#fff" font-size="11" text-anchor="middle">60</text>
          <circle cx="320" cy="115" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="320" y="119" fill="#fff" font-size="11" text-anchor="middle">80</text>
          <circle cx="255" cy="158" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="255" y="162" fill="#fff" font-size="11" text-anchor="middle">65</text>
        `
      },
      {
        title: 'Paso 2: remove(60) — Caso 1 Hijo (tiene a 65)',
        desc: 'El padre (70) puentea directo a su nieto (65): 70->left = 65, y delete(60).',
        svg: `
          <line x1="190" y1="25" x2="105" y2="68" stroke="#475569" stroke-width="2"/><line x1="190" y1="25" x2="275" y2="68" stroke="#475569" stroke-width="2"/>
          <line x1="105" y1="68" x2="145" y2="115" stroke="#475569" stroke-width="2"/>
          <line x1="275" y1="68" x2="230" y2="115" stroke="#fbbf24" stroke-width="2.5"/><line x1="275" y1="68" x2="320" y2="115" stroke="#475569" stroke-width="2"/>
          <circle cx="190" cy="25" r="15" fill="#7f1d1d" stroke="#f87171" stroke-width="2"/><text x="190" y="29" fill="#fff" font-size="11" text-anchor="middle">50</text>
          <circle cx="105" cy="68" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="105" y="72" fill="#fff" font-size="11" text-anchor="middle">30</text>
          <circle cx="275" cy="68" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="275" y="72" fill="#fff" font-size="11" text-anchor="middle">70</text>
          <circle cx="145" cy="115" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="145" y="119" fill="#fff" font-size="11" text-anchor="middle">40</text>
          <circle cx="230" cy="115" r="15" fill="#065f46" stroke="#fbbf24" stroke-width="2"/><text x="230" y="119" fill="#fff" font-size="11" text-anchor="middle">65</text>
          <circle cx="320" cy="115" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="320" y="119" fill="#fff" font-size="11" text-anchor="middle">80</text>
        `
      },
      {
        title: 'Paso 3: remove(50) — Caso 2 Hijos (¡y es la Raíz!)',
        desc: 'Buscamos el menor del subárbol derecho (sucesor inorden = 65). 65 reemplaza a 50 y actualizamos root! Inorden final: 30 40 65 70 80.',
        svg: `
          <line x1="190" y1="25" x2="105" y2="68" stroke="#475569" stroke-width="2"/><line x1="190" y1="25" x2="275" y2="68" stroke="#475569" stroke-width="2"/>
          <line x1="105" y1="68" x2="145" y2="115" stroke="#475569" stroke-width="2"/>
          <line x1="275" y1="68" x2="320" y2="115" stroke="#475569" stroke-width="2"/>
          <circle cx="190" cy="25" r="15" fill="#065f46" stroke="#fbbf24" stroke-width="2.5"/><text x="190" y="29" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">65</text>
          <circle cx="105" cy="68" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="105" y="72" fill="#fff" font-size="11" text-anchor="middle">30</text>
          <circle cx="275" cy="68" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="275" y="72" fill="#fff" font-size="11" text-anchor="middle">70</text>
          <circle cx="145" cy="115" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="145" y="119" fill="#fff" font-size="11" text-anchor="middle">40</text>
          <circle cx="320" cy="115" r="15" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="320" y="119" fill="#fff" font-size="11" text-anchor="middle">80</text>
        `
      }
    ];
    el.innerHTML = `
      <div class="widget-box">
        <h4 style="margin:0 0 0.45rem;color:#34d399;">Traza Visual Paso a Paso del Enunciado Clase 07: Los 3 Casos de ABB::remove</h4>
        <div class="w-controls">
          ${states.map((_, i) => `<button class="w-btn ${i===0?'active':''}" data-i="${i}">${i===0?'Árbol Inicial':'Paso '+i}</button>`).join('')}
        </div>
        <div id="abbStTitle" style="font-weight:700;color:#fbbf24;font-size:0.9rem;margin-bottom:0.3rem;"></div>
        <svg id="abbSvg" viewBox="0 0 380 180" width="100%" style="max-height:220px;"></svg>
        <div id="abbStDesc" style="font-size:0.84rem;color:#cbd5e1;"></div>
      </div>
    `;
    function show(i) {
      el.querySelectorAll('.w-btn').forEach((b, idx) => b.classList.toggle('active', idx === i));
      el.querySelector('#abbStTitle').textContent = states[i].title;
      el.querySelector('#abbSvg').innerHTML = states[i].svg;
      el.querySelector('#abbStDesc').textContent = states[i].desc;
    }
    el.querySelectorAll('.w-btn').forEach(b => { b.onclick = () => show(Number(b.dataset.i)); });
    show(0);
  },

  /* 7. CD #2 (Mar B5): Círculos Concéntricos de Tipos de Datos + Selector de Gráficos */
  cd_visualizacion: function(el) {
    el.innerHTML = `
      <div class="grid-2">
        <div class="widget-box">
          <h4 style="margin:0 0 0.45rem;color:#a78bfa;">Círculos Concéntricos: Escalas de Datos (Cada círculo hereda al interior)</h4>
          <svg viewBox="0 0 320 210" width="100%" style="max-height:220px;">
            <circle cx="160" cy="108" r="96" fill="rgba(167,139,250,0.14)" stroke="#a78bfa" stroke-width="1.8"/>
            <text x="160" y="28" fill="#ddd6fe" font-size="10.5" font-weight="bold" text-anchor="middle">RAZÓN (Cero absoluto: ingresos, peso, edad)</text>
            <circle cx="160" cy="118" r="72" fill="rgba(56,189,248,0.15)" stroke="#38bdf8" stroke-width="1.8"/>
            <text x="160" y="60" fill="#bae6fd" font-size="10.5" font-weight="bold" text-anchor="middle">INTERVALO (Sin cero abs: °C, año calendario)</text>
            <circle cx="160" cy="128" r="48" fill="rgba(52,211,153,0.16)" stroke="#34d399" stroke-width="1.8"/>
            <text x="160" y="95" fill="#a7f3d0" font-size="10.5" font-weight="bold" text-anchor="middle">ORDINAL (Orden: Bajo/Medio)</text>
            <circle cx="160" cy="140" r="25" fill="rgba(251,191,36,0.22)" stroke="#fbbf24" stroke-width="1.8"/>
            <text x="160" y="143" fill="#fde68a" font-size="10" font-weight="bold" text-anchor="middle">NOMINAL</text>
          </svg>
        </div>
        <div class="widget-box">
          <h4 style="margin:0 0 0.45rem;color:#38bdf8;">Selector Rápido de Gráfico (Clase 04)</h4>
          <div class="w-controls" id="vizBtns">
            <button class="w-btn active" data-v="1dcat">1 Categórica</button>
            <button class="w-btn" data-v="1dnum">1 Continua</button>
            <button class="w-btn" data-v="2dnum">2 Continuas</button>
            <button class="w-btn" data-v="catnum">Cat + Numérica</button>
            <button class="w-btn" data-v="3d">2 Num + 1 Cat</button>
          </div>
          <div id="vizOut" style="background:#1e293b;padding:0.8rem;border-radius:8px;font-size:0.86rem;"></div>
        </div>
      </div>
    `;
    const map = {
      '1dcat': '✅ <strong>Gráfico de Barras (Bar chart):</strong> mucho más informativo que el de torta.<br/>❌ <strong>Error clásico:</strong> unir barras nominales con líneas o usar torta con muchas categorías.',
      '1dnum': '✅ <strong>Histograma:</strong> agrupa en intervalos (bins) contiguos para ver forma, simetría y sesgo.',
      '2dnum': '✅ <strong>Scatter plot (dispersión)</strong> o <strong>Densidad 2D / Heatmap</strong> si hay miles de puntos superpuestos. Si una es tiempo: <strong>Line plot</strong>.',
      'catnum': '✅ <strong>Boxplot (Cajas y bigotes)</strong> para ver mediana, IQR y outliers, o <strong>Violin plot</strong> para ver además la densidad multimodal.',
      '3d': '✅ <strong>Scatter plot con color por categoría (Color scatter)</strong> o <strong>Bubble plot</strong> (pregunta clásica de la Formativa: Horas vs Nota por Carrera).'
    };
    const out = el.querySelector('#vizOut');
    el.querySelectorAll('#vizBtns button').forEach(b => {
      b.onclick = () => {
        el.querySelectorAll('#vizBtns button').forEach(x => x.classList.remove('active'));
        b.classList.add('active');
        out.innerHTML = map[b.dataset.v];
      };
    });
    out.innerHTML = map['1dcat'];
  },

  /* 8. EDD #4 & #5 (Mié B1 & B2): Visor de las 4 Rotaciones AVL (LL, RR, LR, RL) */
  edd_avl_rotaciones: function(el) {
    const cases = {
      LL: {
        t: 'Caso LL: FB(Z) = +2 y FB(Y) ≥ 0 → Rotación Simple Derecha(Z)',
        d: 'Desbalance izquierda-izquierda. Y sube como nueva raíz, Z baja a la derecha de Y, y el subárbol derecho de Y (T2) pasa a ser izquierdo de Z. ¡Actualiza altura(Z) ANTES que altura(Y)!',
        b: '      (30) FB=+2\n      /\n    (20) FB=+1\n    /\n  (10)',
        a: '      (20) FB=0\n     /    \\\n  (10)    (30)'
      },
      RR: {
        t: 'Caso RR: FB(Z) = −2 y FB(Y) ≤ 0 → Rotación Simple Izquierda(Z)',
        d: 'Espejo exacto de LL (insertaste 10, 20, 30). Y(20) sube, Z(10) baja a la izquierda.',
        b: '  (10) FB=-2\n     \\\n     (20) FB=-1\n        \\\n        (30)',
        a: '      (20) FB=0\n     /    \\\n  (10)    (30)'
      },
      LR: {
        t: 'Caso LR: FB(Z) = +2 y FB(Y) = −1 → Doble: rotIzq(Z->izq) + rotDer(Z)',
        d: 'Zig-zag izquierda-derecha (ej. 30, 10, 20). Primero enderezas el hijo con rotIzq(10) convirtiéndolo en LL, y luego aplicas rotDer(30). ¡El nieto X(20) termina arriba!',
        b: '      (30) FB=+2\n      /\n   (10) FB=-1\n      \\\n      (20)',
        a: '      (20) FB=0\n     /    \\\n  (10)    (30)'
      },
      RL: {
        t: 'Caso RL: FB(Z) = −2 y FB(Y) = +1 → Doble: rotDer(Z->der) + rotIzq(Z)',
        d: 'Zig-zag derecha-izquierda (ej. 10, 30, 20). Primero rotDer(30) y luego rotIzq(10). ¡El nieto X(20) termina arriba!',
        b: '   (10) FB=-2\n      \\\n      (30) FB=+1\n      /\n    (20)',
        a: '      (20) FB=0\n     /    \\\n  (10)    (30)'
      }
    };
    el.innerHTML = `
      <div class="widget-box">
        <h4 style="margin:0 0 0.45rem;color:#34d399;">Simulador de las 4 Rotaciones AVL (LL, RR, LR, RL)</h4>
        <div class="w-controls">
          <button class="w-btn active" data-c="LL">Caso LL (Simple Der)</button>
          <button class="w-btn" data-c="RR">Caso RR (Simple Izq)</button>
          <button class="w-btn" data-c="LR">Caso LR (Doble Izq-Der)</button>
          <button class="w-btn" data-c="RL">Caso RL (Doble Der-Izq)</button>
        </div>
        <div id="avlTitle" style="font-weight:700;color:#fbbf24;font-size:0.9rem;margin:0.4rem 0;"></div>
        <div class="grid-2">
          <div><div style="font-size:0.76rem;color:#f87171;font-weight:700;">ANTES (Desbalanceado)</div><pre class="code-box" id="avlBefore"></pre></div>
          <div><div style="font-size:0.76rem;color:#34d399;font-weight:700;">DESPUÉS (Balanceado O(log n))</div><pre class="code-box" id="avlAfter"></pre></div>
        </div>
        <div id="avlDesc" style="font-size:0.84rem;color:#cbd5e1;margin-top:0.35rem;"></div>
      </div>
    `;
    function show(c) {
      el.querySelectorAll('.w-btn').forEach(b => b.classList.toggle('active', b.dataset.c === c));
      el.querySelector('#avlTitle').textContent = cases[c].t;
      el.querySelector('#avlBefore').textContent = cases[c].b;
      el.querySelector('#avlAfter').textContent = cases[c].a;
      el.querySelector('#avlDesc').textContent = cases[c].d;
    }
    el.querySelectorAll('.w-btn').forEach(b => { b.onclick = () => show(b.dataset.c); });
    show('LL');
  },

  /* 9. CD #3 (Mié B3): Descenso del Gradiente + Círculo Ridge vs Rombo Lasso */
  cd_regresion: function(el) {
    el.innerHTML = `
      <div class="grid-2">
        <div class="widget-box">
          <h4 style="margin:0 0 0.45rem;color:#a78bfa;">Efecto de la Tasa de Aprendizaje α en Descenso del Gradiente</h4>
          <svg viewBox="0 0 340 155" width="100%">
            <path d="M 30 20 Q 170 250 310 20" fill="none" stroke="#64748b" stroke-width="2.5"/>
            <circle cx="170" cy="135" r="5" fill="#34d399"/>
            <text x="170" y="150" fill="#34d399" font-size="9.5" text-anchor="middle">Mínimo ECM</text>
            <path id="gdTrace" fill="none" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,3"/>
          </svg>
          <div class="w-controls" id="gdBtns">
            <button class="w-btn" data-g="low">α muy pequeño</button>
            <button class="w-btn active" data-g="ok">α adecuado</button>
            <button class="w-btn" data-g="high">α muy grande (diverge)</button>
          </div>
          <div id="gdTxt" style="font-size:0.82rem;color:#cbd5e1;"></div>
        </div>

        <div class="widget-box">
          <h4 style="margin:0 0 0.45rem;color:#38bdf8;">Por qué Lasso hace w = 0 y Ridge NO (Geometría L1 vs L2)</h4>
          <svg viewBox="0 0 340 165" width="100%">
            <!-- Ridge Circle -->
            <line x1="85" y1="15" x2="85" y2="150" stroke="#475569"/><line x1="20" y1="95" x2="150" y2="95" stroke="#475569"/>
            <circle cx="85" cy="95" r="36" fill="rgba(56,189,248,0.18)" stroke="#38bdf8" stroke-width="2"/>
            <ellipse cx="122" cy="45" rx="34" ry="20" transform="rotate(-25 122 45)" fill="none" stroke="#fbbf24" stroke-width="1.5"/>
            <circle cx="104" cy="64" r="4.5" fill="#f87171"/>
            <text x="85" y="160" fill="#bae6fd" font-size="10" font-weight="bold" text-anchor="middle">RIDGE (L2 = w²) → w₁≠0, w₂≠0</text>

            <!-- Lasso Diamond -->
            <line x1="255" y1="15" x2="255" y2="150" stroke="#475569"/><line x1="190" y1="95" x2="320" y2="95" stroke="#475569"/>
            <polygon points="255,55 295,95 255,135 215,95" fill="rgba(52,211,153,0.18)" stroke="#34d399" stroke-width="2"/>
            <ellipse cx="288" cy="42" rx="36" ry="20" transform="rotate(-25 288 42)" fill="none" stroke="#fbbf24" stroke-width="1.5"/>
            <circle cx="255" cy="55" r="5" fill="#f87171"/>
            <text x="255" y="160" fill="#a7f3d0" font-size="10" font-weight="bold" text-anchor="middle">LASSO (L1 = |w|) → ¡Esquina w₁=0!</text>
          </svg>
          <div style="font-size:0.8rem;color:#94a3b8;">El rombo de Lasso tiene puntas sobre los ejes: la curva de pérdida choca en la esquina y anula variables irrelevantes (selección automática).</div>
        </div>
      </div>
    `;
    const gdInfo = {
      low:  { p: 'M 48,45 L 62,64 L 76,81 L 90,95 L 104,106', t: 'α muy pequeño: avanza con pasos diminutos; tarda demasiadas iteraciones en converger.' },
      ok:   { p: 'M 48,45 L 95,98 L 138,126 L 165,134 L 170,135', t: 'α adecuado: desciende suave y directo hasta el mínimo global del ECM.' },
      high: { p: 'M 65,68 L 285,50 L 38,32 L 305,24', t: 'α muy grande: rebota de un lado al otro del valle y el error EXPLOTA (diverge).' }
    };
    function setGd(k) {
      el.querySelectorAll('#gdBtns button').forEach(b => b.classList.toggle('active', b.dataset.g === k));
      el.querySelector('#gdTrace').setAttribute('d', gdInfo[k].p);
      el.querySelector('#gdTxt').textContent = gdInfo[k].t;
    }
    el.querySelectorAll('#gdBtns button').forEach(b => { b.onclick = () => setGd(b.dataset.g); });
    setGd('ok');
  },

  /* 10. EDD #6 (Jue B1): Quiz Interactivo Oficial Simulacro Parte 1 (8 preguntas) */
  edd_simulacro_quiz: function(el) {
    const qs = [
      { q: '1. Árbol binario de altura K = 5 (raíz = nivel 1): ¿máx nodos en nivel 4 y máx nodos totales?', opts: ['8 y 31', '16 y 32', '8 y 32', '16 y 31'], ans: 0, exp: 'Nivel i: 2^(i-1) = 2^3 = 8. Totales: 2^K - 1 = 31.' },
      { q: '2. ¿Qué recorrido libera nodos dinámicos sin perder punteros a los hijos?', opts: ['Pre-orden', 'In-orden', 'Post-orden', 'Por nivel sin cola'], ans: 2, exp: 'Post-orden: borra Izq, luego Der y al final el Padre.' },
      { q: '3. Dos árboles con las mismas claves {10,20,30,40} pero distinta altura son:', opts: ['Isomorfos', 'Semejantes', 'Llenos', 'Completos'], ans: 1, exp: 'Mismos valores con distinta forma = Semejantes (misma forma = Isomorfos).' },
      { q: '4. Arreglo base 1: [-, A, B, C, D, E, F]. ¿Padre de F(6) e hijo izq de C(3)?', opts: ['Padre C; izq de C es F', 'Padre B; izq E', 'Padre C; sin izq', 'Padre A; izq F'], ans: 0, exp: 'Padre(6) = 6/2 = 3 (C). Izq(3) = 2*3 = 6 (F).' },
      { q: '5. Enhebrado In-orden: si X tiene rightThread == true y right == Y, ¿qué es Y?', opts: ['Hijo derecho real', 'Predecesor inorden', 'Sucesor inorden', 'Padre directo'], ans: 2, exp: 'rightThread == true apunta siempre al sucesor In-orden.' },
      { q: '6. En ABB::remove con 2 hijos, el sucesor inorden S (menor del subárbol derecho) cumple:', opts: ['Siempre es hoja', 'S->left == nullptr, pero puede tener hijo derecho', 'S->right == nullptr', 'Tiene 2 hijos'], ans: 1, exp: 'Si tuviera hijo izquierdo no sería el menor; sí puede tener hijo derecho (hay que reconectarlo!).' },
      { q: '7. En AVL, si FB(Z) = +2 y FB(Z.izq) = −1, corresponde rotación:', opts: ['LL', 'RR', 'LR', 'RL'], ans: 2, exp: 'Signos distintos (+2 y -1) = rotación doble Izquierda-Derecha (LR).' },
      { q: '8. Peor caso de búsqueda en ABB simple vs AVL:', opts: ['O(log n) y O(log n)', 'O(n) y O(log n)', 'O(n log n) y O(n)', 'O(1) y O(log n)'], ans: 1, exp: 'Un ABB degenerado en lista cae a O(n); el AVL garantiza O(log n) siempre.' }
    ];
    el.innerHTML = `<div class="widget-box"><h4 style="margin:0 0 0.6rem;color:#34d399;">Autotest Interactivo: Las 8 Preguntas Oficiales del Simulacro (16 pts)</h4><div id="simQList"></div></div>`;
    const wrap = el.querySelector('#simQList');
    qs.forEach((item, qi) => {
      const d = document.createElement('div');
      d.style.cssText = 'margin-bottom:0.75rem;padding-bottom:0.65rem;border-bottom:1px solid #1e293b;';
      d.innerHTML = `<div style="font-size:0.86rem;font-weight:600;margin-bottom:0.35rem;">${item.q}</div>
        <div class="w-controls">${item.opts.map((o, oi) => `<button class="w-btn" data-oi="${oi}">${o}</button>`).join('')}</div>
        <div class="q-fb" style="font-size:0.8rem;margin-top:0.25rem;"></div>`;
      d.querySelectorAll('button').forEach(b => {
        b.onclick = () => {
          const oi = Number(b.dataset.oi);
          const fb = d.querySelector('.q-fb');
          if (oi === item.ans) {
            fb.style.color = '#34d399';
            fb.textContent = '✅ ¡Correcto! ' + item.exp;
          } else {
            fb.style.color = '#f87171';
            fb.textContent = '❌ Revisa: ' + item.exp;
          }
        };
      });
      wrap.appendChild(d);
    });
  },

  /* 11. CD #4 (Vie B1): Sigmoide + Calculadora de Ejercicios p.50 y p.51 Clase 06 */
  cd_clasificacion: function(el) {
    el.innerHTML = `
      <div class="grid-2">
        <div class="widget-box">
          <h4 style="margin:0 0 0.45rem;color:#a78bfa;">Curva Sigmoide (Regresión Logística) y Umbral</h4>
          <svg viewBox="0 0 340 145" width="100%">
            <line x1="30" y1="125" x2="320" y2="125" stroke="#475569"/>
            <line x1="175" y1="15" x2="175" y2="125" stroke="#475569" stroke-dasharray="3,3"/>
            <line x1="30" y1="70" x2="320" y2="70" stroke="#fbbf24" stroke-dasharray="4,3"/>
            <text x="38" y="65" fill="#fbbf24" font-size="9.5">Umbral P = 0.5</text>
            <path d="M 35 123 C 115 123, 135 120, 175 70 C 215 20, 235 17, 315 17" fill="none" stroke="#a78bfa" stroke-width="3"/>
            <circle id="sigDot" cx="175" cy="70" r="5.5" fill="#34d399"/>
          </svg>
          <label style="font-size:0.8rem;display:flex;justify-content:space-between;">Combinación lineal z = b + w·x: <strong id="zVal">0.0</strong></label>
          <input id="zRange" type="range" min="-60" max="60" value="0" style="width:100%;accent-color:#a78bfa;"/>
          <div id="sigOut" style="font-size:0.84rem;color:#e2e8f0;margin-top:0.35rem;"></div>
        </div>

        <div class="widget-box">
          <h4 style="margin:0 0 0.45rem;color:#38bdf8;">Ejercicios Reales Clase 06 (Diapositivas 50 y 51)</h4>
          <div class="w-controls" id="cmPresets">
            <button class="w-btn active" data-p="ej1">Ejercicio 1 (Balanceado)</button>
            <button class="w-btn" data-p="ej2">Ejercicio 2 (Desbalanceado!)</button>
          </div>
          <div id="cmTableOut"></div>
        </div>
      </div>
    `;
    const zR = el.querySelector('#zRange');
    function updSig() {
      const z = Number(zR.value) / 10;
      const p = 1 / (1 + Math.exp(-z));
      el.querySelector('#zVal').textContent = z.toFixed(1);
      const cx = 175 + (z / 6) * 140;
      const cy = 123 - p * 106;
      el.querySelector('#sigDot').setAttribute('cx', cx.toFixed(1));
      el.querySelector('#sigDot').setAttribute('cy', cy.toFixed(1));
      el.querySelector('#sigOut').innerHTML = `Probabilidad <code>σ(z) = ${(p*100).toFixed(1)}%</code> → Predicción (umbral 0.5): <strong style="color:${p>=0.5?'#34d399':'#f87171'}">Clase ${p>=0.5?1:0}</strong>`;
    }
    zR.addEventListener('input', updSig); updSig();

    const presets = {
      ej1: { tp: 23, fp: 5, fn: 1, tn: 42, note: 'Caso sano: alto Accuracy y buen F1.' },
      ej2: { tp: 23, fp: 10, fn: 11, tn: 242, note: '¡Trampa de prueba! Hay 252 negativos: el Accuracy sube a 92.7%, pero Precision cae a 69.7% y Recall a 67.6%. ¡En desbalanceo NO confíes solo en Accuracy!' }
    };
    function showCM(k) {
      el.querySelectorAll('#cmPresets button').forEach(b => b.classList.toggle('active', b.dataset.p === k));
      const { tp, fp, fn, tn, note } = presets[k];
      const tot = tp + fp + fn + tn;
      const acc = (tp + tn) / tot, prec = tp / (tp + fp), rec = tp / (tp + fn);
      const f1 = 2 * prec * rec / (prec + rec);
      el.querySelector('#cmTableOut').innerHTML = `
        <table class="clean-tbl">
          <tr><th></th><th>Real = 1</th><th>Real = 0</th></tr>
          <tr><th>Pred = 1</th><td>TP = <strong>${tp}</strong></td><td>FP = <strong>${fp}</strong></td></tr>
          <tr><th>Pred = 0</th><td>FN = <strong>${fn}</strong></td><td>TN = <strong>${tn}</strong></td></tr>
        </table>
        <div class="w-stat-row">
          <div class="w-stat"><div class="v">${(acc*100).toFixed(1)}%</div><div class="k">Accuracy</div></div>
          <div class="w-stat"><div class="v">${(prec*100).toFixed(1)}%</div><div class="k">Precision</div></div>
          <div class="w-stat"><div class="v">${(rec*100).toFixed(1)}%</div><div class="k">Recall</div></div>
          <div class="w-stat"><div class="v">${f1.toFixed(3)}</div><div class="k">F1-Score</div></div>
        </div>
        <div style="font-size:0.8rem;color:#fde68a;margin-top:0.45rem;">${note}</div>
      `;
    }
    el.querySelectorAll('#cmPresets button').forEach(b => { b.onclick = () => showCM(b.dataset.p); });
    showCM('ej1');
  },

  /* 12. CD #5 (Vie B2): Dianas Circulares Sesgo-Varianza + Esquema k-Fold CV */
  cd_evaluacion: function(el) {
    el.innerHTML = `
      <div class="grid-2">
        <div class="widget-box">
          <h4 style="margin:0 0 0.45rem;color:#a78bfa;">Dianas Circulares: Sesgo (Bias) vs. Varianza</h4>
          <div class="grid-2" style="gap:0.6rem;">
            <div style="text-align:center;background:#1e293b;padding:0.5rem;border-radius:8px;">
              <svg viewBox="0 0 100 100" width="84"><circle cx="50" cy="50" r="42" fill="none" stroke="#475569"/><circle cx="50" cy="50" r="24" fill="none" stroke="#475569"/><circle cx="50" cy="50" r="8" fill="#ef4444"/><circle cx="48" cy="49" r="3" fill="#38bdf8"/><circle cx="53" cy="51" r="3" fill="#38bdf8"/><circle cx="50" cy="46" r="3" fill="#38bdf8"/></svg>
              <div style="font-size:0.76rem;"><strong>Bajo Sesgo · Baja Varianza</strong><br/><span style="color:#34d399">Ideal</span></div>
            </div>
            <div style="text-align:center;background:#1e293b;padding:0.5rem;border-radius:8px;">
              <svg viewBox="0 0 100 100" width="84"><circle cx="50" cy="50" r="42" fill="none" stroke="#475569"/><circle cx="50" cy="50" r="24" fill="none" stroke="#475569"/><circle cx="50" cy="50" r="8" fill="#ef4444"/><circle cx="24" cy="26" r="3" fill="#fbbf24"/><circle cx="28" cy="23" r="3" fill="#fbbf24"/><circle cx="22" cy="30" r="3" fill="#fbbf24"/></svg>
              <div style="font-size:0.76rem;"><strong>Alto Sesgo · Baja Varianza</strong><br/><span style="color:#fbbf24">Underfitting (modelo muy simple)</span></div>
            </div>
            <div style="text-align:center;background:#1e293b;padding:0.5rem;border-radius:8px;">
              <svg viewBox="0 0 100 100" width="84"><circle cx="50" cy="50" r="42" fill="none" stroke="#475569"/><circle cx="50" cy="50" r="24" fill="none" stroke="#475569"/><circle cx="50" cy="50" r="8" fill="#ef4444"/><circle cx="26" cy="40" r="3" fill="#f87171"/><circle cx="72" cy="32" r="3" fill="#f87171"/><circle cx="56" cy="76" r="3" fill="#f87171"/><circle cx="38" cy="68" r="3" fill="#f87171"/></svg>
              <div style="font-size:0.76rem;"><strong>Bajo Sesgo · Alta Varianza</strong><br/><span style="color:#f87171">Overfitting (memoriza ruido)</span></div>
            </div>
            <div style="text-align:center;background:#1e293b;padding:0.5rem;border-radius:8px;">
              <svg viewBox="0 0 100 100" width="84"><circle cx="50" cy="50" r="42" fill="none" stroke="#475569"/><circle cx="50" cy="50" r="24" fill="none" stroke="#475569"/><circle cx="50" cy="50" r="8" fill="#ef4444"/><circle cx="16" cy="20" r="3" fill="#94a3b8"/><circle cx="80" cy="18" r="3" fill="#94a3b8"/><circle cx="82" cy="78" r="3" fill="#94a3b8"/></svg>
              <div style="font-size:0.76rem;"><strong>Alto Sesgo · Alta Varianza</strong><br/><span style="color:#94a3b8">Peor escenario</span></div>
            </div>
          </div>
        </div>

        <div class="widget-box">
          <h4 style="margin:0 0 0.45rem;color:#34d399;">Esquema Visual 5-Fold Cross-Validation</h4>
          <p style="font-size:0.8rem;color:#94a3b8;margin:0 0 0.45rem;">Todos los bloques actúan 1 vez como Validación (amarillo) y 4 veces como Entrenamiento (azul). Luego se promedian las 5 métricas:</p>
          ${[0,1,2,3,4].map(r => `
            <div style="display:flex;gap:4px;margin-bottom:5px;align-items:center;">
              <span style="font-size:0.74rem;width:54px;color:#94a3b8;">Iter ${r+1}:</span>
              ${[0,1,2,3,4].map(c => `<div style="flex:1;text-align:center;font-size:0.72rem;padding:4px 0;border-radius:4px;background:${r===c?'rgba(251,191,36,0.28)':'rgba(56,189,248,0.18)'};border:1px solid ${r===c?'#fbbf24':'#38bdf8'};color:#fff;">${r===c?'VAL':'Train'}</div>`).join('')}
            </div>
          `).join('')}
          <div style="font-size:0.79rem;color:#fde68a;margin-top:0.45rem;">Ojo de cátedra: CV NO aprende un modelo final, evalúa qué tan bien generaliza un método/hiperparámetro.</div>
        </div>
      </div>
    `;
  },

  /* 13. CD #6 (Vie B3): Calculadora Interactiva Gini vs Entropía (Clase 08) */
  cd_arboles_gini: function(el) {
    el.innerHTML = `
      <div class="widget-box">
        <h4 style="margin:0 0 0.45rem;color:#a78bfa;">Calculadora Visual en Vivo: Impureza Gini vs. Entropía (Nodo Binario Clase A / Clase B)</h4>
        <label style="font-size:0.84rem;display:flex;justify-content:space-between;">Proporción Clase A (p₁): <strong id="p1Lbl">70% (Ejercicio pág. 29 de Clase 08)</strong></label>
        <input id="p1Range" type="range" min="0" max="100" value="70" style="width:100%;accent-color:#a78bfa;"/>
        <div class="w-stat-row">
          <div class="w-stat"><div class="v" id="giniVal">0.420</div><div class="k">Gini = 1 − (p₁² + p₂²)</div></div>
          <div class="w-stat"><div class="v" id="entVal">0.881</div><div class="k">Entropía (bits, máx 1.0)</div></div>
          <div class="w-stat"><div class="v" id="nodeSt">Impuro medio</div><div class="k">Pureza del nodo</div></div>
        </div>
        <div style="font-size:0.8rem;color:#94a3b8;margin-top:0.5rem;">
          Prueba poner <strong>100%</strong> (nodo puro → Gini = <code>0</code>, Ejercicio p.28), <strong>50%</strong> (máximo desorden → Gini = <code>0.50</code>, Entropía = <code>1.0</code>) y <strong>70%</strong> (Gini = <code>1 - (0.49 + 0.09) = 0.42</code>, Ejercicio p.29!).
        </div>
      </div>
    `;
    const r = el.querySelector('#p1Range');
    function upd() {
      const p1 = Number(r.value) / 100, p2 = 1 - p1;
      el.querySelector('#p1Lbl').textContent = `${Math.round(p1*100)}% Clase A  |  ${Math.round(p2*100)}% Clase B`;
      const gini = 1 - (p1*p1 + p2*p2);
      const ent = (p1 === 0 || p2 === 0) ? 0 : -(p1 * Math.log2(p1) + p2 * Math.log2(p2));
      el.querySelector('#giniVal').textContent = gini.toFixed(3);
      el.querySelector('#entVal').textContent = ent.toFixed(3);
      el.querySelector('#nodeSt').textContent = gini === 0 ? '¡100% Puro!' : (gini > 0.45 ? 'Máxima mezcla' : 'Parcialmente puro');
    }
    r.addEventListener('input', upd); upd();
  },

  /* 14. CIBER #1 (Vie B4): Embudo Visual SIEM (X.816 / Wazuh) + Círculos del SOC */
  ciber_siem_soc: function(el) {
    el.innerHTML = `
      <div class="grid-2">
        <div class="widget-box">
          <h4 style="margin:0 0 0.5rem;color:#fbbf24;">Embudo Visual: Del Evento al SIEM (RFC 4949 / X.816 / Wazuh)</h4>
          <div class="flow-row" style="flex-direction:column;gap:0.4rem;">
            <div class="flow-node" style="width:100%;border-color:#38bdf8;"><strong>1. Los 4 Niveles de Rastro</strong><span>Sistema · Aplicación · Usuario · Físico (tarjetas/alarmas)</span></div>
            <div class="flow-arrow">⬇ Captura (Logging: Windows Event Log / Syslog UNIX)</div>
            <div class="flow-node" style="width:88%;border-color:#a78bfa;"><strong>2. Centralización y Almacenamiento</strong><span>Servidor SIEM dedicado (ej. Wazuh) evita que un atacante borre logs locales</span></div>
            <div class="flow-arrow">⬇ Análisis (NIST SP 800-92)</div>
            <div class="flow-node" style="width:74%;border-color:#34d399;"><strong>3. Detección: Reglas + Línea Base + Anomalías</strong><span>Correlaciona miles de eventos sueltos → genera Alerta accionable</span></div>
          </div>
        </div>

        <div class="widget-box">
          <h4 style="margin:0 0 0.5rem;color:#38bdf8;">Círculos Operativos de un SOC Maduro</h4>
          <div class="circle-row">
            <div class="circle-badge" style="border-color:#38bdf8;"><strong>Tier 1 · Triage</strong><span>Monitorea SIEM 24/7, filtra falsos positivos</span></div>
            <div class="circle-badge" style="border-color:#fbbf24;"><strong>Tier 2 · Respuesta</strong><span>Investiga incidente, contiene y analiza alcance</span></div>
            <div class="circle-badge" style="border-color:#34d399;"><strong>Tier 3 / CTAC</strong><span>Threat hunting proactivo, forense y CERT/CSIRT</span></div>
          </div>
          <div style="font-size:0.8rem;color:#94a3b8;text-align:center;">Pieza central de software del SOC = <strong>SIEM</strong> + escáner de vulnerabilidades + tickets de incidentes.</div>
        </div>
      </div>
    `;
  },

  /* 15. CIBER #2 (Vie B5): Plano Interactivo Zero Trust (PE / PA / PEP) vs Castillo */
  ciber_zta: function(el) {
    el.innerHTML = `
      <div class="widget-box">
        <h4 style="margin:0 0 0.45rem;color:#fbbf24;">Comparador Arquitectónico: Firewall Perimetral ("Castillo") vs. Zero Trust (NIST / Syed et al.)</h4>
        <div class="w-controls" id="ztaTabs">
          <button class="w-btn" data-z="old">Modelo Antiguo (Castillo)</button>
          <button class="w-btn active" data-z="zta">Arquitectura Zero Trust (PE → PA → PEP)</button>
          <button class="w-btn" data-z="ac">Control de Acceso (RBAC vs ABAC)</button>
        </div>
        <div id="ztaView" style="margin-top:0.5rem;"></div>
      </div>
    `;
    const views = {
      old: `
        <div style="background:#1e293b;padding:0.9rem;border-radius:10px;border-left:4px solid #f87171;font-size:0.86rem;">
          <strong>Problema del Perímetro Tradicional:</strong> Todo afuera es <em>Untrusted</em>, pero una vez que alguien cruza el firewall/VPN hacia la red interna (<em>Trusted</em>), tiene confianza implícita y puede hacer <strong>movimiento lateral</strong> libre entre servidores.
        </div>`,
      zta: `
        <svg viewBox="0 0 680 165" width="100%" style="min-width:520px;">
          <!-- Plano de Control -->
          <rect x="210" y="8" width="260" height="58" rx="9" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
          <text x="340" y="27" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">PLANO DE CONTROL (Cerebro)</text>
          <text x="340" y="48" fill="#fff" font-size="11" text-anchor="middle">PE (Policy Engine)  ➔  PA (Policy Admin)</text>

          <!-- Plano de Datos -->
          <rect x="15" y="96" width="145" height="55" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.8"/>
          <text x="87" y="120" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">Sujeto + Dispositivo</text>
          <text x="87" y="136" fill="#94a3b8" font-size="9.5" text-anchor="middle">Auth Continua + Contexto</text>

          <rect x="255" y="96" width="170" height="55" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
          <text x="340" y="120" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle">PEP (Guardia / Compuerta)</text>
          <text x="340" y="136" fill="#cbd5e1" font-size="9.5" text-anchor="middle">Policy Enforcement Point</text>

          <rect x="515" y="96" width="150" height="55" rx="8" fill="#0f172a" stroke="#a78bfa" stroke-width="1.8"/>
          <text x="590" y="120" fill="#ddd6fe" font-size="11" font-weight="bold" text-anchor="middle">Microsegmento</text>
          <text x="590" y="136" fill="#94a3b8" font-size="9.5" text-anchor="middle">Solo 1 app/recurso puntual</text>

          <line x1="160" y1="123" x2="255" y2="123" stroke="#38bdf8" stroke-width="2.5"/>
          <line x1="425" y1="123" x2="515" y2="123" stroke="#34d399" stroke-width="2.5"/>
          <line x1="340" y1="66" x2="340" y2="96" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,3"/>
        </svg>
        <div style="font-size:0.82rem;color:#cbd5e1;"><strong>Regla de oro ZTA:</strong> "Nunca confiar, siempre verificar" por sesión. <strong>PE</strong> calcula confianza (SIEM, postura, hora, rol), <strong>PA</strong> emite el token/canal y <strong>PEP</strong> abre paso únicamente a ese microsegmento.</div>`,
      ac: `
        <table class="clean-tbl">
          <tr><th>Modelo</th><th>En qué se basa</th><th>Ejemplo práctico</th></tr>
          <tr><td><strong>IBAC</strong></td><td>Identidad individual</td><td>Lista puntual: "solo juan@empresa.cl lee este archivo".</td></tr>
          <tr><td><strong>RBAC</strong></td><td>Rol en la organización</td><td>"Rol Contador accede al ERP" (rígido si cambia el contexto).</td></tr>
          <tr><td><strong>ABAC</strong></td><td>Atributos combinados (usuario + equipo + hora + lugar)</td><td>"Contador + laptop corporativo sano + desde Chile + horario hábil".</td></tr>
          <tr><td><strong>RbAC</strong></td><td>Puntaje dinámico de riesgo</td><td>Si sube el riesgo de inicio de sesión en Entra ID, pide MFA o bloquea.</td></tr>
        </table>`
    };
    const out = el.querySelector('#ztaView');
    el.querySelectorAll('#ztaTabs button').forEach(b => {
      b.onclick = () => {
        el.querySelectorAll('#ztaTabs button').forEach(x => x.classList.remove('active'));
        b.classList.add('active');
        out.innerHTML = views[b.dataset.z];
      };
    });
    out.innerHTML = views.zta;
  },

  /* 16. CD #7 (Sáb B1): Simulador Feedforward y Backpropagation (Clase 09) */
  cd_redes: function(el) {
    el.innerHTML = `
      <div class="widget-box">
        <h4 style="margin:0 0 0.45rem;color:#a78bfa;">Visualizador Red Multicapa (2 Entradas → 2 Ocultas → 1 Salida): Feedforward vs. Backpropagation</h4>
        <svg viewBox="0 0 540 165" width="100%">
          <line x1="85" y1="45" x2="255" y2="45" stroke="#475569" stroke-width="2"/>
          <line x1="85" y1="45" x2="255" y2="120" stroke="#475569" stroke-width="2"/>
          <line x1="85" y1="120" x2="255" y2="45" stroke="#475569" stroke-width="2"/>
          <line x1="85" y1="120" x2="255" y2="120" stroke="#475569" stroke-width="2"/>
          <line x1="255" y1="45" x2="435" y2="82" stroke="#38bdf8" stroke-width="2.5"/>
          <line x1="255" y1="120" x2="435" y2="82" stroke="#38bdf8" stroke-width="2.5"/>

          <circle cx="85" cy="45" r="20" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="85" y="49" fill="#fff" font-size="11" text-anchor="middle">x₁</text>
          <circle cx="85" cy="120" r="20" fill="#1e293b" stroke="#34d399" stroke-width="2"/><text x="85" y="124" fill="#fff" font-size="11" text-anchor="middle">x₂</text>

          <circle cx="255" cy="45" r="22" fill="#1e293b" stroke="#a78bfa" stroke-width="2"/><text x="255" y="49" fill="#fff" font-size="10.5" text-anchor="middle">h₁=f(Σ)</text>
          <circle cx="255" cy="120" r="22" fill="#1e293b" stroke="#a78bfa" stroke-width="2"/><text x="255" y="124" fill="#fff" font-size="10.5" text-anchor="middle">h₂=f(Σ)</text>

          <circle cx="435" cy="82" r="23" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/><text x="435" y="86" fill="#fff" font-size="11" text-anchor="middle">ŷ</text>

          <text x="165" y="34" fill="#94a3b8" font-size="9.5">w₁..w₄</text>
          <text x="350" y="55" fill="#38bdf8" font-size="10.5" font-weight="bold">w₅</text>
          <text x="350" y="116" fill="#38bdf8" font-size="10.5" font-weight="bold">w₆</text>
        </svg>
        <div class="w-controls" id="nnSteps">
          <button class="w-btn active" data-s="0">1. Por qué falla el Perceptrón (XOR)</button>
          <button class="w-btn" data-s="1">2. Paso Feedforward ( → )</button>
          <button class="w-btn" data-s="2">3. Paso Backpropagation ( ← )</button>
        </div>
        <div id="nnTxt" style="background:#1e293b;padding:0.75rem;border-radius:8px;font-size:0.85rem;"></div>
      </div>
    `;
    const msgs = [
      '<strong>Límite del Perceptrón:</strong> un solo perceptrón solo dibuja 1 recta (clasificador lineal), por lo que jamás resuelve XOR. Al agregar una <strong>capa oculta + función de activación NO lineal f(Σ)</strong> (sigmoide/ReLU), la red dobla el espacio y aproxima cualquier función continua.',
      '<strong>Feedforward (de izquierda a derecha):</strong><br/>1) Calculas suma ponderada en oculta: <code>z_h1 = w₁x₁ + w₂x₂ + b</code> y aplicas activación <code>h₁ = f(z_h1)</code>.<br/>2) Calculas salida final: <code>ŷ = f(w₅h₁ + w₆h₂ + b)</code>.<br/>3) Mides el error: <code>E = ½ (y_real − ŷ)²</code>.',
      '<strong>Backpropagation (de derecha a izquierda con Regla de la Cadena):</strong><br/>1) Primero ajustas la última capa (<code>w₅, w₆</code>): <code>w_nuevo = w_actual − α · (∂E/∂w)</code>.<br/>2) Luego propagas ese error hacia atrás para actualizar <code>w₁, w₂, w₃, w₄</code> según cuánto contribuyó cada una al error.'
    ];
    const out = el.querySelector('#nnTxt');
    el.querySelectorAll('#nnSteps button').forEach(b => {
      b.onclick = () => {
        el.querySelectorAll('#nnSteps button').forEach(x => x.classList.remove('active'));
        b.classList.add('active');
        out.innerHTML = msgs[Number(b.dataset.s)];
      };
    });
    out.innerHTML = msgs[0];
  }
};
