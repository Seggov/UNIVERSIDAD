# Módulo 04 — Árboles AVL, Factor de Balance y Rotaciones

**Referencia en el repo:** [02_Prueba_2/README.md](../../README.md) · [ArbolAVL.cpp del Taller 2](../../Talleres/Taller-2_Hospital/src/ArbolAVL.cpp)  
**Práctica orientativa:** 2.5–3 horas.

[Resumen Prueba 2](../README.md) · [Práctica y Apuntes](01_Practica_y_Apuntes/apuntes.md) · [Enunciados Escalados](02_Enunciados/README.md) · [Siguiente: Simulacro](../05_Simulacro_Prueba_2/README.md)

---

## Contenidos

### 1. ¿Por qué necesitamos Árboles AVL?
En un ABB común, insertar valores ordenados (`10, 20, 30, 40, 50`) forma una lista inclinada de altura $n$, degradando búsquedas a **$O(n)$**.  
Un **Árbol AVL** mantiene la altura en **$O(\log n)$** garantizando en todo nodo $N$:

$$\text{FB}(N) = \text{altura}(N.\text{izq}) - \text{altura}(N.\text{der}) \in \{-1, 0, +1\}$$

- Convención: `altura(nullptr) = 0`, hoja = `1`, `altura(N) = 1 + max(altura(izq), altura(der))`.

---

### 2. Los 4 casos de desbalance y sus rotaciones

| Caso | Condición | Rotación |
| :--- | :--- | :--- |
| **LL** | $\text{FB}(Z) > +1$ y $\text{FB}(Z.\text{izq}) \ge 0$ | **Simple Derecha (`rotarDerecha(Z)`)** |
| **RR** | $\text{FB}(Z) < -1$ y $\text{FB}(Z.\text{der}) \le 0$ | **Simple Izquierda (`rotarIzquierda(Z)`)** |
| **LR** | $\text{FB}(Z) > +1$ y $\text{FB}(Z.\text{izq}) < 0$ | **Doble Izq–Der:** `Z.izq = rotarIzquierda(Z.izq)`, luego `rotarDerecha(Z)` |
| **RL** | $\text{FB}(Z) < -1$ y $\text{FB}(Z.\text{der}) > 0$ | **Doble Der–Izq:** `Z.der = rotarDerecha(Z.der)`, luego `rotarIzquierda(Z)` |

```text
Rotación Simple Derecha (LL):
          (Z) FB=+2                      (Y) FB=0
         /   \                          /   \
       (Y)   [T3]    rotarDerecha     (X)   (Z)
       / \              =====>               / \
     (X) [T2]                             [T2] [T3]
```

> **Regla crítica al rotar:** actualiza **primero** la altura de `Z` (el nodo que bajó) y **después** la altura de `Y` (la nueva raíz).

---

## Cómo continuar en este módulo

1. **Primero ve a [`01_Practica_y_Apuntes/`](01_Practica_y_Apuntes/apuntes.md):** dibuja cada rotación en tus apuntes y practica `rotarDerecha` / `rotarIzquierda` sobre 3 nodos sueltos antes de programar la clase completa.
2. **Luego pasa a [`02_Enunciados/`](02_Enunciados/README.md):** resuelve los niveles escalados (Nivel 1 rotaciones y `FB` → Nivel 2 inserción AVL → Nivel 3 eliminación con rebalanceo y prueba de estrés).
