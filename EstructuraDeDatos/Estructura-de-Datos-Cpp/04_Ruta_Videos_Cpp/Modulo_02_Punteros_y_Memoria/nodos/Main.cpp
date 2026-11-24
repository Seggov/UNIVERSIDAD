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
    int getValor(){return valor;}
    Nodo *getSiguiente() { return siguiente; }
    void setSiguiente(Nodo *nuevo) { siguiente = nuevo; }
};

void insert(Nodo *head,Nodo *value, int index); // el primer argumento cambiaria dependiendo de lo que queremos insetar
void remove(Nodo *head,int index);
void mostrar(Nodo * head);
int getIndex(Nodo *head,int value);

int main(){

    Nodo *a = new Nodo(13);
    Nodo *b = new Nodo(131);
    Nodo *c = new Nodo(110);
    Nodo *d = new Nodo(14441);


    a -> setSiguiente(b);
    b-> setSiguiente(c);
    c-> setSiguiente(d);


    Nodo *head = a;
    Nodo *istOutlaier = new Nodo(123113313);

    std::cout << "Hola Bienvenido ahora te enseñaremos a remover, insertar y obtener el indice de nodos" << std::endl;
    // insertando
    insert(head,istOutlaier,2);
    mostrar(head);

    // eliminando ando
    remove(head, 3);
    mostrar(head);


    int value = c->getValor();
    int indx = getIndex(head,value);


    return 0;
}

int getIndex(Nodo *head,int value){   
    Nodo *cursor = head;
    int indice = 0;
    while (cursor != nullptr){
        int valorNodo = cursor->getValor();
        if (valorNodo == value){
            return indice;
        }
        indice++;
        cursor = cursor->getSiguiente();
    }
    


    return 0;
}

void insert(Nodo *head,Nodo *value, int index){
    int c = -1;
    Nodo *cursor = head; // empezamos supuestamente desde el indice [0]
    while (cursor != nullptr){
        if (c==index){
            cursor->setSiguiente(value);
        }
        c++;
        cursor = cursor->getSiguiente();
    }
}

void remove(Nodo *head,int index){

    Nodo *cursor = head;
    int c = 0;
    while (cursor!=nullptr){
        if (c==index){
            Nodo *actual = cursor;
            
        }
        cursor = cursor->getSiguiente();
    }
    
}



// para ver el reusltaod noma
void mostrar(Nodo * head){
    Nodo *cursor = head;int c = 0;
    std::cout << "=============================================================" << std::endl;
    while (cursor != nullptr)
    {
        c++;
        int valorActual = cursor->getValor();
        std::cout << "Valor del nodo numero ["<<c<<"] " << valorActual << std::endl;
        cursor = cursor->getSiguiente();

    }   
    std::cout << "=============================================================" << std::endl;

}