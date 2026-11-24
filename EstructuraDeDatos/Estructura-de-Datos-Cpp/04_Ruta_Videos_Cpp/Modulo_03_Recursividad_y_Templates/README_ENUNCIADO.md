# Enunciado 03 — Comparaciones genéricas y suma recursiva

Construye dos herramientas para procesar números. Pueden usar arreglos normales o los del módulo anterior.

## Parte A: función genérica

Completa `template <typename T> T mayor(T a, T b)`. Devuelve el mayor; si son iguales, devuelve a. Usa comparación y retorno, sin std::max.

Prueba mayor(4, 9) -> 9, mayor(7, 7) -> 7 y mayor(2.5, 1.2) -> 2.5. En cada llamada usa dos argumentos del mismo tipo.

## Parte B: recursión

Completa `int sumarRecursivo(const int* datos, int n)`:

- Si datos es nullptr o n <= 0, devuelve 0.
- En otro caso, devuelve la suma de los primeros n elementos mediante una llamada recursiva con un problema más pequeño.
- No uses ciclos en esta función. El llamador garantiza que el arreglo tiene al menos n elementos y usará tamaños pequeños.

Pruebas: [4, 6, 5] con n=3 -> 15; con n=1 -> 4; con n=0 -> 0; nullptr con n=3 -> 0; [-2, 3, -1] con n=3 -> 0.

## Integración y evaluación

En main suma dos arreglos y usa mayor para comparar sus totales. Explica el tipo T de cada llamada, el caso base y la secuencia de llamadas y retornos para [4, 6, 5]. No necesitas que sumarRecursivo sea un template.
