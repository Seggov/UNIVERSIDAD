#include <iostream>

class Nodo
{
private:
    int valor;
    Nodo *siguiente;

public:
    Nodo(int valor)
    {
        this->valor = valor;
        this->siguiente = nullptr;
    }
    int getValor() { return valor; }
    Nodo *getSiguiente() { return siguiente; }
    void setSiguiente(Nodo *nuevo) { siguiente = nuevo; }
};

void menu();

int main()
{

    Nodo *a = new Nodo(10);
    Nodo *b = new Nodo(20);
    Nodo *c = new Nodo(30);
    Nodo *d = new Nodo(40);

    a->setSiguiente(b);
    b->setSiguiente(c);
    c->setSiguiente(d);

    Nodo *head = a;

    Nodo *anterior = nullptr;
    Nodo *actual = head;
    Nodo *siguiente = nullptr;

    while (actual != nullptr){
        // 1. Guardar el siguiente nodo
        siguiente = actual->getSiguiente();

        // 2. Dar vuelta el enlace
        actual->setSiguiente(anterior);

        // 3. Mover anterior
        anterior = actual;

        // 4. Mover actual
        actual = siguiente;
    }

    return 0;
}