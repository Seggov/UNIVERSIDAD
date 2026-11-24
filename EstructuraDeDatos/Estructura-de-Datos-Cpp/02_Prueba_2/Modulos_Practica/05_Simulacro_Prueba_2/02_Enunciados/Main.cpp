#include <iostream>
#include <queue>

struct TNode {
    int value;
    TNode* left;
    TNode* right;

    TNode(int v) : value(v), left(nullptr), right(nullptr) {}
};

// --- Nivel 1 ---
int contarConUnSoloHijo(const TNode* root) {
    (void)root;
    return 0;
}

// --- Nivel 2 ---
int sumarEnRangoABB(const TNode* root, int low, int high) {
    (void)root;
    (void)low;
    (void)high;
    return 0;
}

// --- Nivel 3 ---
bool esArbolCompleto(const TNode* root) {
    (void)root;
    return false;
}

void liberar(TNode* root) {
    if (root == nullptr) return;
    liberar(root->left);
    liberar(root->right);
    delete root;
}

int main() {
    std::cout << std::boolalpha;

    /* ABB de prueba:
              35
            /    \
          15      50
         /  \
       10    25
            /
          20
    */
    TNode* abb = new TNode(35);
    abb->left = new TNode(15);
    abb->right = new TNode(50);
    abb->left->left = new TNode(10);
    abb->left->right = new TNode(25);
    abb->left->right->left = new TNode(20);

    std::cout << "=== NIVEL 1 ===\n";
    std::cout << "contarConUnSoloHijo(abb)  = " << contarConUnSoloHijo(abb) << " (esp: 1)\n";

    std::cout << "\n=== NIVEL 2 ===\n";
    std::cout << "sumarEnRango(15, 35)      = " << sumarEnRangoABB(abb, 15, 35) << " (esp: 95)\n";
    std::cout << "sumarEnRango(100, 200)    = " << sumarEnRangoABB(abb, 100, 200) << " (esp: 0)\n";

    std::cout << "\n=== NIVEL 3 ===\n";
    TNode* comp = new TNode(1);
    comp->left = new TNode(2);
    comp->right = new TNode(3);
    comp->left->left = new TNode(4);
    comp->left->right = new TNode(5);

    TNode* noComp = new TNode(1);
    noComp->left = new TNode(2);
    noComp->right = new TNode(3);
    noComp->right->right = new TNode(6);

    std::cout << "esArbolCompleto(abb)      = " << esArbolCompleto(abb) << " (esp: false)\n";
    std::cout << "esArbolCompleto(comp)     = " << esArbolCompleto(comp) << " (esp: true)\n";
    std::cout << "esArbolCompleto(noComp)   = " << esArbolCompleto(noComp) << " (esp: false)\n";
    std::cout << "esArbolCompleto(nullptr)  = " << esArbolCompleto(nullptr) << " (esp: true)\n";

    liberar(abb);
    liberar(comp);
    liberar(noComp);
    return 0;
}
