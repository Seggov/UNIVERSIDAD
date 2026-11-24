#include <iostream>

class Cuenta {
public:
    int saldo;

    Cuenta() : saldo(0) {
        // TODO: comprobar que cumple el enunciado.
    }

    Cuenta(int saldoInicial) : saldo(0) {
        // TODO: validar e inicializar con el parametro.
        (void)saldoInicial;
    }

    bool depositar(int monto) {
        // TODO: validar y actualizar el saldo.
        (void)monto;
        return false;
    }

    bool retirar(int monto) {
        // TODO: validar y actualizar el saldo.
        (void)monto;
        return false;
    }

    void mostrar() {
        // TODO: mostrar el saldo de este objeto.
    }
};

bool transferir(Cuenta& origen, Cuenta& destino, int monto) {
    // TODO: validar y utilizar los metodos.
    (void)origen; (void)destino; (void)monto;
    return false;
}

int main() {
    Cuenta a;
    Cuenta b(100);
    std::cout << std::boolalpha;
    // TODO: completar los casos del enunciado.
    a.mostrar();
    b.mostrar();
    return 0;
}
