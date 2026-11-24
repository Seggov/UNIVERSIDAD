# Laboratorio 2 — Análisis Estacional y Predicción de Alta Demanda (H&M)

**Curso:** Ciencia de Datos 2026-02 — Escuela de Ingeniería, Universidad Católica del Norte (Coquimbo)  
**Integrantes:**
* Pedro Segovia — RUT 21672694-4 — Sección C2
* Aurelie Lorena Saliou — RUT ficticio 40017078-9 — Sección C2

---

## 1. Descripción y Objetivos del Proyecto

Siguiendo la metodología **CRISP-DM**, este proyecto analiza los patrones estacionales de compra en el dataset real de transacciones comerciales de H&M (*H&M Personalized Fashion Recommendations*, Kaggle) y evalúa mediante **regresión logística en KNIME 5.12** la probabilidad de que un día registre **alta demanda** a partir de variables de calendario.

* **Objetivo general:** Analizar los patrones estacionales de las compras y estimar, mediante regresión logística, la probabilidad de que un día sea de alta demanda según sus características de calendario.
* **Objetivos específicos:**
  1. Agrupar las transacciones por fecha y analizar la demanda diaria según el día de la semana, el día del mes y el mes del año.
  2. Definir una variable binaria (`alta_demanda`) que identifique los días de alta demanda evitando fuga de información (*data leakage*).
  3. Entrenar y evaluar modelos progresivos de regresión logística con variables de calendario e interpretar los patrones estacionales encontrados.

---

## 2. Arquitectura del Proyecto

```text
Ciencia-de-Datos-2/
├── README.md                                  # Documentación principal y guía del repositorio
├── .gitignore                                 # Exclusión de datos crudos masivos y metadatos locales
├── docs/                                      # Documentación académica y respaldo metodológico
│   ├── Laboratorio 2.pdf                      # Pauta oficial y rúbrica de evaluación del curso
│   ├── OBJETIVO GENERAL.pdf                   # Propuesta aprobada de objetivos e integrantes
│   └── Resumen_Resultados_y_Mejoras.md        # Resumen técnico de optimización del flujo KNIME y métricas
├── data/                                      # Conjuntos de datos del estudio
│   ├── raw/
│   │   └── transactions_train.csv             # Base original de Kaggle (31,79M filas · 3,49 GB — ignorada en Git)
│   └── processed/
│       └── demanda_diaria.csv                 # Serie diaria agregada (734 días continuos · 27 KB)
├── scripts/                                   # Código de preprocesamiento reproducible
│   └── preprocesar.py                         # Agrupa transactions_train.csv -> demanda_diaria.csv
├── knime/                                     # Proyecto fuente editable de KNIME 5.12
│   └── Lab2_Mejorado/                         # Workflow descomprimido (37/37 nodos ejecutados + data embebida)
└── entrega_final/                             # Archivos definitivos listos para subir a la plataforma
    ├── Informe_Laboratorio_2_HM.pdf           # Informe final en PDF (entregable oficial)
    ├── lab2.knwf                              # Workflow KNIME autocontenido (entregable oficial)
    ├── Informe_Laboratorio_2_HM.docx          # Versión editable del informe en Word
    ├── Informe_Laboratorio_2_HM.html          # Versión web autocontenida del informe
    ├── resultados/
    │   └── tabla_coeficientes_modelo4.csv     # Coeficientes, errores estándar, p-valores y Odds Ratios (M4)
    └── figuras/
        ├── fig1_evolucion_temporal.png        # Serie temporal diaria 2018–2020 y división Train/Test
        ├── fig2_eda_estacional.png            # Patrones por día de la semana, mes y periodo del mes
        ├── fig3_matrices_roc.png              # Matrices de confusión y curvas ROC comparativas (M1–M4)
        ├── fig4_odds_ratios_m4.png            # Forest plot de Odds Ratios significativos del Modelo 4
        └── fig5_workflow_knime.png            # Captura de arquitectura del workflow en KNIME 5.12
```

> **Nota sobre directorios ocultos locales:** `.git/` contiene el control de versiones del repositorio y `.metadata/` almacena la configuración local del espacio de trabajo de KNIME (excluida de Git mediante `.gitignore`).

