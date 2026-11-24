#include <iostream>


void cambio(std::string &X, std::string &Y);
void imprimirInformacion(const std::string nombre, int edad, int anios);

void cambio(std::string &X, std::string &Y){
    std::string temp;  // es como la variable auxiliar
    temp = X;
    X = Y;
    Y = temp;
    /*
    Se hace exactamente lo mismo pero cambia la direccion de memoria se intercambian no los valores.
    */
    std::cout << "X: " << X << "\nY: " << Y << std::endl;

}
void imprimirInformacion(const std::string nombre, int edad, int anios){
    int anio = anios;
    if (anio != 2101){
        std::cout << "Nombre: " << nombre << "\nYear : " << anio << "\nEdad: " << edad << std::endl;
        anio++;edad++;
        imprimirInformacion(nombre,edad,anio);
    }else {std::cout << "finalizamos bucle" << std::endl;}}

int main() {    
    std::string name = "Alex";int age = 24;
    std::cout << "Nombre: " << name << std::endl; std::cout << "Edad: " << age << std::endl;
    imprimirInformacion("Pedro", 22, 2026);

    /* Ahora llamaremos a la direccion de memoria (Hexadecimal)*/

    std::string X = "Cafe";
    std::string Y = "Agua";
    std::string temp; temp = X;
    X = Y;
    Y = temp;
    std::cout << "El cambio se ha hecho correctamente: \n" << "X: " << X << "\nY: " << Y << std::endl;
    X = "Cafe";
    Y = "Agua";
    std::cout << "X: " << X << "\nY: " << Y << std::endl;
    std::cout << "Cambiando...\n";
    cambio(X,Y);

    return 0;
} 

