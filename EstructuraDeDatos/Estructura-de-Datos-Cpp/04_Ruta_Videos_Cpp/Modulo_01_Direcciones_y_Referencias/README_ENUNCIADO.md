# Enunciado 01 — Transferencia de saldo

Dos personas tienen saldos enteros. Implementa una transferencia mediante funciones, sin clases ni variables globales.

## Funciones que debes completar

1. `int 
(int saldo, int monto)`: devuelve saldo menos monto, sin cambiar el saldo original. Se usa solo con montos válidos.
2. `bool transferir(int& origen, int& destino, int monto)`: modifica ambos saldos si monto es positivo, alcanza el saldo y origen y destino son variables distintas. En otro caso devuelve false y deja todo igual.
3. `void mostrarSaldos(const int& origen, const int& destino)`: muestra los saldos sin modificarlos.

Usa cantidades pequeñas; no se exige tratar desbordamientos de enteros.

## Casos obligatorios

Prueba cada caso desde sus saldos iniciales:

| Origen | Destino | Monto | Resultado | Saldos finales |
| --- | --- | --- | --- | --- |
| 100 | 40 | 30 | true | 70 y 70 |
| 100 | 40 | 150 | false | 100 y 40 |
| 100 | 40 | 0 | false | 100 y 40 |
| 100 | 40 | -5 | false | 100 y 40 |
| 100 | 40 | 100 | true | 0 y 140 |

También llama `transferir(saldo, saldo, 10)` con saldo 100: debe devolver false y conservar 100. Compara las direcciones de los parámetros para detectar este caso.

Comprueba que `saldoSimulado(100, 30)` devuelve 70 y que la variable pasada sigue valiendo 100. En main imprime el valor y la dirección de cada saldo.

## Para la evaluación

Además de los criterios generales, explica por qué la simulación no cambia el original, por qué transferir sí puede hacerlo y qué protege const. Entrega main.cpp completo y tus respuestas en el chat o en un archivo RESPUESTAS.md.
