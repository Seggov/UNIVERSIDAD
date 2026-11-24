#include <iostream>
#include <string>
using namespace std;

// Variables Globales
const int MAX_PERSONAS = 20;
string personas[MAX_PERSONAS];                   // Vertices: Para los vertices lista de String
int matrizADY[MAX_PERSONAS][MAX_PERSONAS] = {};  // Matriz 
void recorrerMatriz(int total);
int ingresarValores();

void recorrerMatriz(int total) {
    cout << "\n--- Matriz de Adyacencia (" << total << "x" << total << ") ---\n";
    for (int i = 0; i < total; i++) {
        cout << personas[i] << ":\t";
        for (int j = 0; j < total; j++) {
            cout << matrizADY[i][j] << "\n";
        }
        cout << endl; 
    }
}

int ingresarValores() {
    personas[0] = "Yo";
    int cantidad = 0;

    cout << "Cuantas personas deseas agregar (1 a 19)? ";
    cin >> cantidad;

    for (int j = 1; j <= cantidad; j++) {
        cout << "\nNombre de la persona " << j << ": ";
        cin >> personas[j];
        int peso = 0;
        do {
            cout << "Proximidad con " << personas[j] << " (1 a 100): ";
            cin >> peso;
        } while (peso < 1 || peso > 100);
        matrizADY[0][j] = peso;
    }

    return cantidad + 1; // +1 porque el vertice 0 ("Yo") tambien cuenta
}

int main() {
    cout << "=== Red de Proximidad (Grafos) ===\n";

    int totalVertices = ingresarValores();
    recorrerMatriz(totalVertices);

    return 0;
}