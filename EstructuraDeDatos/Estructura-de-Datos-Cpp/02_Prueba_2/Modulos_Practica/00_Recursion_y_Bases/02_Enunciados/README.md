# Enunciados Escalados — Módulo 00 (Recursión)

[Volver a Contenidos](../README.md) · [Volver a Práctica y Apuntes](../01_Practica_y_Apuntes/apuntes.md) · [Plantilla de Enunciados](Main.cpp)

Resuelve en orden **Nivel 1 → Nivel 2 → Nivel 3** dentro de `Main.cpp`.

---

## Nivel 1 — Básico (un solo subproblema lineal)
Implementa:
1. `int sumarHasta(int n)`: retorna $1 + 2 + \dots + n$. Si `n <= 0`, retorna `0`.
2. `int sumarDigitos(int n)`: suma los dígitos de un entero (si es negativo, usa su valor absoluto; si es `0`, retorna `0`).

**Ejemplo:** `sumarHasta(5) == 15` | `sumarDigitos(482) == 14`.

---

## Nivel 2 — Intermedio (arreglos y condiciones)
Implementa:
1. `int contarOcurrencias(const int* arr, int n, int objetivo)`: cuenta cuántas veces aparece `objetivo` en `arr`. Si `arr == nullptr || n <= 0`, retorna `0`.
2. `bool estaOrdenado(const int* arr, int n)`: retorna `true` si el arreglo está en orden no decreciente (`arr[0] <= arr[1] <= ...`). Un arreglo de `0` o `1` elementos está ordenado.

**Casos borde:** arreglo nulo, `n == 0`, `n == 1`, elementos repetidos `{1, 2, 2, 5}` → `true`.

---

## Nivel 3 — Reto (bifurcación en nodos binarios)
Dado el `struct Nodo` de `Main.cpp` (`valor`, `left`, `right`), implementa:
1. `int contarNodos(const Nodo* root)`: total de nodos.
2. `int sumarNodos(const Nodo* root)`: suma de valores.
3. `bool contiene(const Nodo* root, int objetivo)`: retorna `true` si `objetivo` aparece en algún subárbol (**no** asumas que está ordenado).
4. `int maximoArbol(const Nodo* root)`: retorna el valor máximo del árbol (si es `nullptr`, retorna `INT_MIN`; cuida que funcione con números negativos).

---

## Resultados esperados

| Nivel | Prueba | Esperado |
| :--- | :--- | :--- |
| 1 | `sumarHasta(5)` / `sumarDigitos(-482)` | `15` / `14` |
| 2 | `contarOcurrencias({3,1,3,5,3}, 5, 3)` | `3` |
| 2 | `estaOrdenado({1,2,2,5}, 4)` / `({1,4,2,5}, 4)` | `true` / `false` |
| 3 | `contarNodos(root)` / `sumarNodos(root)` | `4` / `37` |
| 3 | `contiene(root, 20)` / `contiene(root, 99)` | `true` / `false` |
| 3 | `maximoArbol(negativos)` (`-10 -> -5, -20`) | `-5` |

**Para avanzar:** todas las pruebas en `Main.cpp` coinciden y explicas la complejidad $O(n)$ en tiempo y $O(h)$ en pila para árboles.
