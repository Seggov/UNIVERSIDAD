#include <iostream>

// NODOS
class Nodo{

private:
    int valor;
    Nodo *siguiente; // variable PUNTERO - Guarda la Direccion del siguiente NODO
public:
    Nodo(int valor){ // Constructor
        this->valor = valor;
        this->siguiente = nullptr; // fin nodos, siguiente valor nulo
    }
    int getValor(){return valor;} // gettter

    Nodo *getSiguiente(){ // ojon aqui queremos obtener cual es el siguiente, por eso es PUNTERO 
        return siguiente;
    }
    void setSiguiente(Nodo *nuevo){ // aqui cambiamos el siguiente
        siguiente = nuevo; 
    }
};

void mostrar(Nodo *head);
int contar(Nodo *head);
int buscarMayor(Nodo *head);
void menu();

int main()
{
    // Ejemplo de nodo basico, guardando un int poque la clase nodo tiene un  atributo de valor
    Nodo *a = new Nodo(5);
    Nodo *b = new Nodo(8);
    Nodo *c = new Nodo(3);
    Nodo *d = new Nodo(12);

    // Aqui vamos a decir como es la "lista"
    a->setSiguiente(b);
    b->setSiguiente(c);
    c->setSiguiente(d);
    Nodo *head = a; // le decimos quer el primero sera a
    int selector=-1;
    while (selector != 0){
        menu();
        std::cin >> selector;
        if (selector == 1){mostrar(head);}
        else if (selector == 2){contar(head);}
        else if (selector==3){buscarMayor(head);}
        else if (selector == 0) {std::cout << "SaLiendo ..." << std::endl; selector = 0;}
        else {std::cout << "SaLiendo por defecto" << std::endl; selector = 0;}
    }
    return 0;
}    
    
void mostrar(Nodo * head){
    Nodo *cursor = head;int c = 0;
    while (cursor != nullptr)
    {
        c++;
        int valorActual = cursor->getValor();
        std::cout << "Valor del nodo numero ["<<c<<"] " << valorActual << std::endl;
        cursor = cursor->getSiguiente();
    }   
    
}

int contar(Nodo * head)
{
    
    Nodo *cursor = head;
    int acumulador = 0;;int actualNumberNodo = cursor->getValor();
    while (cursor != nullptr){
        acumulador += actualNumberNodo;
        cursor = cursor->getSiguiente();

    }
    std::cout << "El total de los nodos es -> " << acumulador << std::endl;
    return acumulador;
}
int buscarMayor(Nodo * head)
{   
    Nodo *cursor = head;
    int mayorActual = 0;int actualNumberNodo = cursor->getValor();
    while (cursor != nullptr){
    actualNumberNodo = cursor->getValor();
    if (actualNumberNodo > mayorActual){
        mayorActual = actualNumberNodo;
    }
    cursor = cursor->getSiguiente();
}
    std::cout << "El Mayor actual es el " << mayorActual << std::endl;
    return mayorActual;
    


}
void menu()
{
    std::cout << "Hola que quieres hacer \n"
                << std::endl;
    std::cout << "[1] Mostrar" << std::endl;
    std::cout << "[2] Contar" << std::endl;
    std::cout << "[3] Buscar Mayor" << std::endl;
    std::cout << "[0] Saliendo salir \n"
                << std::endl;
}
