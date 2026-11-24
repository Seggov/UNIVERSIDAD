#include <iostream>
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

Nodo *insertarInicio(Nodo *head, Nodo *nodo);
Nodo *insertarAlFinal(Nodo *head, Nodo *nodo);
void mostrar(Nodo * head);

int main(){
    Nodo *a = new Nodo(5);
    Nodo *b = new Nodo(8);
    Nodo *c = new Nodo(3);
    Nodo *d = new Nodo(12);
    // Aqui vamos a decir como es la "lista"
    a->setSiguiente(b);
    b->setSiguiente(c);
    c->setSiguiente(d);

    Nodo *head = a; // el indice [0]

    Nodo *final = new Nodo(20);  // el que queremos insertar al final
    Nodo *nuevo = new Nodo(2); // el que queremos agregar aparte del header.
    head = insertarInicio(head, nuevo);
    head = insertarAlFinal(head, final);

    // Imprimimos para visualizar los nodos

    mostrar(head);
    return 0;
}
// =====================================================================
/*
Metodos que retornan en un ATRIBUTO de CLASE
*/
Nodo *insertarInicio(Nodo *head, Nodo *nodo){
    nodo->setSiguiente(head);
    return nodo; // y aqui finalemtne retornamos el primero
}
Nodo *insertarAlFinal(Nodo *head, Nodo *final){
    Nodo *cursor = head;
    while (cursor != nullptr){
        if (cursor->getSiguiente() == nullptr){
            cursor->setSiguiente(final); // decimos entonces que el proximo es el final
            break;
        }
        cursor = cursor->getSiguiente();
    }
    return head;
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