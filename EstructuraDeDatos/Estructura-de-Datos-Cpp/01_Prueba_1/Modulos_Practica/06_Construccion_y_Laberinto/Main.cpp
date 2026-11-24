#include <iostream>

class Nodo
{
private:
    int cordenadaX;
    int cordenadaY;
    Nodo *siguiente;

public:
    Nodo(int x, int y)
    {
        this->cordenadaX = x;
        this->cordenadaY = y;
        this->siguiente = nullptr;
    }
    int getCordenadaX() { return cordenadaX; }
    int getCordenadaY() { return cordenadaY; }
    Nodo *getSiguiente() { return siguiente; }
    void setSiguiente(Nodo *nuevo) { siguiente = nuevo; }
};

void menu();

int main()
{
    const int FILAS = 7;
    const int COLUMNAS = 10;

    const char laberinto[FILAS][COLUMNAS] = {
        {'S', '.', '#', '.', '.', '.', '.', '.', '.', '.'},
        {'.', '#', '#', '.', '#', '#', '.', '#', '#', '.'},
        {'.', '.', '.', '.', '#', '.', '.', '.', '.', '.'},
        {'.', '#', '#', '#', '#', '.', '#', '#', '#', '.'},
        {'.', '.', '.', '.', '.', '.', '.', '.', '.', '.'},
        {'.', '#', '#', '#', '#', '#', '#', '#', '#', '.'},
        {'.', '.', '.', '.', '.', '.', '.', '.', '.', 'F'}
    };

    Nodo* nodos[FILAS][COLUMNAS] = {};

    for (int fila = 0; fila < FILAS; fila++){
        for (int columna = 0; columna < COLUMNAS; columna++){
            if (laberinto[fila][columna] != '#'){
                nodos[fila][columna] = new Nodo(columna, fila);
            }

            // Si es pared, nodos[fila][columna] sigue siendo nullptr.
        }
    }
    Nodo* nodoCursor = nodos[0][0]; // Nodo inicial

    while (nodoCursor != nullptr && (nodoCursor->getCordenadaY() != 9 || nodoCursor->getCordenadaX() != 9))
    {
        std::cout << "Nodo en (" << nodoCursor->getCordenadaX() << ", " << nodoCursor->getCordenadaY() << ")\n";
        nodoCursor = nodoCursor->getSiguiente();
    }

    // Liberar memoria asignada
    for (int fila = 0; fila < FILAS; fila++){
        for (int columna = 0; columna < COLUMNAS; columna++){
            delete nodos[fila][columna];
        }
    }

    return 0;
}
