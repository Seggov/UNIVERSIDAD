# Módulo 05 — Integración y Simulacro Prueba 2

**Objetivo:** unir todos los contenidos (Clases 06, 07, 07.1 y AVL) en un ensayo completo tipo certamen, con trazado en papel y programación bajo restricciones de tiempo y complejidad.  
**Tiempo sugerido:** 90–120 minutos continuos.

[Resumen Prueba 2](../README.md) · [Práctica y Apuntes](01_Practica_y_Apuntes/apuntes.md) · [Enunciados del Simulacro](02_Enunciados/README.md)

---

## Qué integra este módulo

| Bloque | Qué repasa | Dónde se trabaja |
| :--- | :--- | :--- |
| **Resumen rápido y autochequeo** | Formulario de complejidades, errores típicos y traza previa | [`01_Practica_y_Apuntes/`](01_Practica_y_Apuntes/apuntes.md) |
| **Simulacro Parte 1 (16 pts)** | Selección múltiple (TDA Árbol, recorridos, enhebrados, ABB, AVL) | [`02_Enunciados/`](02_Enunciados/README.md) |
| **Simulacro Parte 2 (20 pts)** | Trazado en papel: ABB vs AVL, rotaciones, `remove`, hebras | [`02_Enunciados/`](02_Enunciados/README.md) |
| **Simulacro Parte 3 (40 pts)** | Dos problemas escalados en C++ (`sumarEnRangoABB`, `esArbolCompleto`, etc.) | [`02_Enunciados/Main.cpp`](02_Enunciados/Main.cpp) |

---

## Checklist antes de rendir el simulacro

- [ ] Distingues **altura** (máx. nivel, raíz = 1) de **profundidad** (arcos desde la raíz).
- [ ] Escribes sin dudar los 4 recorridos (**Pre**, **In**, **Post**, **Por Nivel**) y sabes por qué liberar memoria va en Post-orden.
- [ ] Trazas un **Árbol Enhebrado** e identificas cuándo `thread` pasa de `true` a `false`.
- [ ] Resuelves los 3 casos de **`ABB::remove`** (sin romper si eliminas la raíz o si el sucesor tiene hijo derecho).
- [ ] Identificas y ejecutas **LL, RR, LR, RL** actualizando primero la altura del nodo que bajó.
