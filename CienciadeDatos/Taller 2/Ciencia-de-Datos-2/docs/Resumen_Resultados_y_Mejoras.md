# KNIME Mejorado (Versión Optimizada Definitiva) — Lab 2

**Integrantes:** Pedro Segovia y Aurelie Lorena Saliou  
**Archivo único listo para entregar / importar:** `Lab2_Mejorado.knwf` *(489 KB — 37/37 nodos ya ejecutados en verde + dataset embebido)*  
**Carpeta del workflow:** `Lab2_Mejorado/`  
**Dataset embebido (ruta relativa):** `Lab2_Mejorado/data/demanda_diaria.csv`

---

## 1. Optimización aplicada (de 64/52/50 nodos $\rightarrow$ **37 nodos**)

* **3 recuadros limpios** (1 por cada objetivo del taller), con márgenes holgados y cero duplicación:
  1. **🔵 Recuadro 1 — EDA (Objetivo 1, 10 nodos):**
     * Evolución diaria 2018–2020 (`String to Date&Time` $\rightarrow$ `Line Plot`, simplificado de 8 a 2 nodos con fechas reales en el eje X).
     * `Box Plot` por día de la semana ordenado Lunes–Domingo (`Sorter` $\rightarrow$ `Domain Calculator` $\rightarrow$ `Box Plot`).
     * `Bar Chart` demanda promedio por mes (`GroupBy` $\rightarrow$ `Bar Chart`).
     * `Bar Chart` demanda mediana por día del mes (`GroupBy` $\rightarrow$ `Bar Chart`).
     * `Histogram` distribución de la demanda diaria (evidencia de *outliers*).
  2. **🟠 Recuadro 2 — Carga, Preparación y Target (Objetivo 2, 10 nodos):**
     * `CSV Reader` con ruta 100% relativa (`knime.workflow.data/demanda_diaria.csv`).
     * `Rule Engine` (`mes_nombre`) $\rightarrow$ `Rule Engine` (`periodo_mes`: inicio/mediados/fin de mes).
     * `Column Filter` (quita `alta_demanda` global) $\rightarrow$ `Rule Engine` (`alta_demanda >= 51.849,75`, P75 de Train) $\rightarrow$ `One to Many` (dummies una sola vez) $\rightarrow$ `Rule-based Row Splitter` (`fecha < "2019-09-21"`).
     * Auditoría conectada directo al splitter: `GroupBy` (verifica P75 Train = **`51.849,75`**) + 2 `Statistics` (Train 24,9% vs. Test 12,8%).
  3. **🟢 Recuadro 3 — Modelado Progresivo y Evaluación (Objetivo 3, 17 nodos):**
     * 4 modelos temporales con `Prior = Gauss` (`var = 10.0`, `epsilon = 1e-5`), categorías de referencia omitidas (`enero`, `Lunes`, `inicio_mes`), probabilidades activadas (`include_probabilites = true`), `Scorer` y `ROC Curve`.
     * **Incorporado el acierto de `Lab2_3.0`:** **`Rule Engine` con umbral `0.30`** (`prediccion_umbral_30`) en el **Modelo 2** para resolver el Recall de 0% con umbral 0.50.

---

## 2. Resultados reales ejecutados en KNIME 5.12 (37/37 nodos en verde)

*Umbral verificado por `GroupBy (#5)`: **`51.849,75`** transacciones (P75 exclusivo de Train).*

| Modelo (Temporal, P75 Train = 51.849,75) | Umbral | Accuracy | Precision (1) | Recall (1) | F1-Score (1) | Cohen's $\kappa$ | **AUC-ROC** | Matriz (TP / FP / FN / TN) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Modelo 1:** Solo Mes | 0,50 | 79,9% | 27,9% | 36,2% | 0,315 | 0,199 | **0,694** | 17 / 44 / 30 / 277 |
| **Modelo 2:** Solo Día de la Semana | **0,30** | 59,0% | 16,7% | **55,3%** | 0,256 | 0,075 | **0,593** | 26 / 130 / 21 / 191 |
| **Modelo 3:** Día de la Semana + Mes | 0,50 | 78,3% | 23,0% | 29,8% | 0,259 | 0,134 | **0,710** | 14 / 47 / 33 / 274 |
| **Modelo 4:** Completo (+ Periodo Mes) | 0,50 | **81,5%** | **34,8%** | **51,1%** | **0,414** | **0,309** | **0,724** | **24 / 45 / 23 / 276** |

### Principales Odds Ratios significativos (Modelo 4 — PMML real de KNIME `#231`)
* **Meses (vs. enero):** Julio ($\text{OR} = 52{,}84$), Junio ($\text{OR} = 36{,}69$), Mayo ($\text{OR} = 6{,}22$), Octubre ($\text{OR} = 5{,}18$), Abril ($\text{OR} = 4{,}78$), Marzo estabilizado ($\text{OR} = 0{,}067$).
* **Días de la semana (vs. Lunes):** Jueves ($\text{OR} = 7{,}71$), Viernes ($\text{OR} = 3{,}97$), Sábado ($\text{OR} = 3{,}60$), Miércoles ($\text{OR} = 3{,}42$).
* **Periodo del mes (vs. inicio 1–10):** **Fin de mes (días 21–31)** ($\text{OR} = 3{,}82$, $p < 0{,}001$).
