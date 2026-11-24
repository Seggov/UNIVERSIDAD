# Apuntes y Práctica Guiada — Clase 07.1 (Ejercicios de Árboles)

[Volver a Contenidos](../README.md) · [Código de práctica](Main.cpp) · [Ir a Enunciados](../02_Enunciados/README.md)

---

## Mis apuntes de clase

### 1. ¿Por qué NO sirve hacer `(average(left) + average(right) + val) / 3`?
> *(Anota aquí qué pasa si un subárbol tiene 10 nodos y el otro 1...)*

### 2. ¿Cómo funciona el Backtracking en `calcMaxSum`?
```text
Al entrar a un nodo:   ______________________________
Al detectar una hoja:  ______________________________
Al salir del nodo:     ______________________________
```

### 3. Caso trampa de prueba: ¿qué pasa si un nodo tiene 1 solo hijo y el otro es `nullptr`?
> *(¿Es ese nodo una hoja? ¿Debe parar ahí `calcMaxSum`?...)*

---

## Guía paso a paso (para programar en `Main.cpp`)

1. **Paso 1 — Crea un `TNode` mínimo** (`char id; int val; TNode* left; TNode* right;`) y arma un árbol pequeño de 3–4 nodos en `main()`.
2. **Paso 2 — Helper con `&`:** escribe `void contarYSumar(TNode* r, int& suma, int& cnt)` y úsalo para calcular el promedio. Prueba con `nullptr` para verificar que no divida por cero.
3. **Paso 3 — Altura paso a paso:** escribe `int altura(TNode* r)` e imprime el retorno en un árbol de 1 nodo y en uno inclinado de 3 nodos.
4. **Paso 4 — Imprimir todas las rutas raíz-a-hoja:** antes de buscar el máximo, escribe `void mostrarRutas(TNode* r, vector<char>& ruta)` haciendo `ruta.push_back(r->id)` al entrar y `ruta.pop_back()` al salir. Cuando veas que imprime cada rama limpia, agrégale la suma y la comparación con `maxValue`.
