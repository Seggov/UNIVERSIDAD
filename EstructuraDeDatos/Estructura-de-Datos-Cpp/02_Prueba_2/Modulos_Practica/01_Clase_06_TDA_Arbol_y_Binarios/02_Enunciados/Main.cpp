#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

template <typename T>
class BTNode {
private:
    T value;
    BTNode<T>* left;
    BTNode<T>* right;

public:
    BTNode(T val) : value(val), left(nullptr), right(nullptr) {}
    T getValue() const { return value; }
    BTNode<T>* getLeft() const { return left; }
    BTNode<T>* getRight() const { return right; }
    void setLeft(BTNode<T>* l) { left = l; }
    void setRight(BTNode<T>* r) { right = r; }
};

// --- Nivel 1 ---
void preorden(const BTNode<int>* root) {
    (void)root;
}

void inorden(const BTNode<int>* root) {
    (void)root;
}

void postorden(const BTNode<int>* root) {
    (void)root;
}

void porNivel(const BTNode<int>* root) {
    (void)root;
}

// --- Nivel 2 ---
int contarHojas(const BTNode<int>* root) {
    (void)root;
    return 0;
}

int contarEnNivel(const BTNode<int>* root, int nivelObjetivo) {
    (void)root;
    (void)nivelObjetivo;
    return 0;
}

void inordenArreglo(const std::vector<int>& tree, int idx) {
    (void)tree;
    (void)idx;
}

// --- Nivel 3 ---
bool esLleno(const BTNode<int>* root) {
    (void)root;
    return false;
}

bool sonIsomorfos(const BTNode<int>* a, const BTNode<int>* b) {
    (void)a;
    (void)b;
    return false;
}

void liberar(BTNode<int>* root) {
    if (root == nullptr) return;
    liberar(root->getLeft());
    liberar(root->getRight());
    delete root;
}

int main() {
    std::cout << std::boolalpha;

    /* Arbol de prueba:
            40
           /  \
          8    80
           \  /  \
           12 67 102
    */
    BTNode<int>* root = new BTNode<int>(40);
    root->setLeft(new BTNode<int>(8));
    root->setRight(new BTNode<int>(80));
    root->getLeft()->setRight(new BTNode<int>(12));
    root->getRight()->setLeft(new BTNode<int>(67));
    root->getRight()->setRight(new BTNode<int>(102));

    std::cout << "=== NIVEL 1 ===\n";
    std::cout << "Preorden  : "; preorden(root);  std::cout << " (esp: 40 8 12 80 67 102)\n";
    std::cout << "Inorden   : "; inorden(root);   std::cout << " (esp: 8 12 40 67 80 102)\n";
    std::cout << "Postorden : "; postorden(root); std::cout << " (esp: 12 8 67 102 80 40)\n";
    std::cout << "Por nivel : "; porNivel(root);  std::cout << " (esp: 40 8 80 12 67 102)\n";

    std::cout << "\n=== NIVEL 2 ===\n";
    std::cout << "Hojas          : " << contarHojas(root) << " (esp: 3)\n";
    std::cout << "Nodos nivel 3  : " << contarEnNivel(root, 3) << " (esp: 3)\n";
    std::vector<int> arr = {-1, 20, 12, 61, 33, 48, 81};
    std::cout << "Inorden arreglo: "; inordenArreglo(arr, 1); std::cout << " (esp: 33 12 48 20 81 61)\n";

    std::cout << "\n=== NIVEL 3 ===\n";
    BTNode<int>* lleno1 = new BTNode<int>(1);
    lleno1->setLeft(new BTNode<int>(2));
    lleno1->setRight(new BTNode<int>(3));

    BTNode<int>* lleno2 = new BTNode<int>(99);
    lleno2->setLeft(new BTNode<int>(50));
    lleno2->setRight(new BTNode<int>(70));

    std::cout << "esLleno(root)           : " << esLleno(root) << " (esp: false)\n";
    std::cout << "esLleno(lleno1)         : " << esLleno(lleno1) << " (esp: true)\n";
    std::cout << "sonIsomorfos(ll1, ll2)  : " << sonIsomorfos(lleno1, lleno2) << " (esp: true)\n";
    std::cout << "sonIsomorfos(ll1, root) : " << sonIsomorfos(lleno1, root) << " (esp: false)\n";

    liberar(root);
    liberar(lleno1);
    liberar(lleno2);
    return 0;
}
