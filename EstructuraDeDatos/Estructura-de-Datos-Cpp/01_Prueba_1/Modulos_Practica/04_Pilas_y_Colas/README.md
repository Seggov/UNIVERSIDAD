# Módulo 4 — Pilas y colas manuales

**Estado:** conceptos trabajados; completar las operaciones. **Práctica orientativa:** 1–2 horas.

[Resumen de prácticas](../README.md) · [Anterior: módulo 3](../03_Posiciones_y_Eliminacion/README.md) · [Código actual](Main.cpp)

## Explicación sencilla

Una pila retira primero lo último que entró: LIFO. Puede insertar y eliminar al inicio de una lista.

Una cola retira primero lo primero que entró: FIFO. Inserta al final y elimina al inicio. Guarda head y tail para conocer ambos extremos.

| Operación | Pila | Cola |
| --- | --- | --- |
| Agregar | push al inicio | push al final |
| Retirar | pop del inicio | pop del inicio |
| Consultar | top | front |
| Comprobar vacío | empty | empty |

## Enunciado

Completa el menú para manejar una pila y una cola de enteros implementadas con nodos propios. Cada estructura debe tener sus propios nodos.

Para cada una, permite agregar, consultar el siguiente valor que saldrá y retirar. Ante una operación sobre una estructura vacía, informa que no hay elementos y continúa el menú.

Implementa las clases Pila y Cola. En el constructor de Pila, inicializa head en nullptr; en el de Cola, inicializa head y tail en nullptr. Para practicar una interfaz segura, utiliza:

~~~cpp
void push(int valor);
bool pop();
bool empty();
~~~

La pila agrega:

~~~cpp
bool top(int& valor);
~~~

La cola agrega:

~~~cpp
bool front(int& valor);
~~~

pop retorna false si no había nada que retirar. top y front escriben en valor y retornan true cuando existe un elemento; en vacío retornan false y dejan valor sin cambios. El parámetro int& permite escribir ese resultado en la variable del llamador.

## Pasos de práctica

1. Crea una pila vacía y comprueba empty.
2. Inserta 10, 20 y 30 al inicio.
3. Consulta antes de retirar y registra el orden de salida.
4. Crea una cola independiente e inserta esos valores al final.
5. Consulta y retira desde head.
6. Cuando elimines el último de la cola, deja head y tail en nullptr.
7. Vuelve a insertar después de vaciar.
8. Agrega un destructor que libere los nodos de cada estructura.

## Resultados esperados

| Prueba | Pila | Cola |
| --- | --- | --- |
| Insertar 10, 20 y 30; consultar | 30 | 10 |
| Retirar todos | 30, 20, 10 | 10, 20, 30 |
| Retirar estando vacía | false | false |
| Insertar 40 después de vaciar; consultar | 40 | 40 |

En este ejercicio trabaja con una instancia de cada clase y mantén separados sus nodos.

## Qué revisar en Main.cpp

El archivo contiene el menú y la clase Nodo, pero las operaciones todavía no están implementadas. Conecta las opciones del menú con las estructuras cuando puedas probar cada operación por separado.

## Comparación con STL

Después de comprobar la implementación manual, repite el ejemplo con std::stack y std::queue. En STL, pop no retorna el elemento: consulta top o front antes de retirarlo y comprueba empty antes de acceder.

La implementación manual de este módulo se hace sin contenedores STL.

## Para avanzar

Explicas LIFO y FIFO; distingues consultar de retirar; manejas vacío y un solo nodo; la cola vuelve a funcionar después de vaciarse.

Las operaciones básicas cuestan O(1) con el diseño indicado y tail en la cola. Liberar todos los nodos cuesta O(n).

[Continuar al módulo 5](../05_Reenlazado_e_Inversion/README.md)
