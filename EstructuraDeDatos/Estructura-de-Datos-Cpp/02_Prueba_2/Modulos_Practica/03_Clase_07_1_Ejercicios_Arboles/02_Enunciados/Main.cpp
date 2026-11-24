#include <algorithm>
#include <iostream>
#include <limits>
#include <vector>

struct TNode {
    char label;
    int value;
    TNode* left;
    TNode* right;

    TNode(char lbl, int val) : label(lbl), value(val), left(nullptr), right(nullptr) {}
};

// --- Nivel 1 ---
float average(TNode* root) {
    (void)root;
    return 0.0f;
}

int getMaxHeight(TNode* root) {
    (void)root;
    return 0;
}

// --- Nivel 2 ---
void calcMaxSum(TNode* root, int& maxValue, std::vector<char>& maxPath) {
    (void)root;
    maxValue = 0;
    maxPath.clear();
}

// --- Nivel 3 ---
bool existeSumaCamino(TNode* root, int objetivo) {
    (void)root;
    (void)objetivo;
    return false;
}

int sumaHojasIzquierdas(TNode* root) {
    (void)root;
    return 0;
}

void liberar(TNode* root) {
    if (root == nullptr) return;
    liberar(root->left);
    liberar(root->right);
    delete root;
}

int main() {
    std::cout << std::boolalpha;

    /* Arbol ejemplo:
              5(A)
            /      \
          4(B)     8(C)
          /        /  \
        11(D)   13(E) 4(F)
        /   \            \
      7(G)  2(H)         1(I)
    */
    TNode* root = new TNode('A', 5);
    root->left = new TNode('B', 4);
    root->right = new TNode('C', 8);
    root->left->left = new TNode('D', 11);
    root->left->left->left = new TNode('G', 7);
    root->left->left->right = new TNode('H', 2);
    root->right->left = new TNode('E', 13);
    root->right->right = new TNode('F', 4);
    root->right->right->right = new TNode('I', 1);

    std::cout << "=== NIVEL 1 ===\n";
    std::cout << "average(nullptr)     = " << average(nullptr) << " (esp: 0)\n";
    std::cout << "average(root)        = " << average(root) << " (esp: 6.11111)\n";
    std::cout << "getMaxHeight(null)   = " << getMaxHeight(nullptr) << " (esp: 0)\n";
    std::cout << "getMaxHeight(root)   = " << getMaxHeight(root) << " (esp: 4)\n";

    std::cout << "\n=== NIVEL 2 ===\n";
    int maxSum = 0;
    std::vector<char> maxPath;
    calcMaxSum(root, maxSum, maxPath);
    std::cout << "calcMaxSum(root)     = " << maxSum << " | ruta: ";
    for (char c : maxPath) std::cout << c << " ";
    std::cout << "(esp: 27 | A B D G)\n";

    TNode* neg = new TNode('X', -10);
    neg->left = new TNode('Y', -5);
    neg->right = new TNode('Z', -20);
    calcMaxSum(neg, maxSum, maxPath);
    std::cout << "calcMaxSum(neg)      = " << maxSum << " | ruta: ";
    for (char c : maxPath) std::cout << c << " ";
    std::cout << "(esp: -15 | X Y)\n";

    std::cout << "\n=== NIVEL 3 ===\n";
    std::cout << "existeSumaCamino(22) = " << existeSumaCamino(root, 22) << " (esp: true)\n";
    std::cout << "existeSumaCamino(9)  = " << existeSumaCamino(root, 9) << " (esp: false)\n";
    std::cout << "sumaHojasIzq(root)   = " << sumaHojasIzquierdas(root) << " (esp: 20)\n";

    liberar(root);
    liberar(neg);
    return 0;
}
