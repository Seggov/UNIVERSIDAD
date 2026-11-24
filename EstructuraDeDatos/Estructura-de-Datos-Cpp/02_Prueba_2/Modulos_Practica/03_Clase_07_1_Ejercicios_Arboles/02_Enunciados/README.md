# Enunciados Escalados — Clase 07.1 (Ejercicios Oficiales)

[Volver a Contenidos](../README.md) · [Volver a Práctica y Apuntes](../01_Practica_y_Apuntes/apuntes.md) · [Plantilla de Enunciados](Main.cpp)

---

## Nivel 1 — Básico (Ejercicios 1 y 2 oficiales de Clase 07.1)
Implementa en `Main.cpp`:
1. `float average(TNode* root)`: devuelve el promedio de todos los valores del árbol. Si `root == nullptr`, devuelve `0.0f`.
2. `int getMaxHeight(TNode* root)`: devuelve la altura/profundidad máxima (raíz = nivel 1; vacío = `0`).

---

## Nivel 2 — Intermedio (Ejercicio 3 oficial de Clase 07.1)
Implementa:
```cpp
void calcMaxSum(TNode* root, int& maxValue, std::vector<char>& maxPath);
```
que calcule la suma máxima entre **todas las ramas raíz-a-hoja** y deje en `maxValue` el valor máximo y en `maxPath` la ruta de etiquetas (`'A', 'B', ...`).

**Requisitos clave:**
- Si `root == nullptr`: deja `maxValue = 0` y `maxPath.clear()`.
- Funciona correctamente incluso si **todos los valores del árbol son negativos**.
- No te detengas en nodos con 1 solo hijo: solo las hojas (`left == nullptr && right == nullptr`) cierran una rama.

---

## Nivel 3 — Reto (Variantes de prueba sobre ramas)
Implementa:
1. `bool existeSumaCamino(TNode* root, int objetivo)`: retorna `true` si existe alguna rama completa desde la raíz hasta una hoja cuya suma sea igual a `objetivo`.
2. `int sumaHojasIzquierdas(TNode* root)`: suma únicamente los valores de las **hojas que son hijo izquierdo** de su padre.

---

## Resultados esperados en `Main.cpp`

| Nivel | Prueba | Esperado |
| :--- | :--- | :--- |
| 1 | `average(nullptr)` / `average(root)` | `0` / `6.11111` |
| 1 | `getMaxHeight(nullptr)` / `getMaxHeight(root)` | `0` / `4` |
| 2 | `calcMaxSum(root)` | `27` y ruta `A B D G` |
| 2 | `calcMaxSum(neg)` (`-10 -> -5, -20`) | `-15` y ruta `X Y` |
| 3 | `existeSumaCamino(root, 22)` / `(root, 9)` | `true` / `false` (9 es prefijo `5+4`, no llega a hoja!) |
| 3 | `sumaHojasIzquierdas(root)` | `20` (`G(7) + E(13)`) |
