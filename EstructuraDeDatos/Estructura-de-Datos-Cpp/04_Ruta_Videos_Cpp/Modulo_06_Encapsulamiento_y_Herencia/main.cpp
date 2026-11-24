#include <iostream>

class Cuenta {
private:
    int saldo;

public:
    Cuenta() : saldo(0) {}
    Cuenta(int saldoInicial) : saldo(0) {
        // TODO: adaptar tu constructor del modulo 05.
        (void)saldoInicial;
    }

    int getSaldo() const {
        return saldo;
    }

    bool depositar(int monto) {
        // TODO: recuperar tu implementacion del modulo 05.
        (void)monto;
        return false;
    }

    bool retirar(int monto) {
        // TODO: recuperar tu implementacion del modulo 05.
        (void)monto;
        return false;
    }
};

class CuentaBonificada : public Cuenta {
private:
    int bono;
    bool bonoAplicado;

public:
    CuentaBonificada(int saldoInicial, int bonoInicial)
        : Cuenta(saldoInicial), bono(0), bonoAplicado(false) {
        // TODO: validar e inicializar el bono.
        (void)bonoInicial;
    }

    int getBono() const { return bono; }

    bool setBono(int nuevoBono) {
        // TODO: validar el valor y si el bono ya se aplico.
        (void)nuevoBono;
        return false;
    }

    bool aplicarBono() {
        // TODO: usar depositar y actualizar bonoAplicado.
        (void)bonoAplicado;
        return false;
    }
};

bool transferir(Cuenta& origen, Cuenta& destino, int monto) {
    // TODO: adaptar tu transferencia del modulo 05.
    (void)origen; (void)destino; (void)monto;
    return false;
}

int main() {
    CuentaBonificada especial(100, 20);
    std::cout << std::boolalpha;
    // TODO: comprobar todos los casos con la interfaz publica.
    std::cout << "Saldo provisional: " << especial.getSaldo() << '\n';
    return 0;
}
