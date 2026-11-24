# Apuntes y Práctica Guiada — Módulo 00 (Recursión)

[Volver a Contenidos](../README.md) · [Código de práctica](Main.cpp) · [Ir a Enunciados](../02_Enunciados/README.md)

---

## Mis apuntes de clase

### 1. ¿Qué es un caso base y qué pasa si falta?
> *(Anota aquí con tus palabras...)*

### 2. ¿Cómo funciona la pila de llamadas (call stack)?
```text
Dibuja o anota la traza de cuentaRegresiva(3):
- Bajada:
- Subida:
```

### 3. Diferencia entre pasar por valor vs por referencia (`&`) en recursión
> *(Anota un ejemplo de cuándo te conviene cada uno...)*

---

## Guía paso a paso (para programar en `Main.cpp`)

Avanza **un paso a la vez**, compilando y probando antes de pasar al siguiente:

1. **Paso 1 — Ver la bajada y subida:** escribe `void trazar(int n)` que imprima `"baja " << n` antes de llamarse con `n - 1`, y `"sube " << n` después de llamarse. Observa el orden en consola.
2. **Paso 2 — Acumular retorno:** escribe `int sumaHasta(int n)` usando el retorno de `sumaHasta(n - 1)`.
3. **Paso 3 — Recursión sobre arreglo:** escribe `int contarPares(const int* arr, int n)` avanzando con `arr + 1` y `n - 1` (o usando un índice).
4. **Paso 4 — Primer nodo binario:** define un `struct Nodo` mínimo (`int valor; Nodo* left; Nodo* right;`), arma 3 nodos a mano en `main()` y escribe `int contar(const Nodo* r)` para ver cómo la recursión se bifurca en `left` y `right`. ¡No olvides hacer `delete` al final!
