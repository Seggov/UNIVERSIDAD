#include <iostream>
using namespace std;
template <typename T>


void caminando(int pasos);


void caminando(int pasos){
    if (pasos <= 0){cout << "terminamos de caminar...";}
    else{
        cout << "Caminado, aun faltan " << pasos << " pasos \n";
        pasos--;
        caminando(pasos);

    }
}



int main() {
    cout << "Modulo 03: completa las funciones y los casos.\n" << endl;
    caminando(21);
    return 0;
}
