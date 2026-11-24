# Módulo 03 (Clase 07.1) — Ejercicios Oficiales de Árboles Binarios

**Fuente oficial:** [07.1 - [U4] Ejercicios Árboles.pdf](../../Material_Teorico/07.1%20-%20%5BU4%5D%20Ejercicios%20%C3%81rboles.pdf)  
**Práctica orientativa:** 1.5–2 horas.

[Resumen Prueba 2](../README.md) · [Práctica y Apuntes](01_Practica_y_Apuntes/apuntes.md) · [Enunciados Escalados](02_Enunciados/README.md) · [Siguiente: Árboles AVL](../04_Arboles_AVL_y_Rotaciones/README.md)

---

## Contenidos de la Clase 07.1

En esta clase se resuelven tres problemas tipo certamen sobre `TNode*`, combinando recursión, múltiples datos de retorno por referencia y backtracking sobre ramas completas.

### Patrones clave

| Problema | Patrón de diseño | Cuidado / Caso borde |
| :--- | :--- | :--- |
| **`float average(TNode* root)`** | Helper recursivo `void aux(TNode*, int& suma, int& cont)` + división `static_cast<float>(suma) / cont` al final | Si `root == nullptr` (`cont == 0`), retornar `0.0f` sin dividir por cero |
| **`int getMaxHeight(TNode* root)`** | Recursión de abajo hacia arriba: `1 + max(hIzq, hDer)` | Si `root == nullptr`, retornar `0` (raíz = nivel 1, hoja = 1) |
| **`void calcMaxSum(TNode* root, int& maxValue, vector<char>& maxPath)`** | DFS pasando suma/ruta actual y actualizando `maxValue`/`maxPath` al llegar a una **hoja** (`!left && !right`), haciendo `pop_back()` al subir | Inicializar `maxValue = INT_MIN` (por si existen valores negativos) |

### Árbol de referencia para trazar

```text
            [5] (A)
           /       \
       [4] (B)     [8] (C)
       /           /     \
   [11] (D)    [13] (E)  [4] (F)
    /    \                  \
 [7](G) [2](H)             [1](I)
```

- **Suma total:** $55$, **Nodos:** $9$ → **`average` = `6.111...`**
- **Altura máxima:** **`4`** (`A -> B -> D -> G`)
- **Ramas raíz-hoja:** `27` (`A B D G`, ganadora), `22` (`A B D H`), `26` (`A C E`), `18` (`A C F I`).

---

## Cómo continuar en este módulo

1. **Primero ve a [`01_Practica_y_Apuntes/`](01_Practica_y_Apuntes/apuntes.md):** practica por separado cómo sumar/contar con referencias y cómo hacer `push_back`/`pop_back` en un árbol chiquito de 3 nodos antes de ir a los enunciados completos.
2. **Luego pasa a [`02_Enunciados/`](02_Enunciados/README.md):** resuelve los enunciados escalados (Nivel 1 `average` y `getMaxHeight` → Nivel 2 `calcMaxSum` → Nivel 3 variantes de prueba).