---

## 3. Datos y Preprocesamiento (`scripts/preprocesar.py`)

El archivo original `data/raw/transactions_train.csv` contiene **31.788.324 registros individuales** (3,49 GB) entre el `2018-09-20` y el `2020-09-22`. Dado que la unidad de análisis es el **día**, el script `scripts/preprocesar.py` agrupa las compras por fecha (`t_dat`) y genera `data/processed/demanda_diaria.csv` (**734 días continuos**, 0 valores faltantes y 0 fechas ausentes).

### Variables generadas en `demanda_diaria.csv`

| Variable | Tipo | Descripción |
| :--- | :---: | :--- |
| `fecha` | Fecha | Fecha única diaria (`YYYY-MM-DD`). |
| `demanda_diaria` | Entero | Total de transacciones registradas ese día. |
| `dia_semana_num` | Entero | Número del día de la semana (`1` = Lunes … `7` = Domingo). |
| `dia_semana_nombre` | Texto | Nombre del día (`Lunes` … `Domingo`). |
| `dia_mes` | Entero | Día calendario del mes (`1` a `31`). |
| `mes` | Entero | Mes del año (`1` a `12`). |
| `es_fin_de_semana` | Binaria | `1` si es sábado o domingo; `0` en caso contrario. |
| `alta_demanda` | Binaria | Etiqueta inicial global (P75); **recalculada en KNIME solo sobre Train** para evitar *data leakage*. |

### Cómo reproducir el preprocesamiento

```bash
python scripts/preprocesar.py
```

---

## 4. Workflow en KNIME 5.12 y Resultados (`entrega_final/lab2.knwf`)

El flujo definitivo cuenta con **37 nodos nativos ejecutados en verde** (`knime/Lab2_Mejorado/` y empaquetado en `entrega_final/lab2.knwf`) con `demanda_diaria.csv` embebido mediante ruta relativa (`knime.workflow.data/demanda_diaria.csv`), dividido en tres bloques alineados con los objetivos:

1. **EDA (10 nodos):** evolución diaria 2018–2020, boxplot semanal ordenado Lunes–Domingo, barras por mes y día del mes, e histograma de distribución.
2. **Preparación, Target y División Temporal (10 nodos):** creación de `mes_nombre` y `periodo_mes` (inicio 1–10, mediados 11–20, fin 21–31), codificación *One-Hot*, partición cronológica estricta (**Train:** Año 1, `fecha < 2019-09-21`, 366 días; **Test:** Año 2, 368 días) y cálculo del umbral **P75 exclusivo de Train = 51.849,75 transacciones**.
3. **Modelado Progresivo y Evaluación (17 nodos):** cuatro regresiones logísticas con regularización Gaussiana (L2, `var = 10.0`), categorías de referencia omitidas (`enero`, `Lunes`, `inicio_mes`), `Scorer` y `ROC Curve`.

### Comparación de desempeño en Test (N = 368 días)

| Modelo | Predictores | Umbral | Accuracy | Precision (1) | Recall (1) | F1-Score | Cohen's κ | AUC-ROC |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Modelo 1** | Solo Mes | 0,50 | 79,9% | 27,9% | 36,2% | 0,315 | 0,199 | **0,694** |
| **Modelo 2** | Solo Día de la Semana | 0,30 | 59,0% | 16,7% | 55,3% | 0,256 | 0,075 | **0,593** |
| **Modelo 3** | Día de la Semana + Mes | 0,50 | 78,3% | 23,0% | 29,8% | 0,259 | 0,134 | **0,710** |
| **Modelo 4** | Completo (+ Periodo del Mes) | 0,50 | **81,5%** | **34,8%** | **51,1%** | **0,414** | **0,309** | **0,724** |

---

## 5. Archivos Listos para Subir a la Plataforma

Los dos entregables obligatorios definidos en la pauta (`docs/Laboratorio 2.pdf`) se encuentran centralizados en `entrega_final/`:

1. **`entrega_final/Informe_Laboratorio_2_HM.pdf`** — Informe final en formato oficial.
2. **`entrega_final/lab2.knwf`** — Proyecto KNIME autocontenido con todos los nodos ejecutados y datos embebidos.
