# Módulo 3 — Posiciones, inserción y eliminación

**Estado:** conceptos trabajados; completar la implementación. **Práctica orientativa:** 1–2 horas.

[Resumen de prácticas](../README.md) · [Anterior: módulo 2](../02_Insercion_Extremos/README.md) · [Código actual](Main.cpp)

## Explicación sencilla

Los índices empiezan en cero. Para modificar el medio, necesitas llegar al nodo anterior a la posición elegida.

~~~text
ANTERIOR -> ACTUAL -> SIGUIENTE
~~~

Antes de insertar, conserva el enlace que ya existía. Antes de eliminar, guarda el nodo que vas a borrar y conecta el resto de la lista. El índice 0 requiere actualizar head.

## Enunciado

Trabaja primero con valores fijos, en lugar de aleatorios. Implementa búsqueda, inserción y eliminación por posición, recogiendo el nuevo head cuando corresponda.

Firmas propuestas para completar el borrador actual:

~~~cpp
int getIndex(Nodo* head, int valor);
Nodo* insert(Nodo* head, int valor, int index);
Nodo* remove(Nodo* head, int index);
Nodo* clear(Nodo* head);
~~~

En insert, crea el nodo dentro de la función después de validar la posición. Adapta las llamadas de Main.cpp a estas firmas.

Para una lista de tamaño n:
- Insertar permite índices entre 0 y n, incluido n para agregar al final.
- Eliminar permite índices entre 0 y n - 1.
- Un índice inválido conserva la lista y no reserva nodos.
- getIndex retorna la primera coincidencia, o -1 si el valor no existe.
- clear libera todos los nodos y retorna nullptr.

## Pasos de práctica

1. Busca un valor contando posiciones desde cero.
2. Inserta al inicio y recoge el nuevo head.
3. Inserta en medio guardando el siguiente antes de cambiar enlaces.
4. Elimina el primer nodo y luego uno intermedio.
5. Elimina el último y comprueba su enlace anterior.
6. Repite con vacío, un nodo e índices inválidos.
7. Libera toda la lista con head = clear(head).

## Ejemplo principal

| Paso | Resultado |
| --- | --- |
| Crear lista | 10, 30, 40 |
| Insertar 20 en índice 1 | 10, 20, 30, 40 |
| Eliminar índice 2 | 10, 20, 40 |
| Buscar 40 | Índice 2 |
| Buscar 99 | -1 |
| Liberar la lista | head es nullptr |

Prueba además insertar en índice n, eliminar hasta vaciar y rechazar índices negativos o demasiado grandes.

## Qué revisar en Main.cpp

- insert cambia un enlace sin conservar el tramo siguiente y utiliza un contador desfasado.
- remove todavía no elimina ni libera nodos; su contador tampoco avanza.
- getIndex retorna 0 cuando no encuentra el valor, confundiendo ese caso con la primera posición.
- Revisa los punteros antiguos después de eliminar: no debes leer un nodo que ya fue liberado.

## Para avanzar

Puedes dibujar el antes y después; resuelves el índice 0; no pierdes nodos; liberas cada eliminado y distingues una búsqueda fallida.

Las búsquedas y modificaciones por posición cuestan O(n) en general. Una cantidad fija de recorridos completos también sigue siendo O(n).

[Continuar al módulo 4](../04_Pilas_y_Colas/README.md)
