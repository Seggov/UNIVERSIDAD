#include <iostream>
#include <vector>

using namespace std;

struct Nodo
{
    char valor;
    int izquierdo;
    int derecho;
};

int main()
{
    vector<Nodo> arbol = {
        {'A', 1, 2},     // Nodo 0
        {'B', -1, -1},   // Nodo 1
        {'C', -1, -1}    // Nodo 2
    };

    for (int i = 0; i < arbol.size(); i++)
    {
        cout << "Nodo: " << arbol[i].valor << endl;

        if (arbol[i].izquierdo != -1)
        {
            cout << "  Izquierdo: "
                 << arbol[arbol[i].izquierdo].valor << endl;
        }

        if (arbol[i].derecho != -1)
        {
            cout << "  Derecho: "
                 << arbol[arbol[i].derecho].valor << endl;
        }
    }

    return 0;
}