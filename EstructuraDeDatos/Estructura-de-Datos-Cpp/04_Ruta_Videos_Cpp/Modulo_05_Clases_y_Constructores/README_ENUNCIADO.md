# Enunciado 05 — Cuenta con estado propio

Implementa la clase Cuenta con un saldo entero público y los siguientes constructores y métodos. Usa cantidades pequeñas y no reserves memoria dinámica.

## Requisitos

- `Cuenta()`: saldo inicial 0.
- `Cuenta(int saldoInicial)`: usa el valor recibido si es no negativo; si es negativo, comienza en 0.
- `depositar(monto)`: acepta solo montos positivos, suma al saldo y devuelve true; de lo contrario deja el estado igual y devuelve false.
- `retirar(monto)`: acepta solo montos positivos que no superen el saldo. Actualiza el saldo y devuelve true; si falla, deja todo igual y devuelve false.
- `mostrar()`: imprime el saldo del objeto.
- Función externa `transferir(Cuenta& origen, Cuenta& destino, int monto)`: rechaza transferencias al mismo objeto y montos inválidos o sin fondos; si es válida, utiliza retirar y depositar para efectuarla. Devuelve si tuvo éxito.

## Casos obligatorios

- Cuenta a; comienza con 0. Cuenta b(100); comienza con 100. Cuenta c(-20); comienza con 0.
- Deposita 40 en a: a=40, b=100.
- Transfiere 30 de b a a: b=70, a=70.
- Rechaza retirar 80 de b, depositar 0 en a y transferir -5 de a a b; conserva los saldos.
- Rechaza transferir de a hacia a; conserva 70.
- Retira 70 de a: queda en 0.

## Para la evaluación

Explica qué constructor se ejecuta en cada declaración, por qué los objetos conservan saldos independientes y sobre qué objeto actúa cada llamada a un método. Conserva esta versión: el módulo 06 trabaja sobre una copia en su propia carpeta.
