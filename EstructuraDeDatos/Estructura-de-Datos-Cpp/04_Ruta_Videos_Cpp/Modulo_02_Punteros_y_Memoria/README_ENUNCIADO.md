# Enunciado 02 — Registro dinámico de notas

Un curso necesita guardar una cantidad de notas conocida durante la ejecución. Usa notas enteras de 1 a 7 y un arreglo dinámico de int. No uses vector ni un arreglo de capacidad fija como almacenamiento principal.

## Requisitos

1. `crearNotas(n)` devuelve nullptr si n <= 0; en otro caso reserva n enteros inicializados en cero.
2. `cambiarNota(notas, n, posicion, valor)` devuelve false sin modificar nada si el puntero es nulo, n <= 0, el índice está fuera de [0, n) o la nota está fuera de [1, 7]. Si todo es válido, guarda la nota y devuelve true.
3. `promedio(notas, n)` devuelve 0.0 si el puntero es nulo o n <= 0; en otro caso devuelve la media como double. Se llamará cuando todas las posiciones tengan notas válidas.
4. `liberarNotas(int*& notas)` libera el arreglo y deja el puntero del llamador en nullptr. Debe poder llamarse otra vez sin problemas.

## Casos obligatorios

- Crea 3 notas y carga 4, 6 y 5: promedio 5.0.
- Cambia la posición 0 por 7: promedio 6.0.
- Rechaza índices -1 y 3, y notas 0 y 8, sin alterar los datos.
- crearNotas(0) y crearNotas(-2) devuelven nullptr.
- cambiarNota(nullptr, 3, 0, 5) devuelve false y promedio(nullptr, 3) devuelve 0.0.
- Libera el arreglo, comprueba nullptr y vuelve a llamar a liberarNotas.

Puedes probar con datos escritos directamente en main; no hace falta un menú ni entrada por teclado.

## Para la evaluación

Explica por qué usas delete[], por qué el parámetro de liberarNotas es int*& y qué ocurriría si intentaras leer el arreglo después de liberarlo. Debe quedar toda la memoria reservada liberada.
