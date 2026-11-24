# Enunciados Escalados — Clase 06 (TDA Árbol y Binarios)

[Volver a Contenidos](../README.md) · [Volver a Práctica y Apuntes](../01_Practica_y_Apuntes/apuntes.md) · [Plantilla de Enunciados](Main.cpp)

---

## Parte Teórica (Trazado en papel antes de compilar)
Dado este árbol binario:

```text
            (A)
           /   \
         (B)   (C)
        /     /   \
      (D)   (E)   (F)
        \     \
        (G)   (H)
```

1. Indica: altura del árbol (raíz = nivel 1), profundidad de `H`, grado de `B` y lista de hojas.
2. ¿Es lleno? ¿Es completo? Justifica.
3. Escribe sus recorridos **Pre-orden**, **In-orden**, **Post-orden** y **Por nivel**.
4. Escribe los índices de `A..H` en un arreglo indexado desde `1`.

*(Clave rápida: altura 4, prof(H)=3, hojas G/H/F, Pre: `A B D G C E H F`, In: `D G B A E H C F`, Post: `G D B H E F C A`, Nivel: `A B C D E F G H`, índices base 1: `A:1, B:2, C:3, D:4, E:6, F:7, G:9, H:13`).*

---

## Nivel 1 — Básico (los 4 recorridos sobre `BTNode<int>`)
Completa en `Main.cpp`:
1. `void preorden(const BTNode<int>* root)`
2. `void inorden(const BTNode<int>* root)`
3. `void postorden(const BTNode<int>* root)`
4. `void porNivel(const BTNode<int>* root)` (usando `std::queue`)

---

## Nivel 2 — Intermedio (conteos y representación en arreglo)
Implementa:
1. `int contarHojas(const BTNode<int>* root)`: cuenta los nodos sin hijos (`left == nullptr && right == nullptr`).
2. `int contarEnNivel(const BTNode<int>* root, int nivelObjetivo)`: cuenta cuántos nodos hay en el nivel `nivelObjetivo` (raíz = nivel 1). Si `root == nullptr` o `nivelObjetivo < 1`, retorna `0`.
3. `void inordenArreglo(const std::vector<int>& tree, int idx)`: recorre en in-orden un árbol almacenado en un vector **indexado desde 1** (`-1` significa vacío), usando `2 * idx` y `2 * idx + 1`.

---

## Nivel 3 — Reto (propiedades estructurales y comparación)
Implementa:
1. `bool esLleno(const BTNode<int>* root)`: retorna `true` si todo nivel presente está completamente lleno (0 o 2 hijos y todas las hojas al mismo nivel; árbol vacío se considera `true`).
2. `bool sonIsomorfos(const BTNode<int>* a, const BTNode<int>* b)`: retorna `true` si dos árboles tienen exactamente la **misma estructura**, sin importar los valores de sus nodos.

---

## Resultados esperados en `Main.cpp`

| Nivel | Prueba | Esperado |
| :--- | :--- | :--- |
| 1 | `preorden` / `inorden` / `postorden` / `porNivel` | `40 8 12 80 67 102` / `8 12 40 67 80 102` / `12 8 67 102 80 40` / `40 8 80 12 67 102` |
| 2 | `contarHojas(root)` / `contarEnNivel(root, 3)` | `3` / `3` |
| 2 | `inordenArreglo({-1, 20, 12, 61, 33, 48, 81}, 1)` | `33 12 48 20 81 61` |
| 3 | `esLleno(root)` / `esLleno(lleno)` | `false` / `true` |
| 3 | `sonIsomorfos(lleno, lleno2)` / `sonIsomorfos(lleno, root)` | `true` / `false` |
