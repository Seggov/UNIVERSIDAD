(function() {
  const STORAGE_DONE = 'portal_estudio_p2_done_v1';
  const STORAGE_NOTES = 'portal_estudio_p2_notes_v1';

  let doneMap = {};
  let notesMap = {};
  try { doneMap = JSON.parse(localStorage.getItem(STORAGE_DONE) || '{}'); } catch (_) {}
  try { notesMap = JSON.parse(localStorage.getItem(STORAGE_NOTES) || '{}'); } catch (_) {}

  let activeDayId = 'lun23';
  let activeBlockId = 'lun23_b1';
  let courseFilter = 'all'; // 'all' | 'arqui' | 'edd' | 'ciber' | 'cd'

  const dayListEl = document.getElementById('dayList');
  const mainEl = document.getElementById('mainContent');
  const progTextEl = document.getElementById('progText');
  const progFillEl = document.getElementById('progFill');

  function saveDone() {
    try { localStorage.setItem(STORAGE_DONE, JSON.stringify(doneMap)); } catch (_) {}
    updateGlobalProgress();
  }
  function saveNote(id, val) {
    notesMap[id] = val;
    try { localStorage.setItem(STORAGE_NOTES, JSON.stringify(notesMap)); } catch (_) {}
  }

  function updateGlobalProgress() {
    const total = window.PORTAL_BLOCKS.length;
    const doneCount = window.PORTAL_BLOCKS.filter(b => doneMap[b.id]).length;
    progTextEl.textContent = `${doneCount} / ${total} bloques`;
    progFillEl.style.width = `${total ? Math.round((doneCount / total) * 100) : 0}%`;
  }

  function renderSidebar() {
    dayListEl.innerHTML = '';
    window.DAYS_DATA.forEach(day => {
      const dayBlocks = window.PORTAL_BLOCKS.filter(b => b.dayId === day.id);
      const doneInDay = dayBlocks.filter(b => doneMap[b.id]).length;
      const btn = document.createElement('button');
      btn.className = 'day-btn' + (courseFilter === 'all' && activeDayId === day.id ? ' active' : '');
      btn.innerHTML = `
        <div class="day-btn-top">
          <span>${day.short} · ${day.title.split(' de ')[0]}</span>
          ${day.exam ? '<span class="exam-tag">PRUEBA</span>' : `<span style="font-size:0.75rem;color:#94a3b8;">${doneInDay}/${dayBlocks.length}</span>`}
        </div>
        <div class="day-btn-sub">
          <span>${dayBlocks.length ? dayBlocks.length + ' blq (60m)' : 'Solo prueba'}</span>
          ${dayBlocks.length && doneInDay === dayBlocks.length ? '<span style="color:#34d399;font-weight:700;">✓ Listo</span>' : ''}
        </div>
      `;
      btn.onclick = () => {
        courseFilter = 'all';
        document.querySelectorAll('.filter-chip').forEach(c => c.classList.toggle('active', c.dataset.course === 'all'));
        activeDayId = day.id;
        const first = dayBlocks[0];
        activeBlockId = first ? first.id : null;
        renderAll();
      };
      dayListEl.appendChild(btn);
    });
  }

  function renderBlockCard(block) {
    const isDone = !!doneMap[block.id];
    const courseClass = { arqui: 'cb-arqui', edd: 'cb-edd', ciber: 'cb-ciber', cd: 'cb-cd' }[block.course];
    const dayObj = window.DAYS_DATA.find(d => d.id === block.dayId);

    const card = document.createElement('article');
    card.className = 'block-card';
    card.innerHTML = `
      <div class="block-header">
        <div>
          <span class="course-badge ${courseClass}">${block.courseLabel} · ${block.ra}</span>
          <h3 class="block-title">Bloque ${block.num}: ${block.title}</h3>
          <div class="block-meta">📅 ${dayObj ? dayObj.title : ''} &nbsp;|&nbsp; ⏰ <strong>${block.time}</strong></div>
        </div>
        <button class="check-complete-btn ${isDone ? 'done' : ''}" id="btnComplete_${block.id}">
          <span>${isDone ? '✅ Bloque Completado' : '⬜ Marcar Completado'}</span>
        </button>
      </div>

      <div class="goal-banner">
        <strong>🎯 Objetivo final de estos 60 min:</strong> ${block.goal}
      </div>

      <div class="zone">
        <h4 class="zone-title">💡 Explicación Sencilla y Directo al Punto</h4>
        ${block.simpleHtml}
      </div>

      ${block.widgetId ? `
      <div class="zone">
        <h4 class="zone-title">🎨 Laboratorio Visual Interactivo (Toca y prueba)</h4>
        <div id="widgetMount_${block.id}"></div>
      </div>` : ''}

      <div class="zone sketch-zone">
        <h4 class="zone-title">✏️ Qué Dibujar y Escribir con tus Palabras en tu Cuaderno</h4>
        ${block.sketchHtml}
      </div>

      <div class="zone">
        <h4 class="zone-title">📋 Enunciados, Ejercicios Prácticos y Pauta</h4>
        ${block.practiceHtml}
        <div style="margin-top:0.85rem;">
          <div style="font-size:0.76rem;color:#94a3b8;margin-bottom:0.35rem;font-weight:700;">📂 ARCHIVOS DE ESTE BLOQUE EN TU CARPETA UNIVERSIDAD:</div>
          <div class="file-list">
            ${block.files.map(f => `<span class="file-pill">${f}</span>`).join('')}
          </div>
        </div>
      </div>

      <div class="zone">
        <h4 class="zone-title">📝 Mis Reglas / Resumen con mis Palabras (Se guarda solo en este navegador)</h4>
        <textarea class="notes-area" id="noteArea_${block.id}" placeholder="Escribe aquí tus reglas cortas, dudas para preguntar en el chat o puntos clave de este bloque..."></textarea>
      </div>
    `;

    card.querySelector(`#btnComplete_${block.id}`).onclick = () => {
      doneMap[block.id] = !doneMap[block.id];
      saveDone();
      renderAll();
    };

    const noteArea = card.querySelector(`#noteArea_${block.id}`);
    noteArea.value = notesMap[block.id] || '';
    noteArea.addEventListener('input', e => saveNote(block.id, e.target.value));

    if (block.widgetId && window.WIDGETS[block.widgetId]) {
      const mount = card.querySelector(`#widgetMount_${block.id}`);
      window.WIDGETS[block.widgetId](mount);
    }

    return card;
  }

  function renderMain() {
    mainEl.innerHTML = '';

    // Mode 1: Filtered by Course across all days
    if (courseFilter !== 'all') {
      const names = { arqui: 'Arquitectura de Computadores (5 bloques)', edd: 'Estructura de Datos en C++ (7 bloques)', ciber: 'Ciberseguridad (2 bloques)', cd: 'Ciencia de Datos (11 bloques)' };
      const blocks = window.PORTAL_BLOCKS.filter(b => b.course === courseFilter);
      if (!blocks.some(b => b.id === activeBlockId)) activeBlockId = blocks[0].id;

      const hero = document.createElement('div');
      hero.className = 'day-hero';
      hero.innerHTML = `<h2>Ruta Completa · ${names[courseFilter]}</h2><p style="margin:0.3rem 0 0;color:#94a3b8;font-size:0.88rem;">Viendo todos los bloques de este curso en orden progresivo de inicio a fin.</p>`;
      mainEl.appendChild(hero);

      const tabs = document.createElement('div');
      tabs.className = 'block-tabs';
      blocks.forEach(b => {
        const dObj = window.DAYS_DATA.find(d => d.id === b.dayId);
        const t = document.createElement('button');
        t.className = `block-tab c-${b.course}` + (b.id === activeBlockId ? ' active' : '');
        t.innerHTML = `<span class="done-dot ${doneMap[b.id]?'done':''}"></span><span><strong>${dObj.short} · B${b.num}</strong> — ${b.courseLabel}</span>`;
        t.onclick = () => { activeBlockId = b.id; renderMain(); };
        tabs.appendChild(t);
      });
      mainEl.appendChild(tabs);

      const chosen = blocks.find(b => b.id === activeBlockId) || blocks[0];
      mainEl.appendChild(renderBlockCard(chosen));
      return;
    }

    // Mode 2: Day-by-Day view
    const day = window.DAYS_DATA.find(d => d.id === activeDayId) || window.DAYS_DATA[0];
    const dayBlocks = window.PORTAL_BLOCKS.filter(b => b.dayId === day.id);

    const hero = document.createElement('div');
    hero.className = 'day-hero';
    hero.innerHTML = `
      <div class="day-hero-head">
        <div>
          <h2>${day.title}</h2>
          <div style="color:#94a3b8;font-size:0.88rem;">${day.sub} &nbsp;·&nbsp; 🌙 ${day.ocio}</div>
        </div>
      </div>
      ${day.exam ? `<div class="exam-banner">🚨 ${day.exam}</div>` : ''}
      <div class="timeline-strip" id="tlStrip"></div>
    `;
    const strip = hero.querySelector('#tlStrip');
    day.timeline.forEach(item => {
      const div = document.createElement('div');
      const cls = item.type === 'break' ? 'tl-break' : (item.type === 'exam' ? 'tl-exam' : `tl-${item.type} clickable`);
      div.className = `tl-item ${cls}`;
      div.innerHTML = `<strong>${item.time}</strong> <span>${item.label}</span>`;
      if (item.blockId) {
        div.onclick = () => { activeBlockId = item.blockId; renderMain(); };
      }
      strip.appendChild(div);
    });
    mainEl.appendChild(hero);

    if (dayBlocks.length === 0) {
      // Lunes 30 special view
      const endCard = document.createElement('div');
      endCard.className = 'block-card';
      endCard.innerHTML = `
        <h3 style="margin:0;color:#a78bfa;">🏁 Lunes 30 de noviembre · Día de la Prueba Final de Ciencia de Datos (11:40)</h3>
        <p style="margin:0;color:#cbd5e1;">Tal como definiste en tu planificación, <strong>hoy lunes por la mañana no hay bloques de estudio</strong> (tienes clases / mente descansada). Toda la materia quedó cerrada ayer domingo a las 17:00.</p>
        <div class="w-controls">
          <button class="w-btn" id="jumpMaster">Ver Tabla Maestra de Modelos (Dom B2)</button>
          <button class="w-btn" id="jumpCheck">Ver Checklist Anti-Errores (Dom B4)</button>
        </div>
      `;
      endCard.querySelector('#jumpMaster').onclick = () => { activeDayId = 'dom29'; activeBlockId = 'dom29_b2'; renderAll(); };
      endCard.querySelector('#jumpCheck').onclick = () => { activeDayId = 'dom29'; activeBlockId = 'dom29_b4'; renderAll(); };
      mainEl.appendChild(endCard);
      return;
    }

    if (!dayBlocks.some(b => b.id === activeBlockId)) activeBlockId = dayBlocks[0].id;

    const tabs = document.createElement('div');
    tabs.className = 'block-tabs';
    dayBlocks.forEach(b => {
      const btn = document.createElement('button');
      btn.className = `block-tab c-${b.course}` + (b.id === activeBlockId ? ' active' : '');
      btn.innerHTML = `
        <span class="done-dot ${doneMap[b.id] ? 'done' : ''}"></span>
        <span><strong>Bloque ${b.num}</strong> (${b.time.split(' ')[0]}) · ${b.courseLabel}</span>
      `;
      btn.onclick = () => { activeBlockId = b.id; renderMain(); };
      tabs.appendChild(btn);
    });
    mainEl.appendChild(tabs);

    const activeBlock = dayBlocks.find(b => b.id === activeBlockId) || dayBlocks[0];
    mainEl.appendChild(renderBlockCard(activeBlock));
  }

  function renderAll() {
    updateGlobalProgress();
    renderSidebar();
    renderMain();
  }

  // Filter chips
  document.querySelectorAll('.filter-chip').forEach(chip => {
    chip.onclick = () => {
      document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      courseFilter = chip.dataset.course;
      renderAll();
    };
  });

  // 60-Minute Block Timer
  let secsLeft = 3600;
  let timerInt = null;
  const tDisp = document.getElementById('timerDisplay');
  const tStart = document.getElementById('timerStart');
  const tReset = document.getElementById('timerReset');

  function fmtTime(s) {
    const m = Math.floor(s / 60), r = s % 60;
    return String(m).padStart(2, '0') + ':' + String(r).padStart(2, '0');
  }
  tStart.onclick = () => {
    if (timerInt) {
      clearInterval(timerInt);
      timerInt = null;
      tStart.textContent = '▶ Iniciar';
    } else {
      tStart.textContent = '⏸ Pausar';
      timerInt = setInterval(() => {
        if (secsLeft > 0) {
          secsLeft--;
          tDisp.textContent = fmtTime(secsLeft);
        } else {
          clearInterval(timerInt);
          timerInt = null;
          tStart.textContent = '▶ Iniciar';
          alert('⏰ ¡60 minutos cumplidos! Tómate tu pausa de 30 minutos.');
        }
      }, 1000);
    }
  };
  tReset.onclick = () => {
    if (timerInt) { clearInterval(timerInt); timerInt = null; }
    secsLeft = 3600;
    tDisp.textContent = '60:00';
    tStart.textContent = '▶ Iniciar';
  };

  // Master Schedule Modal
  const modal = document.getElementById('scheduleModal');
  document.getElementById('openMasterBtn').onclick = () => modal.classList.add('open');
  document.getElementById('closeMasterBtn').onclick = () => modal.classList.remove('open');
  modal.onclick = e => { if (e.target === modal) modal.classList.remove('open'); };

  renderAll();
})();
