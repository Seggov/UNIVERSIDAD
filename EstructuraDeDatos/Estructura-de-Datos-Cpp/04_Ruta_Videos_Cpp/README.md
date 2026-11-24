# Ruta de C++: videos 45 al 62

Seis módulos para avanzar por el curso y resolver un enunciado por grupo. Esta ruta complementa los módulos de estructuras de datos existentes.

[Playlist del curso](https://www.youtube.com/playlist?list=PL5YuOOJ-FGGjjK8j50TkEcjCcZ8dRAiPy). Busca el número **# del título**, no la posición del reproductor.

| Módulo | Videos obligatorios, en orden | Enunciado |
| --- | --- | --- |
| [01 — Direcciones y referencias](Modulo_01_Direcciones_y_Referencias/README_CONTENIDOS.md) | 45, 46, 47 | Transferencia de saldo |
| [02 — Punteros y memoria](Modulo_02_Punteros_y_Memoria/README_CONTENIDOS.md) | 49, 50, 52 | Registro dinámico de notas |
| [03 — Recursividad y templates](Modulo_03_Recursividad_y_Templates/README_CONTENIDOS.md) | 53, 54 | Comparaciones genéricas y suma recursiva |
| [04 — Struct y enumeraciones](Modulo_04_Struct_y_Enumeraciones/README_CONTENIDOS.md) | 55, 56, 57 | Lista de tareas con nodos |
| [05 — Clases y constructores](Modulo_05_Clases_y_Constructores/README_CONTENIDOS.md) | 58, 59, 60 | Cuenta con estado propio |
| [06 — Encapsulamiento y herencia](Modulo_06_Encapsulamiento_y_Herencia/README_CONTENIDOS.md) | 61, 62 | Cuentas con encapsulamiento y herencia |

Los videos **48 (Luhn)** y **51 (Tic Tac Toe)** son proyectos opcionales: puedes ver el 48 al cerrar el módulo 1 y el 51 durante el módulo 2, antes del 52. Sus técnicas no serán requisitos de los enunciados.

## Forma de trabajo

1. Empieza por el módulo 01, videos 45–47.
2. Lee su README_CONTENIDOS.md y después README_ENUNCIADO.md.
3. Completa los TODO de main.cpp. Las bases compilan, pero NO son soluciones: los retornos provisionales deben reemplazarse.
4. Ejecuta los casos indicados y explica lo que ocurre antes de avanzar.
5. Pide en el chat: «Evalúa el módulo N de 04_Ruta_Videos_Cpp». Revisaremos código, resultados y explicación; corregirás lo pendiente.

Se presupone la base anterior al video 45: variables, condiciones, ciclos, funciones, arreglos y strings. Si algo falla, repasamos ese concepto concreto. Cada enunciado puede usar también lo aprendido en los módulos anteriores. No requiere contenidos de videos posteriores.

## Evaluación de cada módulo: 10 puntos

- Funcionamiento: 4 puntos.
- Casos borde y validación: 2 puntos.
- Uso correcto del concepto central: 2 puntos.
- Explicación y claridad del código: 2 puntos.

Para avanzar: al menos 8/10, sin accesos inválidos a memoria ni memoria dinámica sin liberar. Los criterios específicos están en cada enunciado. No hay soluciones incluidas ni calificaciones asignadas todavía.

## Compilar

Desde la carpeta del módulo, con GCC y C++17:

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp -o practica.exe
.\practica.exe
```

## Alcance para la evaluación final

Esta ruta prepara memoria, referencias, funciones, templates de funciones, struct, nodos, métodos, constructores y herencia. Después hay que integrar las guías existentes de listas, pilas y colas y complementar complejidad, templates de clases, copia, destructores, funciones virtuales y operadores sobrecargados. Terminar estos seis módulos no equivale a cubrir por completo la evaluación de estructuras de datos.
