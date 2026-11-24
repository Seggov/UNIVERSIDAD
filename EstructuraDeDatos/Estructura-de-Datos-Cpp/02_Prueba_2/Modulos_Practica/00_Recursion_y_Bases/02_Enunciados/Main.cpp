#include <algorithm>
#include <iostream>
#include <limits>

struct Nodo {
    int valor;
    Nodo* left;
    Nodo* right;

    Nodo(int v) : valor(v), left(nullptr), right(nullptr) {}
};

// --- Nivel 1 ---
int sumarHasta(int n) {
    (void)n;
    return 0;
}

int sumarDigitos(int n) {
    (void)n;
    return 0;
}

// --- Nivel 2 ---
int contarOcurrencias(const int* arr, int n, int objetivo) {
    (void)arr;
    (void)n;
    (void)objetivo;
    return 0;
}

bool estaOrdenado(const int* arr, int n) {
    (void)arr;
    (void)n;
    return false;
}

// --- Nivel 3 ---
int contarNodos(const Nodo* root) {
    (void)root;
    return 0;
}

int sumarNodos(const Nodo* root) {
    (void)root;
    return 0;
}

bool contiene(const Nodo* root, int objetivo) {
    (void)root;
    (void)objetivo;
    return false;
}

int maximoArbol(const Nodo* root) {
    (void)root;
    return std::numeric_limits<int>::min();
}

void liberar(Nodo* root) {
    if (root == nullptr) return;
    liberar(root->left);
    liberar(root->right);
    delete root;
}

int main() {
    std::cout << std::boolalpha;

    std::cout << "=== NIVEL 1 ===\n";
    std::cout << "sumarHasta(5)    = " << sumarHasta(5) << " (esp: 15)\n";
    std::cout << "sumarHasta(0)    = " << sumarHasta(0) << " (esp: 0)\n";
    std::cout << "sumarDigitos(482)= " << sumarDigitos(482) << " (esp: 14)\n";
    std::cout << "sumarDigitos(-482)=" << sumarDigitos(-482) << " (esp: 14)\n";

    std::cout << "\n=== NIVEL 2 ===\n";
    int d1[] = {3, 1, 3, 5, 3};
    int d2[] = {1, 2, 2, 5};
    int d3[] = {1, 4, 2, 5};
    std::cout << "ocurrencias(3)   = " << contarOcurrencias(d1, 5, 3) << " (esp: 3)\n";
    std::cout << "ordenado(d2)     = " << estaOrdenado(d2, 4) << " (esp: true)\n";
    std::cout << "ordenado(d3)     = " << estaOrdenado(d3, 4) << " (esp: false)\n";
    std::cout << "ordenado(null)   = " << estaOrdenado(nullptr, 0) << " (esp: true)\n";

    std::cout << "\n=== NIVEL 3 ===\n";
    Nodo* root = new Nodo(10);
    root->left = new Nodo(5);
    root->right = new Nodo(20);
    root->left->left = new Nodo(2);

    std::cout << "contarNodos      = " << contarNodos(root) << " (esp: 4)\n";
    std::cout << "sumarNodos       = " << sumarNodos(root) << " (esp: 37)\n";
    std::cout << "contiene(20)     = " << contiene(root, 20) << " (esp: true)\n";
    std::cout << "contiene(99)     = " << contiene(root, 99) << " (esp: false)\n";

    Nodo* neg = new Nodo(-10);
    neg->left = new Nodo(-5);
    neg->right = new Nodo(-20);
    std::cout << "maximo(neg)      = " << maximoArbol(neg) << " (esp: -5)\n";

    liberar(root);
    liberar(neg);
    return 0;
}
