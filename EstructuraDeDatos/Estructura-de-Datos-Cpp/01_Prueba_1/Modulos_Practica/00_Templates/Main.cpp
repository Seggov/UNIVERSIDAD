#include <iostream>
template <typename T, typename U>

auto max(T x, U y){  // Argumentos del mismo tipo de datos si es que es T y T
    return (x > y) ? x : y;
}

// ahora el compilador automaticamente con la funcion de "auto" deduce el tipo de retorno de la funcion max, dependiendo del tipo de datos que se le pase como argumento.

int main(){

    std::cout << max(3, 7) << std::endl; // Call max para int
    std::cout << max(3.5, 2.5) << std::endl; // Call max para double
    std::cout << max('a', 'b') << std::endl; // Call max para char
    return 0;
}
