# Proyecto de Sistemas Digitales — Game & Watch

Guía general de la carpeta. Organización realizada el 28 de octubre de 2026.

## Resumen general

El proyecto estudia una consola Nintendo Game & Watch para describir su funcionamiento y llevar sus reglas a máquinas de estados, lógica combinacional y circuitos digitales. Los documentos plantean una implementación con compuertas, registros y contadores, y una posterior adaptación a Arduino.

La carpeta reúne documentación, generadores de informes y un [programa Arduino del controlador de cinco fases](output/tinkercad/Controlador_Judge_Arduino.ino). Hay montajes del controlador en Tinkercad. La generación de números, las acciones de los jugadores y el cálculo de puntajes todavía no están implementados en estos montajes.

Hay dos casos de estudio diferentes:

- **Judge:** juego de reacción entre dos participantes que comparan números y deciden atacar o esquivar. Tiene un informe propio y una imagen con el flujo de una ronda. Es la referencia más directa para retomar la conversación reciente sobre las cinco fases, pero falta confirmar que coincide con la presentación que usó el equipo.
- **Ball:** juego de malabarismo, movimiento de brazos y captura de pelotas. Sus informes se conservan separados para evitar mezclar sus reglas con las de Judge.

En el chat del equipo se propone repartir cinco fases entre tres personas: dos fases para cada una de dos personas y la fase más extensa para la tercera. Los mensajes aportados no fijan responsables ni identifican con certeza la fase más extensa.

## Por dónde empezar

