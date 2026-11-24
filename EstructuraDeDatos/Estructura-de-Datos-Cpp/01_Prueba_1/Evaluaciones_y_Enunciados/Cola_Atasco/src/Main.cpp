#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
using namespace std;

class Auto
{
private:
    string matricula;
    string marca;
    string gasolina;
    int kilometraje;
    int asientos;
    string duenio;

public:
    Auto(string matricula, string marca, string gasolina,
         int kilometraje, int asientos, string duenio)
    {
        this->matricula = matricula;
        this->marca = marca;
        this->gasolina = gasolina;
        this->kilometraje = kilometraje;
        this->asientos = asientos;
        this->duenio = duenio;
    }

    string getMarca() { return marca; }

    string getDuenio()
    {
        return duenio;
    }

    string getMatricula()
    {
        return matricula;
    }
};

class Nodo
{
private:
    Auto *automovil;
    Nodo *siguiente;

public:
    Nodo(Auto *automovil)
    {
        this->automovil = automovil;
        this->siguiente = nullptr;
    }
};

void desencolar();
void mostrarAutos();

int main()
{
    bool esVerde = true;bool esAmarillo = false;bool esRojo = true;
    const int cantidadMaximCalle = 10;
    int contadorAutos = 0;
    ifstream archivo("dataAuto.txt");
    string linea;
    while (getline(archivo, linea)){
        stringstream ss(linea);
        string matricula;string marca;string gasolina;
        string duenio;string asientos;string kilometraje;
        
        getline(ss, matricula, ';');getline(ss, marca, ';');getline(ss, gasolina, ';');
        getline(ss, kilometraje, ';');getline(ss, asientos, ';');getline(ss, duenio, ';');
        
        int km = stoi(kilometraje);int cantAsientos = stoi(asientos);
        Auto *automovil = new Auto(matricula, marca, gasolina, km, cantAsientos, duenio);
        
        if (esVerde){
            contadorAutos++;
            // imprimimos el automovil
            if (contadorAutos == 10){
                desencolar();
                contadorAutos--;
                cout << "[VERDE] Avanzo un auto. Autos: " // decimos que avanzo el actual
                     << contadorAutos << "/"
                     << cantidadMaximCalle << endl;
            }
        }

            esVerde = false;
           

        if (contadorAutos < cantidadMaximCalle)
        {
            // entrandoAutos();
            contadorAutos++;

            cout << "Entro un auto. Autos: " << contadorAutos << "\n" << cantidadMaximCalle << endl;
        }
        else
        {
            cout << "La calle esta llena." << endl;
            // Aqui posteriormente:
            // evasion();
        }

        // 2. Revisar semaforo
        if (esRojo)
        {
            cout << "[ROJO] Nadie avanza." << endl;
            mostrarAutos();
            esRojo = false;
            esAmarillo = true;
        }
        else if (esAmarillo)
        {
            cout << "[AMARILLO] Preparandose para avanzar." << endl;
            esAmarillo = false;
            esVerde = true;
        }
        esRojo = true;
    }

    return 0;
}

void mostrarAutos()
{
}

void desencolar()
{
}