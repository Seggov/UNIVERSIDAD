#include <iostream>
using namespace std;


enum Estado { PENDIENTE, COMPLETADA };

struct Tarea {
    int id;
    Estado estado;
};

struct Nodo {
    Tarea tarea; // Nodo en si tiene dentro una Tarea
    Nodo* siguiente;
};

bool agregarInicio(Nodo*& head, const Tarea& tarea) { // Ese Nodo*& significa que el head es si o si un puntero con referencia
    if (tarea.id <= 0){return false;} // Solo porque el enunciado lo menciona que tiene que ser entero positivo
    Nodo* actual = head; 
    while (actual != nullptr){
        if (actual->tarea.id == tarea.id){return false;} // Porque es el head, si es el head de por si esta en el inicio
    
        actual = actual->siguiente; // Avanzando al siguiente nodo
    }
    Nodo* nuevo = new Nodo;
    nuevo->tarea = tarea;
    nuevo->siguiente = head;    
}

bool completar(Nodo* head, int id) {
    // TODO: buscar y actualizar el estado.
    (void)head; (void)id;
    return false;
}

int contarPendientes(const Nodo* head) {
    // TODO: contar sin modificar.
    (void)head;
    return 0;
}

void mostrar(const Nodo* head) {
    // TODO: recorrer e imprimir id y estado.
    (void)head;
}

void liberarLista(Nodo*& head) {
    // TODO: liberar todos los nodos y dejar head en nullptr.
    (void)head;
}

int main() {
    Nodo* head = nullptr;

    cout << agregarInicio(head,{10,PENDIENTE});

    return 0;
}
