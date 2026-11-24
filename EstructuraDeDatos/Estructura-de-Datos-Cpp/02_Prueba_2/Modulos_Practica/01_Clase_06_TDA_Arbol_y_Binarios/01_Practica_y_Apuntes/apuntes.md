# Apuntes y Práctica Guiada — Clase 06 (TDA Árbol y Binarios)

[Volver a Contenidos](../README.md) · [Código de práctica](Main.cpp) · [Ir a Enunciados](../02_Enunciados/README.md)

---

## Mis apuntes de clase

### 1. Diferencia entre Altura y Profundidad (según Clase 06)
> *(Anota aquí desde dónde se cuenta cada una y cuál es el nivel de la raíz...)*

### 2. Isomorfos vs Semejantes / Lleno vs Completo
> *(Anota con un mini dibujo cuándo un árbol es completo pero NO lleno...)*

### 3. Regla mnemotécnica para los 4 recorridos
```text
Pre-orden  : __ -> __ -> __
In-orden   : __ -> __ -> __
Post-orden : __ -> __ -> __
Por nivel  : usa estructura ______
```

### 4. Fórmulas en arreglo base 1
- Hijo izquierdo de `i`: `____`
- Hijo derecho de `i`: `____`
- Padre de `i`: `____`

---

## Guía paso a paso (para programar en `Main.cpp`)

Construye tu código en `Main.cpp` de a **un paso por vez**:

1. **Paso 1 — Crear el nodo mínimo:** define un `struct Nodo` simple (`int dato; Nodo* izq; Nodo* der;` y un constructor).
2. **Paso 2 — Armar un árbol de 3 o 5 nodos a mano:** en `main()`, reserva nodos con `new` y conéctalos (`raiz->izq = ...`, `raiz->der = ...`).
3. **Paso 3 — Un recorrido a la vez:** escribe primero `preorden(const Nodo* n)`. Compila y comprueba. Luego escribe `inorden` y `postorden` cambiando solo dónde va el `cout`.
4. **Paso 4 — Liberar memoria:** escribe `liberar(Nodo* n)` en **post-orden** (¿qué pasa si haces `delete n` antes de liberar los hijos?).
5. **Paso 5 — Recorrido por nivel (BFS):** agrega `#include <queue>` y escribe `porNivel(const Nodo* raiz)` paso a paso.