La versión sencilla está [montada con Arduino en Tinkercad](https://www.tinkercad.com/things/i3ChqoUqULW/editel). Enciende Q0 al arrancar, avanza con temporizadores y usa cuatro botones rotulados. La [guía breve de Arduino](output/tinkercad/GUIA_ARDUINO.md) explica cómo probarla.

El [montaje anterior con compuertas y flip-flops](https://www.tinkercad.com/things/6XiKYRBh2IK/editel) se conserva como referencia. Su [guía](output/tinkercad/GUIA_CONTROLADOR.md) explica el reinicio y el reloj manual que necesita para funcionar.

1. Consultar el [enunciado de la primera evaluación](<referencias/enunciado/PSD 2026_20 - Enunciado Primera Evaluación.pdf>) para conocer los requisitos de esa entrega. No se identificó un enunciado específico de la actividad reciente de autómatas.
2. Si trabajan con Judge, leer la sección 3.3 del [informe en Markdown](documentos/judge/INFORME_GAME_AND_WATCH_JUDGE.md), donde se describen las cinco fases, y revisar el [flujo gráfico de una ronda](recursos/imagenes/slide8_img.png).
3. Usar el material de clases para pasar del comportamiento del juego a las tablas, Karnaugh y circuitos.
4. Confirmar las reglas y los diagramas de la presentación antes de repartir y desarrollar los autómatas.

Ya está disponible una [propuesta de estados y autómatas de Judge](documentos/judge/automatas/ESTADOS_Y_AUTOMATAS_JUDGE.md): diagrama general con círculos, tabla de transiciones, codificación y detalle de las cinco fases. Incluye las decisiones propuestas y las reglas que faltan confirmar. El [diagrama general editable](documentos/judge/automatas/estados_judge.mmd) se guarda también por separado.

La [versión PDF de estados y autómatas](output/pdf/Estados_y_automatas_Judge.pdf) muestra el diagrama general y las cinco fases con estados de izquierda a derecha, ejemplos y significados. Esta versión se centra en jugador 1 contra jugador 2, ambos humanos (Game B). Las tablas se entregan por separado en [Tablas, Karnaugh y circuito de Judge](output/pdf/Tablas_Karnaugh_y_circuito_Judge.pdf): matriz de transición con L1-L5, entradas D, mapas y circuito del controlador general. Este segundo documento se regenera con [exportar_tablas_judge_pdf.py](herramientas/exportar_tablas_judge_pdf.py). Se regenera con [exportar_estados_pdf.py](herramientas/exportar_estados_pdf.py), usando ReportLab y las fuentes Arial de Windows.

## Organización de archivos

```text
ProyectoSistemasInteligentes/
├── README.md
├── referencias/
│   ├── enunciado/       Requisitos de la primera evaluación
│   └── clases/          Material de sistemas digitales
├── documentos/
│   ├── judge/           Informes y carpeta automatas/ del juego Judge
│   ├── ball/            Informes del juego Ball
│   └── originales/      Documento original conservado
├── recursos/
│   └── imagenes/        Diagrama y recortes gráficos existentes
└── herramientas/        Generadores de informes en Python
```

Se conservaron los nombres y el contenido de los documentos originales. Los generadores se ajustaron para guardar sus resultados dentro de la carpeta del juego correspondiente.

## Arquitectura funcional documentada

El funcionamiento se puede entender como cuatro bloques que colaboran:

| Bloque | Función | Ejemplo en Judge |
|---|---|---|
| Entradas | Recibir las acciones del usuario y las señales de control. | Botones de ataque, esquiva, selección de modo y reinicio. |
| Control secuencial | Recordar la fase actual y decidir cuándo cambiar. | Pasar de cuenta regresiva a reacción y después a otra ronda o al fin de partida. |
| Datos y lógica combinacional | Comparar valores y calcular resultados. | Comparar los números de los jugadores, evaluar las acciones y actualizar puntajes. |
| Salidas | Mostrar o comunicar el resultado. | Números, marcador, posturas de los personajes y sonido. |

El reloj sincroniza las actualizaciones; los registros guardan valores como el estado y los puntajes. Las entradas y los datos influyen en las decisiones del controlador, que habilita las operaciones y salidas correspondientes.

### Las cinco fases de Judge según el informe

| Estado | Nombre | Qué hace | Siguiente paso documentado |
|---|---|---|---|
| q₀ | Espera / reloj | Espera el inicio de una partida. | Game A o Game B → q₁. |
| q₁ | Inicialización | Pone en cero los puntajes y prepara el juego. | Preparación terminada → q₂. |
| q₂ | Cuenta regresiva y generación de números | Prepara y revela los números de la ronda. | Números revelados → q₃. |
| q₃ | Reacción y evaluación | Lee acciones, compara números y asigna puntos. | Otra ronda → q₂; victoria → q₄. |
| q₄ | Fin de partida | Muestra el ganador y el resultado final. | Espera reinicio; falta formalizar su destino en la tabla de transiciones. |

Esta tabla resume el modelo existente; no constituye todavía una tabla completa para construir el circuito. Una fase puede descomponerse en varios estados internos. q₃ concentra muchas decisiones y podría ser la fase más extensa mencionada en el chat, pero esa identificación no está confirmada.

En **Ball**, el modelo cambia: q₀ espera/reloj, q₁ inicialización, q₂ movimiento del juego, q₃ evaluación de captura o fallo, q₄ fin de partida. Aunque los identificadores coinciden, las funciones y reglas son diferentes.

### Del juego al circuito

```text
Reglas y diagramas de flujo
          ↓
Estados, entradas, salidas y condiciones de transición
          ↓
Diagrama del autómata
          ↓
Codificación de estados y tabla de transiciones/salidas
          ↓
Ecuaciones booleanas y simplificación con Karnaugh
          ↓
Circuito con compuertas y memoria (flip-flops)
          ↓
Simulación y comprobación del comportamiento
```

Un diagrama de flujo describe pasos y decisiones. El autómata precisa qué estados se recuerdan y qué condiciones producen cada cambio. Karnaugh simplifica las funciones lógicas necesarias para implementar ese comportamiento. Un controlador con cinco estados requiere al menos tres bits si se usa codificación binaria; los posibles autómatas internos se dimensionan por separado.

## Qué es cada documento y recurso

### Referencias del curso

| Archivo | Propósito |
|---|---|
| [PSD 2026_20 - Enunciado Primera Evaluación.pdf](<referencias/enunciado/PSD 2026_20 - Enunciado Primera Evaluación.pdf>) | Enunciado identificado por su nombre como correspondiente a la primera evaluación. Referencia para revisar los requisitos originales; no se revalidó su contenido en esta organización. |
| [02 - Sistemas numéricos y cambios de base.pdf](<referencias/clases/02 - [U1] Sistemas numéricos y cambios de base.pdf>) | Material de clase sobre representación numérica y cambios de base; útil para codificar estados y valores. |
| [06 - Álgebra Booleana y Puertas Lógicas.pdf](<referencias/clases/06 - [U2] Álgebra Booleana y Puertas Lógicas.pdf>) | Material de clase sobre funciones booleanas y compuertas. |
| [07 - Simplificación mediante Leyes, Universalidad NAND y NOR.pdf](<referencias/clases/07 - [U2] Simplificación mediante Leyes, Universalidad NAND y NOR.pdf>) | Material de clase sobre simplificación e implementación mediante NAND y NOR. |
| [08 - Simplificación mediante mapas de Karnaugh, Perturbaciones.pdf](<referencias/clases/08 - [U2] Simplificación mediante mapas de Karnaugh, Perturbaciones.pdf>) | Material de clase sobre Karnaugh y perturbaciones en circuitos. |

Los temas de los cuatro archivos de clase se describen a partir de sus títulos; esta tarea no incluyó una revisión página por página.

### Documentos de Judge

| Archivo | Propósito |
|---|---|
| [INFORME_GAME_AND_WATCH_JUDGE.md](documentos/judge/INFORME_GAME_AND_WATCH_JUDGE.md) | Informe editable en texto: descripción del dispositivo, reglas, entradas/salidas, cinco estados, lógica de arbitraje, Karnaugh, alcance con TTL/Arduino y mejoras propuestas. |
| [Informe_G_and_W_Judge.docx](documentos/judge/Informe_G_and_W_Judge.docx) | Versión Word existente para edición y presentación del informe. |
| [Informe_G_and_W_Judge.html](documentos/judge/Informe_G_and_W_Judge.html) | Versión maquetada para navegador; el generador utiliza HTML para producir el PDF. |
| [Informe_G_and_W_Judge.pdf](documentos/judge/Informe_G_and_W_Judge.pdf) | Versión PDF existente para lectura o distribución. |

Son versiones del mismo caso de estudio. No se comprobó que todos los formatos tengan contenido idéntico ni que alguno sea la entrega aprobada por el equipo.

### Documentos de Ball

| Archivo | Propósito |
|---|---|
| [INFORME_TECNICO_GAME_AND_WATCH.md](documentos/ball/INFORME_TECNICO_GAME_AND_WATCH.md) | Informe técnico de Ball: movimiento de pelotas, capturas, fallos, máquina de estados, lógica combinacional y propuestas de implementación. |
| [INFORME_Y_PRESENTACION_FINAL.md](documentos/ball/INFORME_Y_PRESENTACION_FINAL.md) | Documento extenso de trabajo sobre Ball que reúne comentarios de revisión, pautas de formato, informe y guion de diez diapositivas. El nombre “FINAL” no acredita que haya sido entregado o validado. |
| [Informe_Sistemas_Digitales_Game_and_Watch.html](documentos/ball/Informe_Sistemas_Digitales_Game_and_Watch.html) | Versión HTML del informe de Ball, preparada para visualización e impresión. |
| [Informe_Sistemas_Digitales_Game_and_Watch.pdf](documentos/ball/Informe_Sistemas_Digitales_Game_and_Watch.pdf) | Versión PDF existente del informe de Ball. |

Los comentarios y afirmaciones sobre evaluaciones o supuestas instrucciones ocultas que aparecen en documentos de trabajo son contenido histórico del archivo; no se verificaron y no establecen requisitos para continuar el proyecto.

### Original conservado

| Archivo | Propósito |
|---|---|
| [Informe de presentación RNGPT++_20_09.docx](<documentos/originales/Informe de presentación RNGPT++_20_09.docx>) | Documento original recibido, conservado para consulta y comparación. No se revisó su contenido interno en esta organización ni se le asignó un juego sin comprobarlo. |

### Recursos gráficos

| Archivo | Contenido observado |
|---|---|
| [slide8_img.png](recursos/imagenes/slide8_img.png) | Diagrama de una ronda de Judge: comparación de números, ataque/esquiva, resultados, marcador y nueva ronda. Es un flujo de decisiones, no un esquema eléctrico. |
| [slide8_topleft.png](recursos/imagenes/slide8_topleft.png) | Recorte de la esquina superior izquierda del gráfico de Judge; contiene el título y parte del diagrama. |
| [ground_crop.png](recursos/imagenes/ground_crop.png) | Recorte decorativo con suelo de estilo pixelado y parte de los nombres de integrantes. |

### Herramientas de generación

| Archivo | Función y destino |
|---|---|
| [generate_documents.py](herramientas/generate_documents.py) | Genera Word, HTML y PDF de Ball en `documentos/ball/`. Puede crear el DOCX de Ball que no estaba entre los archivos iniciales. |
| [generate_judge_documents.py](herramientas/generate_judge_documents.py) | Genera Word, HTML y PDF de Judge en `documentos/judge/`. |

Estos programas contienen sus propios textos: **no leen los archivos Markdown como fuente**. Editar un informe `.md` no actualiza automáticamente los demás formatos. Regenerar puede sobrescribir cambios manuales del Word, HTML o PDF del mismo nombre.

Requieren Python con `python-docx` y utilizan Microsoft Edge para imprimir el HTML a PDF. La ruta de Edge está fijada en los scripts a `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`; debe existir en el equipo. No se ejecutaron los generadores durante esta organización para conservar los informes existentes.

Desde la raíz del proyecto, cuando corresponda regenerar:

```powershell
python herramientas/generate_judge_documents.py
python herramientas/generate_documents.py
```

## Estado actual y asuntos pendientes

- **Disponible:** informes de ambos juegos, descripción de cinco estados por juego, material teórico, un flujo gráfico de Judge y generadores de documentos. Se añadió una propuesta de autómata principal de Judge con tabla completa del controlador, codificación binaria y cinco diagramas internos.
- **Por confirmar:** juego y versión efectivamente presentados, cinco fases acordadas por el equipo, fase con cuatro diagramas y reparto de responsables.
- **Por conciliar:** el gráfico de Judge incluye una penalización de “Rival +5” en una rama de golpe incorrecto, mientras el informe Markdown describe +2 al rival por acción inversa. Se deben acordar las reglas antes de convertirlas en lógica.
- **Por desarrollar o incorporar:** cerrar las reglas de arbitraje y las tablas completas de los autómatas internos, formalizar todas sus salidas y obtener ecuaciones del próximo estado, mapas de Karnaugh y archivos de circuitos/simulación. La propuesta nueva cubre los estados generales y el detalle inicial de las cinco fases.
- **Por verificar:** correspondencia entre Markdown, Word, HTML, PDF y la presentación usada. Los enlaces absolutos antiguos dentro de los documentos históricos pueden apuntar a ubicaciones anteriores; se preservaron sus contenidos.

El siguiente trabajo puede partir del modelo acordado de Judge o de Ball y guardar cada entregable junto a la documentación de ese juego. Los informes históricos conservan su contenido; el nuevo diseño de estados de Judge está separado en `documentos/judge/automatas/`.
