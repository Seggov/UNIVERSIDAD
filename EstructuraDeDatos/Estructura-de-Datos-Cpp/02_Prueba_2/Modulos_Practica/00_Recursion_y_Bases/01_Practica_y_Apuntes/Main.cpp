#include <iostream>
using namespace std;

// Espacio de practica paso a paso (plantilla leve).
// Sigue los pasos de apuntes.md uno a uno y compila despues de cada paso.

// Paso 1: void trazar(int n)

// Paso 2: int sumaHasta(int n)

// Paso 3: int contarPares(const int* arr, int n)

// Paso 4: struct Nodo y int contar(const Nodo* r)


struct Nodo{
    int valor;
    Nodo* left;
    Nodo* right;

    
};


int contarPares(const int* arr, int n);
void mostrarArbol(const Nodo* r, int nivel = 0);

int contarPares(const int* arr, int n) {
    if (arr == nullptr || n <= 0) {   // caso que no queden elementos
        return 0;
    }

    if (arr[0] % 2 == 0) {
        return 1 + contarPares(arr + 1, n - 1); // Suma 1 + pares del resto
    } else {
        return contarPares(arr + 1, n - 1);     // Suma 0 + pares del resto
    }
}

void mostrarArbol(const Nodo* r, int nivel = 0)
{
    if (r == nullptr) return; // si esta vacio simplemente retorna
    mostrarArbol(r->right, nivel + 1); // Derecha
    
    for (int i = 0; i < nivel; i++) cout << "  "; // Nodo actual cursor
    cout << r->valor << "\n";

    mostrarArbol(r->left, nivel +1);  // izquierda
}


int main() {
    cout << "Modulo 00 - Practica paso a paso\n";

    int datos[] = {7,2,4,9,4,6,8,10,100,313,34};
    int cantidad = contarPares(datos,10); // Congelamos el valor int 

    cout << "Cantidad de Pares son : " << cantidad << endl;
    
    Nodo* raiz = new Nodo{10, nullptr, nullptr};
    Nodo* hijo = new Nodo{5, nullptr, nullptr}; 
    raiz->left = hijo;                      

    cout << "Valor de raiz->left: " << raiz->left->valor << endl; // Imprime 5

    vector<int> valores = {10,5,20,2,15,30};
    Nodo* raiz = nullptr;
    for (int x : valores)
    {
        raiz = insertar(raiz, x);
    }
        mostrarArbol(raiz);

    

    delete hijo; // limpiamos memoria
    delete raiz;

    return 0;
}
