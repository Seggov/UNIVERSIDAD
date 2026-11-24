# Módulo 6 — Resolver un laberinto con una lista

**Estado:** pendiente. **Práctica orientativa:** 2–3 horas en bloques manejables.

Continúa desde el [bloque 5](../05_Reenlazado_e_Inversion/Main.cpp). La clase `Nodo` de `Main.cpp` ya guarda un número y un puntero al siguiente nodo. En este módulo, el número representará un movimiento. Conserva la estructura de la clase y cambia el recorrido de la lista para seguir la ruta.

## Enunciado

Un personaje empieza en la esquina superior izquierda de un laberinto. Debe llegar a la esquina inferior derecha siguiendo una ruta de movimientos.

```text
Inicio  .      #
.       #      .
.       .      Salida
```

El personaje empieza en la posición `(fila 0, columna 0)`. La salida está en `(fila 2, columna 2)`. El símbolo `#` representa una pared.

La ruta llega como un texto formado por `U`, `D`, `L` y `R`:

- `U`: arriba.
- `D`: abajo.
- `L`: izquierda.
- `R`: derecha.

Guarda los movimientos en una lista enlazada y síguelos en orden. Si un movimiento lleva al personaje fuera del tablero o a una pared, la ruta falla. Devuelve `true` si, al terminar los movimientos, el personaje está en la salida; en otro caso, devuelve `false`.

Por ejemplo, `DDRR` llega a la salida:

```text
(0,0) → D → (1,0) → D → (2,0) → R → (2,1) → R → (2,2)
```

## Base del código actual

En `Main.cpp` ya tienes:

- La clase `Nodo`, con `valor` y `siguiente`.
- El constructor que guarda el valor y deja `siguiente` en `nullptr`.
- `getValor()`, `getSiguiente()` y `setSiguiente()`.
- La creación manual de nodos y la conexión de estos.
- El puntero `head` y el recorrido con `actual`.

Usa `valor` para guardar cada movimiento como un número: `1` significa U, `2` significa D, `3` significa L y `4` significa R. La lista de `DDRR` contiene los valores `2 → 2 → 4 → 4`.

El ciclo actual invierte la lista. Para el laberinto, conserva el orden de la ruta: recorre desde `head` y avanza con `actual = actual->getSiguiente()`.

## Paso a paso con pseudocódigo

Haz una parte a la vez. El pseudocódigo explica qué debe hacer el programa; todavía debes escribirlo en C++.

### 1. Prepara los movimientos

Para empezar, practica con la ruta `DDRR`. Crea cuatro nodos con los valores `2`, `2`, `4` y `4`, y conéctalos en ese orden, igual que los nodos `a`, `b`, `c` y `d` del código actual.

```text
crear nodo a con valor 2
crear nodo b con valor 2
crear nodo c con valor 4
crear nodo d con valor 4
conectar a → b → c → d
head apunta a a
```

Cuando esa prueba funcione, como siguiente paso puedes leer letras y convertir cada una a su número antes de crear su nodo.

### 2. Prepara la posición inicial

```text
fila = 0
columna = 0
actual = head
```

`actual` recorre la lista. No muevas `head`: lo necesitas para conservar el inicio de la ruta.

### 3. Lee un movimiento por cada nodo

```text
mientras actual no sea nullptr:
    movimiento = valor guardado en actual
```

### 4. Cambia la posición

```text
si movimiento es 1: restar 1 a fila       // U
si movimiento es 2: sumar 1 a fila        // D
si movimiento es 3: restar 1 a columna    // L
si movimiento es 4: sumar 1 a columna     // R
```

### 5. Revisa el tablero

Después de cada movimiento, comprueba si la fila o la columna quedó fuera del rango `0..2`. También comprueba si la nueva posición es una pared: `(0,2)` o `(1,1)`.

```text
si salió del tablero o llegó a una pared:
    devolver false inmediatamente
```

### 6. Avanza al siguiente nodo

```text
actual = actual->getSiguiente()
```

Este paso debe estar dentro del ciclo. Si falta, `actual` nunca cambia y el recorrido no termina.

### 7. Decide si llegó a la salida

Cuando ya no queden nodos, revisa la posición:

```text
si fila es 2 y columna es 2:
    devolver true
si no:
    devolver false
```

### 8. Libera los nodos

Al terminar, borra la lista. Antes de borrar cada nodo, guarda el puntero al siguiente.

```text
mientras head no sea nullptr:
    guardar head->getSiguiente()
    borrar head
    mover head al nodo guardado
```

## Funciones que puedes separar

Primero puedes resolver el ejercicio dentro de `main`, siguiendo la forma del código actual. Cuando funcione, organiza el trabajo en funciones:

```cpp
Nodo* crearRuta(const std::string& movimientos);
bool resolverLaberinto(Nodo* head);
Nodo* liberarRuta(Nodo* head);
```

En `crearRuta`, convierte U, D, L y R a los valores 1, 2, 3 y 4, y conecta los nodos en orden. `resolverLaberinto` comienza en `(0,0)`, sigue la lista y devuelve el resultado. `liberarRuta` borra todos los nodos y devuelve `nullptr`.

## Para avanzar

- La ruta queda en el mismo orden en que se recibió.
- `head` conserva el primer nodo y `actual` recorre la lista.
- Una pared o un movimiento fuera del tablero hace fallar la ruta.
- Solo se llega a la salida si la posición final es `(2,2)`.
- Al terminar, se libera la memoria de todos los nodos.

[Continuar al módulo 7](../07_Modificacion_de_Listas/README.md)
