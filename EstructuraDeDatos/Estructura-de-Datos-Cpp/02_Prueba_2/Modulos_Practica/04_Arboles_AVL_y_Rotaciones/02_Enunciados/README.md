# Enunciados Escalados — Módulo 04 (Árboles AVL)

[Volver a Contenidos](../README.md) · [Volver a Práctica y Apuntes](../01_Practica_y_Apuntes/apuntes.md) · [Plantilla de Enunciados](Main.cpp)

---

## Parte Teórica (Trazado en papel)
Inserta uno por uno en un AVL vacío: **`10, 20, 30, 15, 25, 5, 1`**.
Para cada paso en que ocurra un desbalance:
1. Indica qué nodo alcanzó `|FB| == 2` y qué caso es (**LL, RR, LR, RL**).
2. Dibuja el árbol resultante después de rotar.

---

## Nivel 1 — Básico (Altura, Factor de Balance y Rotaciones Simples)
En `Main.cpp`, implementa en `ArbolAVL`:
1. `int altura(const NodoAVL* n) const` y `void actualizarAltura(NodoAVL* n)`
2. `int obtenerFB(const NodoAVL* n) const`
3. `NodoAVL* rotarDerecha(NodoAVL* z)` y `NodoAVL* rotarIzquierda(NodoAVL* z)`

---

## Nivel 2 — Intermedio (Balanceo completo e Inserción AVL)
Implementa:
1. `NodoAVL* balancear(NodoAVL* nodo)`: detecta los 4 casos (`LL, RR, LR, RL`) y aplica la rotación correspondiente.
2. `NodoAVL* insertarNodo(NodoAVL* nodo, int clave, bool& insertado)`: inserta sin duplicados y rebalancea al regresar por la recursión.

Prueba con `{10, 20, 30, 15, 25, 5, 1}` y comprueba que `verificarAVL()` retorne `true` y la altura sea `4`.

---

## Nivel 3 — Reto (Eliminación AVL con rebalanceo y prueba de estrés)
Implementa:
```cpp
NodoAVL* eliminarNodo(NodoAVL* nodo, int clave, bool& eliminado);
```
eliminando hoja, 1 hijo o 2 hijos (usando sucesor inorden) y llamando a `balancear(nodo)` al subir por cada ancestro.

Comprueba con el caso de estrés ascendente `1..15`: en un ABB normal daría altura `15`, pero tu AVL debe tener **altura `4`** y **`verificarAVL() == true`**.

---

## Resultados esperados en `Main.cpp`

| Nivel | Prueba | Esperado |
| :--- | :--- | :--- |
| 1–2 | Insertar `10, 20, 30, 15, 25, 5, 1` | `verificarAVL() == true`, altura `4`, inorden `1 5 10 15 20 25 30` |
| 2 | Insertar duplicado `20` | `false` |
| 3 | `eliminar(20)` y `eliminar(30)` | ambos `true`, `verificarAVL() == true` |
| 3 | Estrés ascendente `1..15` | `verificarAVL() == true`, altura `4` |
