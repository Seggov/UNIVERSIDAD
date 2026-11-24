# Módulo 1 — Nodos, punteros y recorrido

**Estado:** conceptos trabajados; repaso de la implementación. **Práctica orientativa:** 45–60 minutos.

[Resumen de prácticas](../README.md) · [Código actual](Main.cpp)

## Explicación sencilla

Un nodo guarda un valor y la dirección del siguiente nodo.
- **Nodo*** guarda una dirección de un Nodo.
- **head** apunta al primero.
- **cursor** permite recorrer sin cambiar head.
- **nullptr** indica que no existe un nodo siguiente.
- **get** obtiene información; **set** la modifica.

Mover cursor cambia el lugar que estás mirando. Modificar el siguiente de un nodo cambia la estructura.

## Enunciado

Construye manualmente esta lista:

~~~text
5 -> 8 -> 3 -> 12 -> nullptr
~~~

Implementa operaciones para mostrar sus valores, contar nodos, sumar valores y buscar el mayor. Conserva head y los enlaces al recorrer.

En esta guía, **contar** significa cantidad de nodos y **sumar** significa suma de valores. Puedes separar estas responsabilidades en tu código:

~~~cpp
void mostrar(Nodo* head);
int contar(Nodo* head);
int sumar(Nodo* head);
int buscarMayor(Nodo* head);
~~~

Para una lista vacía, contar y sumar retornan cero. Antes de llamar a buscarMayor, comprueba que la lista tenga nodos; el programa debe informar que una lista vacía no tiene máximo.

## Pasos de práctica

1. Crea dos nodos, conéctalos y dibuja las direcciones que guardan.
2. Recorre la lista mostrando cada valor.
3. Cuenta un nodo por cada avance del cursor.
4. Suma el valor del nodo que estás mirando en cada iteración.
5. Busca el mayor iniciando la comparación desde un valor de la propia lista.
6. Repite con todos los casos de la tabla.
7. Libera los nodos al terminar, guardando el siguiente antes de borrar el actual.

## Resultados esperados

| Lista | Cantidad | Suma | Mayor |
| --- | --- | --- | --- |
| vacía | 0 | 0 | Informar lista vacía |
| 7 | 1 | 7 | 7 |
| 5, 8, 3, 12 | 4 | 28 | 12 |
| -8, -3, -10 | 3 | -21 | -3 |

## Qué revisar en Main.cpp

- La función contar actual acumula valores y vuelve a sumar el primero. Separa contar de sumar y lee el valor correspondiente al cursor actual.
- Hay lecturas del primer nodo antes de comprobar si existe.
- Iniciar el mayor en cero no funciona con una lista formada solo por negativos.

## Para avanzar

Explicas la diferencia entre dirección y valor; recorres sin perder head; obtienes los resultados de la tabla y distingues una lista vacía antes de acceder a ella.

Mostrar, contar, sumar y buscar el mayor requieren O(n) en general, con espacio auxiliar O(1).

[Continuar al módulo 2](../02_Insercion_Extremos/README.md)
