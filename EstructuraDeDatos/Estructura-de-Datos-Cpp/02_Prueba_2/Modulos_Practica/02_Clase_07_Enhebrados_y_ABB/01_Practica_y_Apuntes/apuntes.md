# Apuntes y Práctica Guiada — Clase 07 (Enhebrados y ABB)

[Volver a Contenidos](../README.md) · [Código de práctica](Main.cpp) · [Ir a Enunciados](../02_Enunciados/README.md)

---

## Mis apuntes de clase

### 1. ¿Para qué sirven `leftThread` y `rightThread`?
> *(Anota aquí qué significa `true` vs `false` y por qué ahorra memoria al recorrer...)*

### 2. Regla de inserción en Árbol Enhebrado
> *(¿Qué pasa cuando insertas un hijo donde antes había una hebra?...)*

### 3. Los 3 casos de `remove` en un ABB
```text
Caso 1 (0 hijos):
Caso 2 (1 hijo) :
Caso 3 (2 hijos):
```

### 4. ¿Por qué NO basta comprobar solo `izq->val < nodo->val < der->val` para validar un ABB?
> *(Dibuja un contra-ejemplo rápido de 4 nodos donde los hijos locales cumplen pero el árbol NO es ABB válido...)*

---

## Guía paso a paso (para programar en `Main.cpp`)

Avanza de a un paso, probando en consola cada avance:

1. **Paso 1 — Nodo ABB y función `insertar`:** crea un `struct Nodo` (`dato`, `izq`, `der`) y escribe `Nodo* insertar(Nodo* r, int x)` recursivo (o iterativo). Inserta `{43, 28, 87, 31, 63, 104, 74}` e imprime su **in-orden** para ver que sale ordenado.
2. **Paso 2 — Búsqueda `buscar`:** implementa `bool buscar(const Nodo* r, int x)` aprovechando `x < r->dato` o `x > r->dato` (sin recorrer todo el árbol).
3. **Paso 3 — Eliminación por pasos (`eliminar`):**
   - Primero implementa solo **Caso 1 (hoja)** y **Caso 2 (1 hijo)**, y pruébalo eliminando `31` y `63`.
   - Luego agrega el **Caso 3 (2 hijos)** buscando el menor del subárbol derecho (`while (suc->izq != nullptr)`) y pruébalo eliminando `87` y luego `43` (¡la raíz!).
4. **Paso 4 — Hebras en papel y código:** dibuja primero en papel qué hebra apunta a qué nodo en `[A, B, C, D, E]`, y recién después programa `inordenEnhebrado` en un `struct TBTNode` pequeño.
