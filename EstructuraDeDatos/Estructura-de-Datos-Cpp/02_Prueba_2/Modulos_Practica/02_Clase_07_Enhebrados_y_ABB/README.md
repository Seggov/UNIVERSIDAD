# Módulo 02 (Clase 07) — Árboles Binarios Enhebrados y ABB

**Fuente oficial:** [07 - [U4] Árboles Binarios Enhebrados, ABB.pdf](../../Material_Teorico/07%20-%20%5BU4%5D%20%C3%81rboles%20Binarios%20Enhebrados,%20ABB.pdf)  
**Práctica orientativa:** 2–3 horas.

[Resumen Prueba 2](../README.md) · [Práctica y Apuntes](01_Practica_y_Apuntes/apuntes.md) · [Enunciados Escalados](02_Enunciados/README.md) · [Siguiente: Clase 07.1](../03_Clase_07_1_Ejercicios_Arboles/README.md)

---

## Contenidos de la Clase 07

### 1. Árboles Binarios Enhebrados (*Threaded Binary Trees*)
En un árbol binario normal con $n$ nodos hay $n + 1$ punteros `nullptr` desperdiciados. Un **árbol enhebrado** reutiliza esos punteros para apuntar al **predecesor** (`left`) o al **sucesor** (`right`) según el recorrido **In-orden**, permitiendo recorrer todo el árbol sin recursión y sin pila ($O(1)$ espacio auxiliar).

```text
Nodo TBTNode<T>:
+------------+-------+-------+--------+-------------+
| leftThread | left  | value | right  | rightThread |
|   (bool)   | (ptr) |  (T)  | (ptr)  |   (bool)    |
+------------+-------+-------+--------+-------------+

Ejemplo In-orden (D, B, E, A, F, C):
             (A)
            /   \
          (B)   (C)
         /  \   /
       (D) (E) (F)

- thread == false -> hijo real
- thread == true  -> hebra hacia predecesor (left) o sucesor (right)
```

**Pasos del recorrido In-orden iterativo ($O(1)$ espacio):**
1. Desde `root`, baja siempre por `left` mientras `leftThread == false`.
2. Procesa/imprime `actual`.
3. Si `rightThread == true`, avanza por la hebra `actual = actual->right` (sucesor directo).
4. Si `rightThread == false`, entra a `actual = actual->right` y vuelve al paso 1.

---

### 2. Árboles Binarios de Búsqueda (ABB / BST)
Un ABB cumple en **todo nodo $N$** la invariante:
- Todos los valores del subárbol izquierdo son **menores** a $N$.
- Todos los valores del subárbol derecho son **mayores** a $N$.

```text
          (43)
         /    \
      (28)    (87)         In-orden SIEMPRE sale ordenado:
         \    /   \        28, 31, 43, 63, 74, 87, 104
        (31)(63) (104)
               \
               (74)
```

- **Complejidad:** $O(\log n)$ promedio cuando está equilibrado; **$O(n)$** en el peor caso (cuando se insertan datos ordenados y se degenera en una lista).

---

### 3. Operaciones del ABB: `find`, `insert` y `remove`

- **`find` e `insert`:** bajan comparando con la raíz. Los valores nuevos se insertan siempre como hojas; si ya existe, se omite (no hay duplicados).
- **`remove` (3 casos):**
  1. **Hoja (0 hijos):** se elimina y el padre pasa a apuntar a `nullptr`.
  2. **1 hijo:** el padre pasa a apuntar directamente al único hijo.
  3. **2 hijos:** se reemplaza por el **menor del subárbol derecho** (sucesor inorden) o el **mayor del subárbol izquierdo** (predecesor inorden).

> **¡Dos errores clásicos de prueba en `ABB::remove`!**
> 1. No actualizar `root` cuando se elimina la raíz (`prev == nullptr`).
> 2. Olvidar reconectar el posible hijo derecho del sucesor inorden cuando el sucesor sube a ocupar el lugar del nodo eliminado.

---

## Cómo continuar en este módulo

1. **Primero ve a [`01_Practica_y_Apuntes/`](01_Practica_y_Apuntes/apuntes.md):** practica paso a paso primero `insert`/`find`, luego `remove` caso por caso y finalmente el trazado de hebras.
2. **Luego pasa a [`02_Enunciados/`](02_Enunciados/README.md):** resuelve los niveles **1 → 2 → 3** con la batería completa de casos borde.
