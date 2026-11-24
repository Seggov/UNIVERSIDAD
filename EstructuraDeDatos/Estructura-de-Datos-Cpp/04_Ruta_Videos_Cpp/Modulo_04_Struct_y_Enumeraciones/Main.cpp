#include <iostream>
using namespace std;

struct Estudiante {
    string nombre;
    double promedio;
    bool inscrito;
};

void imprimirNombre(Estudiante estudiante);
enum Universidad {
    UCN = 780,      
    UCH = 845,     
    UC = 910,       
    USACH = 630,    
    UTFSM = 705,    
    UDEC = 560,     
    UAI = 995,      
    UDP = 870,      
    UANDES = 745,   
    UTA = 520       
};

void imprimirNombre(Estudiante estudiante){
    cout << estudiante.nombre << "\n" << endl;
}
int main() {
    Estudiante estudiante1;
    estudiante1.nombre = "Pedrosky";
    estudiante1.promedio = 67.8;
    estudiante1.inscrito = true;

    Estudiante estudiante2;
    estudiante2.nombre = "Antonia";
    estudiante2.promedio = 82.5;
    estudiante2.inscrito = false;

    cout << estudiante1.nombre << " | Promedio: " << estudiante1.promedio
         << " | Inscrito: " << (estudiante1.inscrito ? "Si" : "No") << endl;

    cout << estudiante2.nombre << " | Promedio: " << estudiante2.promedio
         << " | Inscrito: " << (estudiante2.inscrito ? "Si" : "No") << endl;

    imprimirNombre(estudiante1);

    Universidad uni = UCN;
    //cout << uni; // retorna 780
    //cout << Universidad::UCN; // 780

    switch (uni) {
        case UCN:
            cout << "Universidad Catolica del Norte";
            break;

        case UCH:
            cout << "Universidad de Chile";
            break;

        case UC:
            cout << "Pontificia Universidad Catolica de Chile";
            break;

        case USACH:
            cout << "Universidad de Santiago de Chile";
            break;

        case UTFSM:
            cout << "Universidad Tecnica Federico Santa Maria";
            break;

        case UDEC:
            cout << "Universidad de Concepcion";
            break;

        case UAI:
            cout << "Universidad Adolfo Ibanez";
            break;

        case UDP:
            cout << "Universidad Diego Portales";
            break;

        case UANDES:
            cout << "Universidad de los Andes";
            break;

        case UTA:
            cout << "Universidad de Tarapaca";
            break;

        default:
            cout << "Universidad desconocida";
            break;
    }

    cout << "\nPuntaje de la universidad: " << uni << endl;


    
    

    return 0; // todo bien
}