# Enunciado Base — Red de Proximidad Personal con Grafos

> **Nota:** Este enunciado es un punto de partida editable. Puedes modificar reglas, atributos o agregar nuevas funciones a medida que avancemos.

---

## 1. Idea del ejercicio

Construir un programa de consola en C++ que permita registrar personas (familiares, amigos, conocidos) mediante entrada por teclado, conectarlas con un valor de **proximidad del 1 al 100** (donde 100 representa la máxima cercanía) y **guardar/cargar** toda la red en un archivo `.txt`.

El objetivo principal **no es un sistema profesional**, sino **entender y aplicar en la práctica todos los conceptos de Grafos vistos en cátedra**.

---

## 2. Cómo se traduce tu idea a términos de clase (Grafos)

| Concepto de clase | Qué representa en este ejercicio |
| :--- | :--- |
| **Grafo $G = (V, E)$** | Toda tu red de personas y sus niveles de cercanía |
| **Vértice / Nodo ($V$)** | Cada persona (ej. `Yo`, `Mama`, `Hermano`, `Amigo1`) |
| **Arista / Arco ($E$)** | El vínculo o relación que conecta a dos personas |
| **Peso (Grafo Ponderado)** | El número de proximidad entre `1` y `100` que lleva cada relación |
| **Grafo No Dirigido** | Si la cercanía es mutua (si `Yo`–`Mama` vale `95`, `Mama`–`Yo` también vale `95`) |
| **Grafo Dirigido** | Si la cercanía tiene dirección (lo que `A` siente por `B` puede diferir de `B` hacia `A`) |
| **Vecinos / Adyacentes** | Personas conectadas directamente por una arista |
| **Grado de un vértice** | Cantidad de relaciones directas que tiene una persona |
| **Lista de Adyacencia** | Guardar, para cada persona, la lista de sus vecinos con su peso |
| **Matriz de Adyacencia** | Tabla $N \times N$ donde la celda `[i][j]` guarda la proximidad entre la persona `i` y `j` (`0` si no se conocen) |
| **Camino** | Cadena de personas que conecta a dos personas indirectamente (ej. `Yo -> Hermano -> AmigoDelHermano`) |

---

## 3. Etapas sugeridas (paso a paso)

### Etapa 1 — Definir el tipo de grafo y crear vértices
- Decidir si el grafo será **no dirigido** (relación mutua) o **dirigido**.
- Permitir ingresar personas por teclado (incluyéndote a ti como vértice inicial).
- Evitar personas duplicadas y mostrar la lista de vértices registrados.

### Etapa 2 — Crear aristas con peso (proximidad 1–100)
- Elegir dos personas existentes (por ejemplo, tú y un familiar) y asignar una proximidad entre `1` y `100`.
- Validar que el número esté en el rango `1..100` y que ambas personas existan.
- Mostrar los **vecinos** de una persona y su **grado**.

### Etapa 3 — Persistencia en archivo `.txt`
- Guardar los vértices y las aristas ponderadas en `personas.txt`.
- Al iniciar el programa, cargar automáticamente los datos guardados en `personas.txt`.

Ejemplo de formato simple para `personas.txt` *(editable según prefieras)*:
```text
Yo;Mama;95
Yo;Hermano;88
Hermano;Amigo1;70
```

### Etapa 4 — Consultas y algoritmos de grafos (extensión)
- Listar tus contactos ordenados por mayor proximidad.
- Recorrer la red desde ti usando **BFS** (por niveles: círculo cercano → amigos de amigos) o **DFS** (en profundidad).
- Verificar si existe un **camino** entre dos personas que no se conocen directamente.
- *(Opcional)* Calcular la ruta más cercana o más fuerte entre dos personas.

---

## 4. Mis cambios / notas al enunciado
*(Espacio libre para agregar nuevas ideas o reglas después)*
- 
