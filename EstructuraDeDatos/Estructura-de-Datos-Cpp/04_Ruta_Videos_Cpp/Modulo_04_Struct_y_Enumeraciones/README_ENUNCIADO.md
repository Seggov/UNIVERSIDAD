# Enunciado 04 — Lista de tareas con nodos

Representa tareas mediante una lista enlazada simple. Cada tarea contiene un identificador entero positivo y un estado: PENDIENTE o COMPLETADA. La base ya declara enum, Tarea y Nodo; debes programar las operaciones.

## Requisitos

1. `agregarInicio(Nodo*& head, const Tarea& tarea)`: rechaza id <= 0 y duplicados devolviendo false. Si es válido, crea un nodo, copia la tarea, conecta su siguiente al antiguo head y actualiza head. Devuelve true.
2. `completar(Nodo* head, int id)`: busca por id y cambia el estado a COMPLETADA. Devuelve true si existe, incluso si ya estaba completada; false si no existe.
3. `contarPendientes(const Nodo* head)`: devuelve cuántas tareas siguen pendientes, sin modificar la lista.
4. `mostrar(const Nodo* head)`: imprime cada id y su estado, en orden de recorrido.
5. `liberarLista(Nodo*& head)`: guarda el siguiente antes de eliminar cada nodo; termina dejando head en nullptr.

No uses vector, list ni clases propias. Puedes recorrer con while. No se exige eliminar nodos individuales ni invertir la lista.

## Casos obligatorios

- Lista vacía: pendientes 0, completar devuelve false y liberar no falla.
- Agrega tareas pendientes 10, 20 y 30: el recorrido debe ser 30 -> 20 -> 10 y pendientes 3.
- Completa 20: pendientes 2. Repite completar 20: sigue en 2.
- Completa 99: false y ningún cambio.
- Rechaza otro id 20 y el id 0: siguen existiendo solo tres nodos.
- Libera y comprueba head == nullptr; vuelve a liberar.

## Para la evaluación

Explica qué copia el parámetro tarea al guardarlo en el nodo, por qué agregarInicio recibe head por referencia y por qué debes guardar siguiente antes de delete. Dibuja los tres nodos y sus enlaces antes de liberar.
