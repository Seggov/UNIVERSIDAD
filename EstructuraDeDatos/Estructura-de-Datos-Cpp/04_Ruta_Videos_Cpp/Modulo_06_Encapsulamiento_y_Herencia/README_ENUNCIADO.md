# Enunciado 06 — Cuentas con encapsulamiento y herencia

Evoluciona la cuenta del módulo 05. Conserva todas sus validaciones y reemplaza los accesos directos al saldo por operaciones públicas.

## Parte A: encapsulamiento

- Haz saldo privado.
- Implementa `getSaldo() const`: consulta sin modificar.
- Conserva depositar, retirar y los dos constructores del módulo 05. No agregues un setter de saldo: sus cambios pasan por depositar y retirar.
- Conserva la transferencia y adáptala para usar la interfaz pública.

## Parte B: herencia

Implementa CuentaBonificada, que hereda públicamente de Cuenta:

- Tiene un bono entero privado y un bool privado que indica si ya fue aplicado.
- Su constructor recibe saldoInicial y bonoInicial. La clase base valida el saldo; un bono negativo se transforma en 0. Al comenzar, el bono no está aplicado.
- `getBono() const`: consulta el bono.
- `setBono(nuevoBono)`: acepta valores no negativos solo antes de aplicar el bono. Devuelve true si acepta; si rechaza, devuelve false y conserva el estado.
- `aplicarBono()`: si el bono es positivo y todavía no se aplicó, lo deposita usando el método heredado y marca que se aplicó. Devuelve true. En otro caso devuelve false sin cambios. Si el bono es cero, no lo marca como aplicado.
- No redeclares saldo en la clase derivada ni copies depositar o retirar. No accedas directamente al saldo privado de la base.

## Casos obligatorios

- CuentaBonificada especial(100, 20): saldo 100, bono 20.
- setBono(-5): false, bono sigue en 20. setBono(30): true.
- aplicarBono(): true, saldo 130. Repetir: false, saldo 130.
- setBono(50) después de aplicarlo: false y bono 30.
- CuentaBonificada sinBono(-10, -5): saldo 0, bono 0; aplicarBono devuelve false. Luego setBono(5) y aplicarBono: saldo 5.
- Transfiere 30 de especial a una Cuenta normal con saldo 0: quedan 100 y 30. Esto utiliza la clase derivada como referencia a su base; no necesita métodos virtuales.
- Repite los casos de saldo inválido del módulo 05.

## Para la evaluación

Explica qué protege private, qué hereda CuentaBonificada y por qué su bono se aplica una sola vez. Justifica por qué hay un setter de bono pero no uno de saldo. Con este módulo termina la ruta de videos; la integración de estructuras de datos sigue en las guías anteriores.
