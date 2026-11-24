#include <iostream>
#include <limits>
#include <vector>

struct BTNode {
    int value;
    BTNode* left;
    BTNode* right;

    BTNode(int v) : value(v), left(nullptr), right(nullptr) {}
};

class ABB {
private:
    BTNode* root;

    void liberar(BTNode* nodo) {
        if (nodo == nullptr) return;
        liberar(nodo->left);
        liberar(nodo->right);
        delete nodo;
    }

public:
    ABB() : root(nullptr) {}
    ~ABB() { liberar(root); }

    ABB(const ABB&) = delete;
    ABB& operator=(const ABB&) = delete;

    // --- Nivel 1 ---
    bool insert(int value) {
        (void)value;
        return false;
    }

    bool find(int value) const {
        (void)value;
        return false;
    }

    int minimo() const {
        return std::numeric_limits<int>::min();
    }

    int maximo() const {
        return std::numeric_limits<int>::min();
    }

    void inorden(std::vector<int>& out) const {
        (void)out;
    }

    // --- Nivel 2 ---
    bool remove(int value) {
        (void)value;
        return false;
    }

    bool esABBValido() const {
        return false;
    }
};

struct TBTNode {
    char value;
    TBTNode* left;
    TBTNode* right;
    bool leftThread;
    bool rightThread;

    TBTNode(char v)
        : value(v), left(nullptr), right(nullptr), leftThread(true), rightThread(true) {}
};

// --- Nivel 3 ---
void inordenEnhebrado(const TBTNode* root) {
    (void)root;
}

void imprimirVec(const std::vector<int>& v) {
    for (size_t i = 0; i < v.size(); i++) {
        if (i > 0) std::cout << " ";
        std::cout << v[i];
    }
    std::cout << "\n";
}

int main() {
    std::cout << std::boolalpha;

    ABB arbol;
    int vals[] = {50, 30, 70, 20, 40, 60, 80, 65};
    for (int v : vals) arbol.insert(v);

    std::cout << "=== NIVEL 1 ===\n";
    std::cout << "Insertar duplicado 40: " << arbol.insert(40) << " (esp: false)\n";
    std::cout << "Minimo: " << arbol.minimo() << " (esp: 20)\n";
    std::cout << "Maximo: " << arbol.maximo() << " (esp: 80)\n";
    std::vector<int> rec;
    arbol.inorden(rec);
    std::cout << "Inorden inicial : "; imprimirVec(rec);
    std::cout << "Esperado        : 20 30 40 50 60 65 70 80\n";

    std::cout << "\n=== NIVEL 2 ===\n";
    std::cout << "esABBValido inicial : " << arbol.esABBValido() << " (esp: true)\n";
    std::cout << "remove(20) [hoja]   : " << arbol.remove(20) << " (esp: true)\n";
    std::cout << "remove(60) [1 hijo] : " << arbol.remove(60) << " (esp: true)\n";
    std::cout << "remove(50) [raiz 2h]: " << arbol.remove(50) << " (esp: true)\n";
    std::cout << "remove(99) [no ex.] : " << arbol.remove(99) << " (esp: false)\n";

    rec.clear();
    arbol.inorden(rec);
    std::cout << "Inorden final       : "; imprimirVec(rec);
    std::cout << "Esperado            : 30 40 65 70 80\n";
    std::cout << "find(50) / find(65) : " << arbol.find(50) << " / " << arbol.find(65) << " (esp: false / true)\n";
    std::cout << "esABBValido final   : " << arbol.esABBValido() << " (esp: true)\n";

    std::cout << "\n=== NIVEL 3 ===\n";
    TBTNode a('A'), b('B'), c('C'), d('D'), e('E'), f('F');
    a.left = &b;  a.leftThread = false;
    a.right = &c; a.rightThread = false;
    b.left = &d;  b.leftThread = false;
    b.right = &e; b.rightThread = false;
    c.left = &f;  c.leftThread = false;
    c.right = nullptr; c.rightThread = true;

    d.left = nullptr; d.leftThread = true;
    d.right = &b;     d.rightThread = true;
    e.left = &b;      e.leftThread = true;
    e.right = &a;     e.rightThread = true;
    f.left = &a;      f.leftThread = true;
    f.right = &c;     f.rightThread = true;

    std::cout << "Inorden enhebrado: ";
    inordenEnhebrado(&a);
    std::cout << " (esp: D B E A F C)\n";

    return 0;
}
