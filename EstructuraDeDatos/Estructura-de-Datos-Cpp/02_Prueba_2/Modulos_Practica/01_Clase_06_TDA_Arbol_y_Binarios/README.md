# Módulo 01 (Clase 06) — TDA Árbol, Representaciones, Árboles Binarios y Recorridos

**Fuente oficial:** [06 - [U4] TDA Árbol, Árboles Binarios, Recorridos.pdf](../../Material_Teorico/06%20-%20%5BU4%5D%20TDA%20%C3%81rbol,%20%C3%81rboles%20Binarios,%20Recorridos.pdf)  
**Práctica orientativa:** 1.5–2 horas.

[Resumen Prueba 2](../README.md) · [Práctica y Apuntes](01_Practica_y_Apuntes/apuntes.md) · [Enunciados Escalados](02_Enunciados/README.md) · [Siguiente: Clase 07](../02_Clase_07_Enhebrados_y_ABB/README.md)

---

## Contenidos de la Clase 06

### 1. Conceptos fundamentales del TDA Árbol
Un árbol es una estructura **no lineal** y **jerárquica** formada por un **nodo raíz** y $K \ge 0$ subárboles disjuntos.

```text
Nivel 1:            (D)                 <-- Raíz (grado = 3, altura del árbol = 4)
                  /  |  \
Nivel 2:       (A)  (S)  (T)            <-- A, S, T son hermanos (siblings)
                    / \     \
Nivel 3:          (M) (L)   (F)         <-- L y F son hojas (grado = 0)
                 / | \
Nivel 4:       (V)(W)(P)                <-- V, W, P son hojas; profundidad de W = 3 arcos
```

| Término | Definición según cátedra (Clase 06) | Ejemplo en el diagrama |
| :--- | :--- | :--- |
| **Raíz (*root*)** | Único nodo inicial sin padre | `D` |
| **Grado de un nodo** | Cantidad de subárboles (hijos) del nodo | `D` = 3, `S` = 2, `T` = 1, `A` = 0 |
| **Hoja (*leaf*)** | Nodo sin subárboles (grado = 0) | `A, V, W, P, L, F` |
| **Camino y longitud** | Secuencia de arcos entre dos nodos; longitud = n° de arcos | `D -> S -> M -> W` tiene longitud 3 |
| **Nivel de un nodo** | Posición respecto a la raíz (**raíz = nivel 1**) | `D` = 1, `T` = 2, `M` = 3, `W` = 4 |
| **Altura del árbol** | Máximo nivel de cualquier nodo del árbol | Altura = 4 |
| **Altura de un nodo** | Camino más largo desde una hoja + 1 | `S` tiene altura 3 (`S -> M -> V`) |
| **Profundidad de un nodo** | Longitud (arcos) desde la raíz al nodo | `F` tiene profundidad 2 |
| **Árboles isomorfos** | Comparten la **misma estructura**, no necesariamente los valores | Misma forma, letras distintas |
| **Árboles semejantes** | Comparten los **mismos valores**, no necesariamente la estructura | Mismos elementos, forma distinta |
| **Bosque** | Conjunto de árboles disjuntos | Quitar la raíz deja un bosque |

---

### 2. Árboles Binarios y sus Propiedades
Cada nodo tiene **a lo más 2 hijos**: izquierdo (`left`) y derecho (`right`).

- Máximo de nodos en el nivel $i$ ($i \ge 1$): **$2^{i-1}$**.
- Máximo de nodos totales en profundidad/altura $K$: **$2^K - 1$**.
- **Árbol binario lleno (*full*):** tiene exactamente $2^K - 1$ nodos (todos los niveles completos).
- **Árbol binario completo (*complete*):** solo hay hojas en los niveles $L$ y $L-1$, y las del último nivel $L$ están agrupadas **lo más a la izquierda posible**. Todo árbol lleno es completo.

```text
Lleno y Completo (K=3, 7 nodos)       No Lleno, pero Completo         No Lleno, No Completo
            (1)                                (1)                           (40)
           /   \                              /   \                         /    \
        (2)     (3)                        (2)     (3)                    (8)    (80)
       /  \     /  \                      /  \                              \    /   \
     (4)  (5) (6)  (7)                  (4)  (5)                           (12)(67)(102)
```

---

### 3. Tres formas de representar un Árbol Binario
1. **Con nexos / punteros (`BTNode<T>`):** cada nodo guarda `value`, `left*` y `right*`.
2. **En base a arreglos (indexado desde 1):**
   - Nodos numerados por niveles de izquierda a derecha.
   - Hijo izquierdo de `i`: **`2 * i`** · Hijo derecho de `i`: **`2 * i + 1`** · Padre de `i`: **`i / 2`**.
3. **Con lista de nodos (tabla):** cada fila guarda `(valor, indiceIzq, indiceDer)`.

---

### 4. Los 4 Recorridos de un Árbol Binario
Para el árbol `[40, 8, 80, 12, 67, 102]`:

| Recorrido | Regla | Resultado | Uso típico |
| :--- | :--- | :--- | :--- |
| **Pre-orden** | **Nodo** → Izquierda → Derecha | `40, 8, 12, 80, 67, 102` | Clonar / serializar estructura |
| **In-orden** | Izquierda → **Nodo** → Derecha | `8, 12, 40, 67, 80, 102` | Orden ascendente en ABB |
| **Post-orden** | Izquierda → Derecha → **Nodo** | `12, 8, 67, 102, 80, 40` | Liberar memoria (`delete`) sin perder hijos |
| **Por nivel (BFS)** | Nivel 1, Nivel 2, ... (con `queue`) | `40, 8, 80, 12, 67, 102` | Caminos mínimos / validar completo |

---

## Cómo continuar en este módulo

1. **Primero ve a [`01_Practica_y_Apuntes/`](01_Practica_y_Apuntes/apuntes.md):** anota definiciones, dibuja recorridos y arma tu primer árbol binario paso a paso desde una plantilla mínima.
2. **Luego pasa a [`02_Enunciados/`](02_Enunciados/README.md):** resuelve los enunciados escalados (Nivel 1 → Nivel 2 → Nivel 3) con su plantilla de pruebas.
