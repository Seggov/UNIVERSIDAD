# Módulo 2 — Inserción al inicio y al final

**Estado:** trabajado; comprobar casos borde. **Práctica orientativa:** 1–2 horas.

[Resumen de prácticas](../README.md) · [Anterior: módulo 1](../01_Nodos_Punteros_Recorrido/README.md) · [Código actual](Main.cpp)

## Explicación sencilla

Para insertar al inicio, el nuevo nodo enlaza con el primero anterior y pasa a ser el nuevo head.

Para insertar al final, llegas al último nodo y cambias su enlace siguiente. Si la lista está vacía, el nuevo nodo será también el primero.

Distingue estas dos instrucciones:

~~~cpp
cursor = nuevo;               // Mover un puntero auxiliar.
cursor->setSiguiente(nuevo);   // Cambiar el enlace de un nodo.
~~~

head es una dirección. El nodo al que apunta ocupa la posición 0 de la lista.

## Enunciado

Partiendo de:

~~~text
5 -> 8 -> 3 -> 12 -> nullptr
~~~

Inserta 2 al inicio y 20 al final. Debes obtener:

~~~text
2 -> 5 -> 8 -> 3 -> 12 -> 20 -> nullptr
~~~

Usa nodos recién creados, cuyo siguiente sea nullptr y que todavía no pertenezcan a la lista.

~~~cpp
Nodo* insertarInicio(Nodo* head, Nodo* nuevo);
Nodo* insertarAlFinal(Nodo* head, Nodo* nuevo);
~~~

Ambas funciones retornan el inicio resultante. Recoge el retorno al llamarlas:

~~~cpp
head = insertarInicio(head, nuevo);
head = insertarAlFinal(head, final);
~~~

## Pasos de práctica

1. Inserta en una lista vacía y muestra el resultado.
2. Inserta al inicio de una lista de un nodo.
3. Dibuja el enlace del nuevo nodo antes de cambiar head.
4. Recorre hasta el último nodo para insertar al final.
5. Comprueba que los nodos anteriores siguen conectados.
6. Repite cada prueba con una lista nueva y libera sus nodos al terminar.

## Resultados esperados

| Lista inicial | Operación | Resultado |
| --- | --- | --- |
| vacía | Insertar 4 al inicio | 4 |
| vacía | Insertar 4 al final | 4 |
| 5 | Insertar 2 al inicio | 2, 5 |
| 5 | Insertar 20 al final | 5, 20 |
| 5, 8, 3, 12 | Insertar 2 al inicio y 20 al final | 2, 5, 8, 3, 12, 20 |

## Qué revisar en Main.cpp

La inserción al inicio ya sigue el patrón esperado. La inserción al final todavía debe resolver el caso en que head sea nullptr: el recorrido actual no conecta el nodo en ese caso.

## Para avanzar

Explicas cuándo cambia head y por qué mover cursor no conecta un nodo. Ninguna inserción pierde la lista anterior ni crea ciclos.

Insertar al inicio cuesta O(1). Insertar al final recorriendo desde head cuesta O(n); más adelante usarás un puntero al último para hacerlo en O(1).

[Continuar al módulo 3](../03_Posiciones_y_Eliminacion/README.md)
