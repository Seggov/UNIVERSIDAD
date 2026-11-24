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

    std::cout << "Bienvenidos al Sistema de Pilas y Colas "
              << "¿Que te gustaria ver primero? \n"
              << std::endl;

    int selector = -1;
    while (selector != 0){
        menu();
        std::cin >> selector;
        if (selector == 1){
            // pila()
        }
        else if (selector == 2){
            // COLA()
        }
        else if (selector == 0)
        {
            std::cout << "Saliendo, CHAO MEN -[.]_[.]- ... " << std::endl;
        }
        else
        {
            std::cout << "Saliendo por defecto ... " << std::endl;
        }
    }

    return 0;
}

void pilas(){
    
}




void menu()
{
    std::cout << "[1] - PILAS" << std::endl;
    std::cout << "[2] - COLAS \n"
              << std::endl;
}