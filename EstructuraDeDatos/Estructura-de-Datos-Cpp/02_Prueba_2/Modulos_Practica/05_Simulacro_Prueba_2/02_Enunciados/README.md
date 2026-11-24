# Simulacro Completo — Enunciados y Evaluación (76 pts)

[Volver a Contenidos](../README.md) · [Volver a Apuntes](../01_Practica_y_Apuntes/apuntes.md) · [Plantilla de Enunciados](Main.cpp)

**Tiempo sugerido:** 90–120 minutos continuos (Parte 1: 20 min · Parte 2: 30 min · Parte 3: 50 min).

---

## Parte 1 — Selección Múltiple (16 pts)

1. **(2 pts)** En un árbol binario de profundidad/altura $K = 5$ (raíz = nivel 1), ¿cuál es el número **máximo** de nodos que puede tener el nivel 4, y el máximo de nodos **totales** del árbol?
   - a) $8$ y $31$ · b) $16$ y $32$ · c) $8$ y $32$ · d) $16$ y $31$
2. **(2 pts)** ¿Qué recorrido libera correctamente nodos dinámicos sin perder direcciones de los hijos?
   - a) Pre-orden · b) In-orden · c) Post-orden · d) Por nivel sin cola
3. **(2 pts)** Dos árboles $T_1$ y $T_2$ tienen las mismas claves `{10, 20, 30, 40}`, pero $T_1$ tiene altura $4$ y $T_2$ altura $3$. Son:
   - a) Isomorfos · b) Semejantes · c) Llenos · d) Completos
4. **(2 pts)** Un árbol completo de 6 nodos en arreglo base 1 es `[-, A, B, C, D, E, F]`. ¿Quién es el padre de `F` y el hijo izquierdo de `C`?
   - a) Padre `C`; izq de `C` es `F` · b) Padre `B`; izq de `C` es `E` · c) Padre `C`; sin izq · d) Padre `A`; izq `F`
5. **(2 pts)** En un Árbol Binario Enhebrado In-orden, si `X` tiene `rightThread == true` y `right == Y`, ¿qué es `Y`?
   - a) Hijo derecho real · b) Predecesor inorden · c) Sucesor inorden · d) Padre directo
6. **(2 pts)** En `ABB::remove` con 2 hijos usando el menor del subárbol derecho $S$, ¿qué cumple $S$?
   - a) Siempre es hoja · b) `S->left == nullptr`, pero puede tener hijo derecho · c) `S->right == nullptr` · d) Tiene 2 hijos
7. **(2 pts)** En un AVL, si $\text{FB}(Z) = +2$ y $\text{FB}(Z.\text{izq}) = -1$, la rotación es:
   - a) `LL` · b) `RR` · c) `LR` · d) `RL`
8. **(2 pts)** Peor caso de búsqueda en ABB no balanceado vs AVL:
   - a) $O(\log n)$ y $O(\log n)$ · b) $O(n)$ y $O(\log n)$ · c) $O(n \log n)$ y $O(n)$ · d) $O(1)$ y $O(\log n)$

---

## Parte 2 — Trazado en Papel (20 pts)

1. **(12 pts)** Inserta **`35, 15, 50, 10, 25, 20`**:
   - Dibuja el **ABB simple** y escribe sus 4 recorridos (**Pre**, **In**, **Post**, **Por nivel**).
   - Inserta la misma secuencia en un **AVL vacío**: indica qué inserción desbalancea, los `FB`, la rotación aplicada y el árbol final.
2. **(8 pts)** En el ABB simple anterior, muestra el árbol tras `remove(15)` (sucesor inorden). Luego dibuja las hebras In-orden del árbol `M` (`G` con `B, J`; `T` con izq `P`).

---

## Parte 3 — Programación Escalada en C++ (40 pts)

Completa en `Main.cpp`:

### Nivel 1 (10 pts) — Conteo estructural
`int contarConUnSoloHijo(const TNode* root)`: retorna cuántos nodos tienen **exactamente un hijo**.

### Nivel 2 (15 pts) — Poda eficiente en ABB
`int sumarEnRangoABB(const TNode* root, int low, int high)`: suma los valores en `[low, high]` **podando ramas imposibles** según la propiedad de orden del ABB.

### Nivel 3 (15 pts) — Validación de Árbol Binario Completo
`bool esArbolCompleto(const TNode* root)`: retorna `true` si el árbol binario es **completo** (*complete*: nivel $L$ compactado a la izquierda, sin huecos antes de nodos existentes). *(Pista: BFS con `std::queue` detectando si aparece un nodo válido después de haber visto un `nullptr`).*

---

## Clave rápida (desplegar al terminar)

<details>
<summary>Soluciones Parte 1 y Parte 2</summary>

- **Parte 1:** `1.a`, `2.c`, `3.b`, `4.a`, `5.c`, `6.b`, `7.c`, `8.b`.
- **Parte 2 (ABB):** `35` raíz; izq `15` (`10`, `25 -> izq 20`); der `50`.
  - Pre: `35 15 10 25 20 50` | In: `10 15 20 25 35 50` | Post: `10 20 25 15 50 35` | Nivel: `35 15 50 10 25 20`.
- **Parte 2 (AVL):** al insertar `20`, `FB(35) = +2` y `FB(15) = -1` (**LR**): `rotIzq(15)` luego `rotDer(35)` → raíz `25`, izq `15` (`10`, `20`), der `35` (`50`).
- **Parte 2 (`remove(15)`):** sube `20` en lugar de `15`.

</details>
