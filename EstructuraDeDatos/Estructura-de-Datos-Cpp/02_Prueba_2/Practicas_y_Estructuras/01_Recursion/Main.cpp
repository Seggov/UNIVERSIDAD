#include <iostream>

void caminar(int pasos);

// enfoque recursivo
void caminar(int pasos){
    if (pasos == 0){
        std::cout << "Llegaste a tu destino" << std::endl;
        return;
    }
    else{
        std::cout << "Dando un paso" << std::endl;
        caminar(pasos - 1);
    }
}
int main(){

    std::cout << "RECURSION" << std::endl;
    caminar(5);
    return 0;
}
