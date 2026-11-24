#include <iostream>
using namespace std;
template <typename T>

int sumarRecursivo(const int* datos, int n);

template <typename T>
T mayor(T a, T b) {
    return (a > b) ? a : b;
}

int sumarRecursivo(const int* datos, int n) {
    if (datos == nullptr || n <= 0) {
        return 0;
    }

    return datos[0] + sumarRecursivo(datos + 1, n - 1);
}

int main() {
    cout << "Modulo 03: completa las funciones y los casos.\n";
    const int datos[] = {1,3,4,5,2,6,2,1,4,6,2,1,4,6};
    cout << sumarRecursivo(datos, 14) << endl;
    return 0;
}
