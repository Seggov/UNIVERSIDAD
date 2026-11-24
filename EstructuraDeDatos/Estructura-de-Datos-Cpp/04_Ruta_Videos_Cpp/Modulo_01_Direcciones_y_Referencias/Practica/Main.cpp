#include <iostream>
using namespace std;

int saldoSimulado(double saldo, double monto);
bool transferir(int &origen, int &destino, int monto);

int saldoSimulado(double saldo, double monto){
    return saldo - monto;}

bool transferir(int &origen, int &destino, int monto){
    if (monto > 0){
    if (origen > monto){
        destino += monto;
        origen -= monto;
        return true;
    }
    else if (origen < monto){
        cout << "No tiene saldo suficiente" << endl;
        return false;
    }
    else{return false;}
    }else{return false;}
}

int main() {
    cout << "Simulacion de Transferencias\n" << endl;
    
    int origen = 122; int destino = 1203;
    int saldoActual = saldoSimulado(100, 30);
    bool aux = transferir(origen, destino, 30);    


    return 0;
} 

