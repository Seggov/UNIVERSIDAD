# Módulo 9 — C++ de evaluación y complejidad

**Estado:** pendiente; aprovechar la base de POO en Java. **Práctica orientativa:** 4–6 horas.

[Anterior: módulo 8](../08_Colas_y_Prioridades/README.md)

## Explicación sencilla

Aquí el objetivo es seguir lo que hace el código, llamada por llamada.

- Una variable objeto en C++ puede guardar una copia independiente de otro objeto.
- Una referencia o un puntero puede permitir acceder al mismo objeto.
- Una función virtual permite seleccionar la implementación de la clase del objeto.
- Una función virtual pura hace abstracta la clase que la contiene.
- Un operador sobrecargado ejecuta el código escrito por su autor: lee su implementación.

## Enunciado A: ejecución manual

Antes de ejecutar este programa, completa una tabla con r1, r2, r3, r4, r5 y la energía de a, b y c después de cada llamada.

~~~cpp
#include <iostream>

class Unidad {
protected:
    int energia;
public:
    Unidad(int e) : energia(e) {}
    virtual int actuar(int x) {
        energia -= x;
        return energia;
    }
    bool operator<(const Unidad& otra) const {
        return energia < otra.energia;
    }
    virtual ~Unidad() = default;
};

class Curador : public Unidad {
public:
    Curador(int e) : Unidad(e) {}
    int actuar(int x) override {
        energia += 2 * x;
        return energia;
    }
};

int main() {
    Unidad a(20);
    Curador b(10);
    Unidad* p = &b;

    int r1 = a.actuar(3);
    int r2 = p->actuar(4);
    bool r3 = a < b;
    Unidad c = a;
    int r4 = c.actuar(2);
    int r5 = a.actuar(1);

    std::cout << r1 << " " << r2 << " " << r3 << " "
              << r4 << " " << r5 << std::endl;
}
~~~

p apunta a b. a, b y c son objetos locales que se destruyen al salir de su ámbito. La copia c guarda su propio entero energia.

Después de predecir, compila y compara. r3 se imprime como 0 o 1.

## Enunciado B: variantes de C++

Responde y comprueba una variante a la vez:
1. Explica por qué p ejecuta la implementación de Curador.
2. Quita virtual de actuar en Unidad y también override en Curador. Vuelve a predecir la salida.
3. Agrega un constructor de copia con esta firma y copia energia:

~~~cpp
Unidad(const Unidad& otra);
~~~

4. Explica por qué modificar c no cambia a.
5. Cambia el operador < para comparar el doble de la energía del primer objeto con la del segundo. Predice el nuevo r3.
6. Explica por qué una clase que declara una función virtual pura no puede instanciarse directamente:

~~~cpp
virtual int actuar(int x) = 0;
~~~

Ese último cambio es una variante independiente: el programa original crea un objeto Unidad y necesitaría adaptarse si Unidad fuera abstracta.

## Enunciado C: complejidad

Para cada situación, escribe el orden de crecimiento y justifica cuántas operaciones se realizan. n es la cantidad de elementos.

| Situación | Tiempo | Espacio auxiliar |
| --- | --- | --- |
| Consultar el primer nodo de una lista | Completar | Completar |
| Recorrer una lista completa | Completar | Completar |
| Dividir un contador entero positivo entre 2 hasta llegar a 1 | Completar | Completar |
| Para cada uno de n elementos, repetir las divisiones anteriores empezando en n | Completar | Completar |
| Comparar cada elemento con todos los demás | Completar | Completar |

Compara O(1), O(log n), O(n), O(n log n) y O(n²).

También analiza una búsqueda lineal:
- Mejor caso: el valor está en el primer nodo.
- Peor caso: el valor no está.
- Mantén fijo el tamaño n al comparar los casos.

Distingue la memoria de la entrada, los nodos del resultado y el espacio auxiliar. Al construir una lista necesitas memoria para los nodos; recorrerla con un cursor no exige otra lista.

## Para avanzar

- Predices antes de compilar y explicas cada diferencia.
- Reconoces cuándo hay copia y cuándo hay acceso al mismo objeto.
- Distingues virtual de virtual pura.
- Interpretas el operador según su implementación.
- Justificas tiempo y espacio sin depender del nombre de la función.

Material de apoyo: clases 01, 02 y 05 en [Material de clases](../../01_Material_de_Clases/).

[Continuar al módulo 10](../10_Simulacro_Evaluacion/README.md)
