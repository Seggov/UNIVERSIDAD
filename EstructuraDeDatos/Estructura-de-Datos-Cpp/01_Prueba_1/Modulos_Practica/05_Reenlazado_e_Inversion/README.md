# Módulo 5 — Reenlazado e inversión de listas

**Estado:** en progreso; punto actual de estudio. **Práctica orientativa:** 1–2 horas.

[Resumen de prácticas](../README.md) · [Anterior: módulo 4](../04_Pilas_y_Colas/README.md) · [Código actual](Main.cpp)

## Explicación sencilla

Invertir consiste en cambiar la dirección de los enlaces. Los nodos siguen siendo los mismos y sus valores permanecen iguales.

Usas tres punteros auxiliares:
- **anterior:** inicio de la parte que ya invertiste.
- **actual:** nodo que estás procesando.
- **siguiente:** respaldo del nodo que procesarás después.

Estos nombres son variables del algoritmo. En tu lista simple, el nodo continúa teniendo un valor y un enlace siguiente.

## Enunciado

Transforma:

~~~text
10 -> 20 -> 30 -> 40 -> nullptr
~~~

En:

~~~text
40 -> 30 -> 20 -> 10 -> nullptr
~~~

Implementa una función que retorne el nuevo inicio:

~~~cpp
Nodo* invertir(Nodo* head);
~~~

Recoge su resultado:

~~~cpp
head = invertir(head);
~~~

Durante la inversión:
- Modifica únicamente enlaces.
- Conserva todos los nodos y sus valores.
- Usa una cantidad constante de punteros auxiliares.
- Resuelve el ejercicio sin crear o eliminar nodos y sin contenedores STL.

La liberación de la lista se realiza después de mostrar y comprobar el resultado.

## Pasos de práctica

1. Dibuja los cuatro nodos y sus enlaces originales.
2. Inicia anterior en nullptr y actual en head.
3. Guarda el siguiente de actual antes de cambiar su enlace.
4. Enlaza actual con anterior.
5. Avanza anterior al nodo procesado y actual al nodo guardado.
6. Repite hasta que actual sea nullptr.
7. Usa anterior como nuevo head y muestra la lista.

## Recorrido esperado

| Momento | Parte invertida desde anterior | actual |
| --- | --- | --- |
| Inicio | vacía | 10 |
| Después de procesar 10 | 10 -> nullptr | 20 |
| Después de procesar 20 | 20 -> 10 -> nullptr | 30 |
| Después de procesar 30 | 30 -> 20 -> 10 -> nullptr | 40 |
| Después de procesar 40 | 40 -> 30 -> 20 -> 10 -> nullptr | nullptr |

Al terminar, head debe apuntar a 40.

## Qué revisar en Main.cpp

El ciclo actual ya sigue el orden de guardar, girar y avanzar. Falta asignar el nuevo inicio a head y mostrar el resultado. Después puedes extraer el algoritmo a la función invertir.

Si head conserva la dirección del antiguo primero, un recorrido desde él solo mostrará ese nodo: ahora se encuentra al final.

## Casos para comprobar

| Lista inicial | Resultado |
| --- | --- |
| vacía | vacía |
| 10 | 10 |
| 10, 20 | 20, 10 |
| 10, 20, 30, 40 | 40, 30, 20, 10 |

Invierte dos veces y comprueba que recuperas el orden original. Puedes mostrar las direcciones para verificar que conservaste los mismos nodos.

## Para avanzar

Explicas qué guarda cada auxiliar, por qué hay que respaldar siguiente y cuándo se actualiza head. Tu función funciona con vacío y un nodo, conserva la estructura y cuesta O(n) con espacio auxiliar O(1).

[Continuar al módulo 6](../06_Construccion_y_Laberinto/README.md)
