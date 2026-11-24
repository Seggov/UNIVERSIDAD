#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits>
#include <vector>

struct NodoAVL {
    int clave;
    NodoAVL* izq;
    NodoAVL* der;
    int altura;

    NodoAVL(int k) : clave(k), izq(nullptr), der(nullptr), altura(1) {}
};

class ArbolAVL {
private:
    NodoAVL* raiz;

    void liberar(NodoAVL* n) {
        if (n == nullptr) return;
        liberar(n->izq);
        liberar(n->der);
        delete n;
    }

    // --- Nivel 1 ---
    int altura(const NodoAVL* n) const {
        (void)n;
        return 0;
    }

    void actualizarAltura(NodoAVL* n) {
        (void)n;
    }

    int obtenerFB(const NodoAVL* n) const {
        (void)n;
        return 0;
    }

    NodoAVL* rotarDerecha(NodoAVL* z) {
        (void)z;
        return z;
    }

    NodoAVL* rotarIzquierda(NodoAVL* z) {
        (void)z;
        return z;
    }

    // --- Nivel 2 ---
    NodoAVL* balancear(NodoAVL* nodo) {
        (void)nodo;
        return nodo;
    }

    NodoAVL* insertarNodo(NodoAVL* nodo, int clave, bool& insertado) {
        (void)clave;
        (void)insertado;
        return nodo;
    }

    // --- Nivel 3 ---
    NodoAVL* menorNodo(NodoAVL* nodo) const {
        while (nodo != nullptr && nodo->izq != nullptr) nodo = nodo->izq;
        return nodo;
    }

    NodoAVL* eliminarNodo(NodoAVL* nodo, int clave, bool& eliminado) {
        (void)clave;
        (void)eliminado;
        return nodo;
    }

    void inordenRec(const NodoAVL* n, std::vector<int>& out) const {
        if (n == nullptr) return;
        inordenRec(n->izq, out);
        out.push_back(n->clave);
        inordenRec(n->der, out);
    }

    bool verificarRec(const NodoAVL* n, long long minV, long long maxV, int& altReal) const {
        if (n == nullptr) {
            altReal = 0;
            return true;
        }
        if (n->clave <= minV || n->clave >= maxV) return false;

        int altI = 0, altD = 0;
        if (!verificarRec(n->izq, minV, n->clave, altI)) return false;
        if (!verificarRec(n->der, n->clave, maxV, altD)) return false;

        altReal = 1 + std::max(altI, altD);
        if (n->altura != altReal) return false;
        if (std::abs(altI - altD) > 1) return false;
        return true;
    }

public:
    ArbolAVL() : raiz(nullptr) {}
    ~ArbolAVL() { liberar(raiz); }

    ArbolAVL(const ArbolAVL&) = delete;
    ArbolAVL& operator=(const ArbolAVL&) = delete;

    bool insertar(int clave) {
        bool insertado = false;
        raiz = insertarNodo(raiz, clave, insertado);
        return insertado;
    }

    bool eliminar(int clave) {
        bool eliminado = false;
        raiz = eliminarNodo(raiz, clave, eliminado);
        return eliminado;
    }

    int getAlturaTotal() const { return altura(raiz); }

    std::vector<int> inorden() const {
        std::vector<int> out;
        inordenRec(raiz, out);
        return out;
    }

    bool verificarAVL() const {
        int alt = 0;
        return verificarRec(
            raiz,
            std::numeric_limits<long long>::min(),
            std::numeric_limits<long long>::max(),
            alt
        );
    }
};

int main() {
    std::cout << std::boolalpha;

    std::cout << "=== NIVEL 1 y 2 ===\n";
    ArbolAVL avl;
    int secuencia[] = {10, 20, 30, 15, 25, 5, 1};
    for (int x : secuencia) avl.insertar(x);

    std::cout << "Duplicado 20 : " << avl.insertar(20) << " (esp: false)\n";
    std::cout << "AVL valido?  : " << avl.verificarAVL() << " (esp: true)\n";
    std::cout << "Altura AVL   : " << avl.getAlturaTotal() << " (esp: 4)\n";
    std::cout << "Inorden      : ";
    for (int x : avl.inorden()) std::cout << x << " ";
    std::cout << "(esp: 1 5 10 15 20 25 30)\n";

    std::cout << "\n=== NIVEL 3 ===\n";
    std::cout << "Eliminar 20  : " << avl.eliminar(20) << " | valido? " << avl.verificarAVL() << " (esp: true)\n";
    std::cout << "Eliminar 30  : " << avl.eliminar(30) << " | valido? " << avl.verificarAVL() << " (esp: true)\n";

    ArbolAVL estres;
    for (int i = 1; i <= 15; i++) estres.insertar(i);
    std::cout << "Estres 1..15 : valido=" << estres.verificarAVL()
              << " | altura=" << estres.getAlturaTotal() << " (esp: true | altura=4)\n";

    return 0;
}
