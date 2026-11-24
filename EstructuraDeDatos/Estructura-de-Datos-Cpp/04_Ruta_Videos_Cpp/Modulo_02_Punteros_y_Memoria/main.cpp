#include <iostream>

using namespace std; 
int main() {

    int *pNum = NULL; // la "vaciamos"
    pNum = new int; // "Almacenaremos mas adelante un int en el programa"
    *pNum = 25;

    cout << "Direccion: " << pNum << "\n"; // ESTA RESERVADO
    cout << "Valor Direccion: " << *pNum << "\n";

    delete pNum; // aqui es importante eliminar ese new, para que no exista fuga de memori

    cout << "Cuantas notas va ha ingresar" << endl;
    int tam;
    cin >> tam;

    int* pNotas = n0ew int[tam]; // reserva para notas
    for (int i = 0; i < tam; i++){
        cout << "Ingrese la nota " << i+1 << " ";
        cin >> pNotas[i];
    }

    cout << "Tus notas son" << endl;
    for (int i = 0; i < tam; i++)
    {
        cout << pNotas[i] << " ";
    }

    cout << endl;
    delete [] pNotas;
    
    return 0;
}

