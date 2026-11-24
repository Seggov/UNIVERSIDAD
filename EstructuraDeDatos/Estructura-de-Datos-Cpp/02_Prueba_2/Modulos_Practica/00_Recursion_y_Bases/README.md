# Módulo 00 — Recursión y Pensamiento en Subárboles

**Objetivo:** dominar la recursión (caso base, paso recursivo y pila de llamadas) antes de entrar a árboles binarios.  
**Práctica orientativa:** 45–60 minutos.

[Resumen Prueba 2](../README.md) · [Práctica y Apuntes](01_Practica_y_Apuntes/apuntes.md) · [Enunciados Escalados](02_Enunciados/README.md) · [Siguiente: Clase 06](../01_Clase_06_TDA_Arbol_y_Binarios/README.md)

---

## Contenidos de la clase

### 1. ¿Qué necesita toda función recursiva?
1. **Caso base:** la entrada mínima donde la función responde directo **sin** volver a llamarse (ej. `n == 0` o `nodo == nullptr`).
2. **Paso recursivo:** reduce el problema acercándose al caso base (`n - 1`, `nodo->left`, `nodo->right`).

```text
llamada: suma(3)
  └── 3 + suma(2)
            └── 2 + suma(1)
                      └── 1 + suma(0)  <-- Caso base: retorna 0
                      └── retorna 1 + 0 = 1
            └── retorna 2 + 1 = 3
  └── retorna 3 + 3 = 6
```

### 2. Pensar en Subárboles
Un árbol binario es recursivo por definición: cada nodo tiene un valor y dos subárboles (`left` y `right`) que tienen exactamente la misma forma que el árbol completo.

```text
          [10]
         /    \
      [5]      [20]      <-- f(10) combina el valor 10 con f(5) y f(20)
     /   \        \
   [2]   [7]     [nullptr]  <-- caso base: si es nullptr, detiene y retorna neutro
```

### 3. Reglas clave para no fallar
- Verifica **`nodo == nullptr`** antes de acceder a `nodo->valor` o `nodo->left`.
- Parámetro **por valor** (`int sumaActual`): cada rama tiene su propia copia independiente.
- Parámetro **por referencia** (`int& total`): todas las llamadas comparten la misma variable.

---

## Cómo continuar en este módulo

1. **Primero ve a [`01_Practica_y_Apuntes/`](01_Practica_y_Apuntes/apuntes.md):** toma apuntes y escribe desde cero cada paso en su `Main.cpp` mínimo.
2. **Luego pasa a [`02_Enunciados/`](02_Enunciados/README.md):** resuelve los ejercicios escalados (Nivel 1 → Nivel 2 → Nivel 3) usando su batería de pruebas.
