# Enunciados Escalados — Clase 07 (Enhebrados y ABB)

[Volver a Contenidos](../README.md) · [Volver a Práctica y Apuntes](../01_Practica_y_Apuntes/apuntes.md) · [Plantilla de Enunciados](Main.cpp)

---

## Parte Teórica (Trazado en papel)
1. Inserta en un ABB vacío: `50, 30, 70, 20, 40, 60, 80, 65`.
2. Dibuja el resultado tras ejecutar en orden: `remove(20)`, `remove(60)` y `remove(50)` (usando sucesor inorden).
3. En un árbol con raíz `A`, hijo izq `B` (hijos `D, E`) e hijo der `C` (hijo izq `F`), escribe adónde apunta cada puntero cuando `leftThread == true` o `rightThread == true`.

---

## Nivel 1 — Básico (Inserción, Búsqueda y Extremos en ABB)
Completa en la clase `ABB` de `Main.cpp`:
1. `bool insert(int value)`: inserta sin permitir duplicados (`false` si ya existía, `true` si insertó).
2. `bool find(int value) const`: retorna `true` si existe.
3. `int minimo() const` y `int maximo() const`: retornan el menor y el mayor valor del ABB (`INT_MIN` si está vacío).
4. `void inorden(std::vector<int>& out) const`: guarda los valores ordenados en `out`.

---

## Nivel 2 — Intermedio (Eliminación segura y Validación)
Implementa:
1. `bool remove(int value)`: elimina un valor manejando **todos** los casos:
   - valor inexistente (`false`),
   - hoja,
   - 1 hijo,
   - 2 hijos (incluyendo cuando el nodo a eliminar es `root`, y cuando el sucesor inorden tiene un hijo derecho!).
2. `bool esABBValido() const`: verifica con cotas `(minVal, maxVal)` que cada nodo cumpla estrictamente `minVal < nodo->value < maxVal`.

---

## Nivel 3 — Reto (Recorrido Enhebrado Iterativo en $O(1)$ espacio)
Implementa:
```cpp
void inordenEnhebrado(const TBTNode* root);
```
que imprima el recorrido In-orden del árbol enhebrado armado en `Main.cpp`, **sin usar recursión ni `std::stack`**, guiándote únicamente por `leftThread` y `rightThread`.

---

## Resultados esperados en `Main.cpp`

| Nivel | Prueba | Esperado |
| :--- | :--- | :--- |
| 1 | `insert(40)` duplicado / `minimo()` / `maximo()` | `false` / `20` / `80` |
| 1 | `inorden` inicial | `20 30 40 50 60 65 70 80` |
| 2 | `remove(20)` → `remove(60)` → `remove(50)` + `inorden` | `30 40 65 70 80` |
| 2 | `esABBValido()` después de eliminar la raíz `50` | `true` |
| 3 | `inordenEnhebrado(&a)` | `D B E A F C` |
