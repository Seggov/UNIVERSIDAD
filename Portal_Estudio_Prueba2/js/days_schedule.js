window.DAYS_DATA = [
  {
    id: 'lun23',
    short: 'Lun 23',
    title: 'Lunes 23 de noviembre',
    sub: '4 bloques · 09:00 a 17:00',
    exam: null,
    ocio: '17:00+ Libre / Ocio',
    timeline: [
      { time: '09:00–10:00', label: 'B1 · Arqui #1 (Memoria)', type: 'arqui', blockId: 'lun23_b1' },
      { time: '10:00–10:30', label: 'Pausa', type: 'break' },
      { time: '10:30–11:30', label: 'B2 · Arqui #2 (RAID y E/S)', type: 'arqui', blockId: 'lun23_b2' },
      { time: '11:30–14:30', label: 'Almuerzo y descanso', type: 'break' },
      { time: '14:30–15:30', label: 'B3 · EDD #1 (C05/C06 Código)', type: 'edd', blockId: 'lun23_b3' },
      { time: '15:30–16:00', label: 'Pausa', type: 'break' },
      { time: '16:00–17:00', label: 'B4 · CD #1 (C01, C02 + PLN)', type: 'cd', blockId: 'lun23_b4' },
      { time: '17:00+', label: 'Ocio libre', type: 'break' }
    ]
  },
  {
    id: 'mar24',
    short: 'Mar 24',
    title: 'Martes 24 de noviembre',
    sub: '6 bloques · 09:00 a 19:30 (incluye traslado Arqui #5)',
    exam: null,
    ocio: '19:30+ Libre / Ocio y dormir bien para Arqui',
    timeline: [
      { time: '09:00–10:00', label: 'B1 · Arqui #3 (Clase 9)', type: 'arqui', blockId: 'mar24_b1' },
      { time: '10:00–10:30', label: 'Pausa', type: 'break' },
      { time: '10:30–11:30', label: 'B2 · Arqui #4 (Autoeval. C6–9)', type: 'arqui', blockId: 'mar24_b2' },
      { time: '11:30–12:00', label: 'Pausa', type: 'break' },
      { time: '12:00–13:00', label: 'B3 · EDD #2 (C07 Enheb.+ABB)', type: 'edd', blockId: 'mar24_b3' },
      { time: '13:00–15:00', label: 'Almuerzo y descanso', type: 'break' },
      { time: '15:00–16:00', label: 'B4 · EDD #3 (ABB::remove)', type: 'edd', blockId: 'mar24_b4' },
      { time: '16:00–16:30', label: 'Pausa', type: 'break' },
      { time: '16:30–17:30', label: 'B5 · CD #2 (Clase 04 Viz)', type: 'cd', blockId: 'mar24_b5' },
      { time: '17:30–18:30', label: 'Pausa larga (1 h)', type: 'break' },
      { time: '18:30–19:30', label: 'B6 · Arqui #5 (Repaso Final)', type: 'arqui', blockId: 'mar24_b6' }
    ]
  },
  {
    id: 'mie25',
    short: 'Mié 25',
    title: 'Miércoles 25 de noviembre',
    sub: '0 bloques mañana · 3 bloques tarde (14:30–18:30)',
    exam: 'PRUEBA ARQUITECTURA DE COMPUTADORES · 10:00 (Sin bloques en la mañana)',
    ocio: '18:30+ Libre / Ocio',
    timeline: [
      { time: 'Mañana', label: 'Sin bloques (Clases / Calma)', type: 'break' },
      { time: '10:00–11:45', label: 'PRUEBA ARQUITECTURA', type: 'exam' },
      { time: '11:45–14:30', label: 'Almuerzo y descanso', type: 'break' },
      { time: '14:30–15:30', label: 'B1 · EDD #4 (Clase 07.1)', type: 'edd', blockId: 'mie25_b1' },
      { time: '15:30–16:00', label: 'Pausa', type: 'break' },
      { time: '16:00–17:00', label: 'B2 · EDD #5 (AVL + POO)', type: 'edd', blockId: 'mie25_b2' },
      { time: '17:00–17:30', label: 'Pausa', type: 'break' },
      { time: '17:30–18:30', label: 'B3 · CD #3 (Clase 05 Reg. Lineal)', type: 'cd', blockId: 'mie25_b3' }
    ]
  },
  {
    id: 'jue26',
    short: 'Jue 26',
    title: 'Jueves 26 de noviembre',
    sub: '2 bloques hasta ≤ 13:00 · 0 bloques post-prueba',
    exam: 'PRUEBA ESTRUCTURA DE DATOS (C++) · 16:15 (Sin bloques después de la prueba)',
    ocio: '17:45+ Libre / Ocio total post-prueba',
    timeline: [
      { time: '09:30–10:30', label: 'B1 · EDD #6 (Simulacro C++)', type: 'edd', blockId: 'jue26_b1' },
      { time: '10:30–11:00', label: 'Pausa', type: 'break' },
      { time: '11:00–12:00', label: 'B2 · EDD #7 (Corrección ≤13:00)', type: 'edd', blockId: 'jue26_b2' },
      { time: '12:00–16:15', label: 'Almuerzo, descanso y traslado', type: 'break' },
      { time: '16:15–17:45', label: 'PRUEBA ESTRUCTURA C++', type: 'exam' },
      { time: '17:45+', label: 'Sin bloques · Ocio libre', type: 'break' }
    ]
  },
  {
    id: 'vie27',
    short: 'Vie 27',
    title: 'Viernes 27 de noviembre',
    sub: '5 bloques · 09:00 a 17:30',
    exam: null,
    ocio: '17:30+ Libre / Ocio y dormir temprano (prueba 08:00)',
    timeline: [
      { time: '09:00–10:00', label: 'B1 · CD #4 (Clase 06 Logíst./SVM)', type: 'cd', blockId: 'vie27_b1' },
      { time: '10:00–10:30', label: 'Pausa', type: 'break' },
      { time: '10:30–11:30', label: 'B2 · CD #5 (Clase 07 Evaluación)', type: 'cd', blockId: 'vie27_b2' },
      { time: '11:30–12:00', label: 'Pausa', type: 'break' },
      { time: '12:00–13:00', label: 'B3 · CD #6 (Clase 08 Árboles/RF)', type: 'cd', blockId: 'vie27_b3' },
      { time: '13:00–15:00', label: 'Almuerzo y descanso', type: 'break' },
      { time: '15:00–16:00', label: 'B4 · Ciber #1 (SIEM + SOC)', type: 'ciber', blockId: 'vie27_b4' },
      { time: '16:00–16:30', label: 'Pausa', type: 'break' },
      { time: '16:30–17:30', label: 'B5 · Ciber #2 (Zero Trust)', type: 'ciber', blockId: 'vie27_b5' }
    ]
  },
  {
    id: 'sab28',
    short: 'Sáb 28',
    title: 'Sábado 28 de noviembre',
    sub: '0 bloques mañana · 1 bloque tarde (15:00–16:00)',
    exam: 'PRUEBA CIBERSEGURIDAD · 08:00 (Sin bloques en la mañana)',
    ocio: '16:00+ Libre / Ocio',
    timeline: [
      { time: '08:00–09:30', label: 'PRUEBA CIBERSEGURIDAD', type: 'exam' },
      { time: '09:30–15:00', label: 'Descanso largo y almuerzo', type: 'break' },
      { time: '15:00–16:00', label: 'B1 · CD #7 (Clase 09 Redes Neur.)', type: 'cd', blockId: 'sab28_b1' },
      { time: '16:00+', label: 'Ocio libre', type: 'break' }
    ]
  },
  {
    id: 'dom29',
    short: 'Dom 29',
    title: 'Domingo 29 de noviembre',
    sub: '4 bloques · 09:30 a 17:00 (Cierre total de Ciencia de Datos)',
    exam: null,
    ocio: '17:00+ Libre / Descanso previo al lunes',
    timeline: [
      { time: '09:30–10:30', label: 'B1 · CD #8 (Casos + Ayudantía 5)', type: 'cd', blockId: 'dom29_b1' },
      { time: '10:30–11:00', label: 'Pausa', type: 'break' },
      { time: '11:00–12:00', label: 'B2 · CD #9 (Mapa Teórico C01–C09)', type: 'cd', blockId: 'dom29_b2' },
      { time: '12:00–14:30', label: 'Almuerzo y descanso', type: 'break' },
      { time: '14:30–15:30', label: 'B3 · CD #10 (Simulacro 60 min)', type: 'cd', blockId: 'dom29_b3' },
      { time: '15:30–16:00', label: 'Pausa', type: 'break' },
      { time: '16:00–17:00', label: 'B4 · CD #11 (Corrección y Cierre)', type: 'cd', blockId: 'dom29_b4' }
    ]
  },
  {
    id: 'lun30',
    short: 'Lun 30',
    title: 'Lunes 30 de noviembre',
    sub: '0 bloques en la mañana · Día de cierre',
    exam: 'PRUEBA CIENCIA DE DATOS · 11:40 (Sin bloques de estudio en la mañana)',
    ocio: 'Tarde libre · ¡Fin de las 4 pruebas!',
    timeline: [
      { time: 'Mañana', label: 'Sin bloques (Clases / Mente fresca)', type: 'break' },
      { time: '11:40', label: 'PRUEBA CIENCIA DE DATOS', type: 'exam' },
      { time: 'Tarde', label: '¡Fin de semana de certámenes!', type: 'break' }
    ]
  }
];

window.PORTAL_BLOCKS = [];
