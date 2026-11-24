#include <iostream>

using namespace std;

void visualizarNotas(int* pNotas, int tam);
int* crearNotas(int tam);
bool cambiarNota(int* notas, int tam, int indice, int nuevaNota);
double promedioNotas(int* notas, int tam);

void visualizarNotas(int* pNotas, int tam) {
    cout << "Tus notas son" << endl;
    for (int i = 0; i < tam; i++) {
        cout << pNotas[i] << " ";
    }
}

int* crearNotas(int tam) {
    if (tam <= 0) {
        return nullptr;
    }
    return new int[tam]{};
}

bool cambiarNota(int* notas, int tam, int indice, int nuevaNota) {
    if (notas == nullptr || tam <= 0 || indice < 0 || indice >= tam ||
        nuevaNota < 1 || nuevaNota > 7) {
        return false;
    }

    notas[indice] = nuevaNota;
    return true;
}

double promedioNotas(int* notas, int tam) {
    if (notas == nullptr || tam <= 0) {
        return 0.0;
    }

    int acumulado = 0;
    for (int i = 0; i < tam; i++) {
        acumulado += notas[i];
    }

    return static_cast<double>(acumulado) / tam;
}

int main() {
    cout << "Bienvenido al calculador de Notas" << endl;
    cout << "Cuantas notas va a ingresar: " << endl;

    int tam;
    cin >> tam;
    cout << "Genial, entonces van a ser " << tam << endl;

    int* pNotas = crearNotas(tam); // reserva temp espacios para la nota, ojo una sola direccion

    if (pNotas == nullptr) {
        cout << "Cantidad no valida" << endl;
        return 1;
    }

    for (int i = 0; i < tam; i++) {
        cout << "Ingrese la nota Numero [" << i + 1 << "] ";
        cin >> pNotas[i];
    }

    visualizarNotas(pNotas, tam);
    cout << endl;

    cout << "Tus notas promedio son: "
         << promedioNotas(pNotas, tam) << endl;

    int indice;
    int nuevaNota;
    cout << "Que nota quieres cambiar? (indice desde 0): ";
    cin >> indice;
    cout << "Ingresa la nueva nota: ";
    cin >> nuevaNota;

    if (cambiarNota(pNotas, tam, indice, nuevaNota)) {
        cout << "Nota cambiada correctamente." << endl;
        visualizarNotas(pNotas, tam);
        cout << endl;
        cout << "Nuevo promedio: "
             << promedioNotas(pNotas, tam) << endl;
    } else {
        cout << "No se pudo cambiar la nota." << endl;
    }

    delete[] pNotas;

    return 0;
}