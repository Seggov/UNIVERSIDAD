# Módulos de Práctica — Prueba 2 (Estructuras No Lineales)

## Qué estamos haciendo

Esta ruta organiza toda la preparación de la **Prueba 2** separada **por clases oficiales de cátedra** (Unidad 4: Árboles), junto con Árboles AVL y un Simulacro final.

Cada clase/módulo se divide en:
1. **`README.md` del módulo:** explica **los contenidos de la clase** con diagramas, reglas y ejemplos.
2. **`01_Practica_y_Apuntes/`:** carpeta para **ir aprendiendo paso a paso mientras estudiamos juntos**. Incluye:
   - `apuntes.md`: guía ligera para anotar definiciones con tus palabras, trazas y dudas.
   - `Main.cpp`: plantilla **mínima** (sin clases prearmadas) para escribir tú mismo desde cero, paso por paso.
3. **`02_Enunciados/`:** carpeta de **enunciados escalados** (Nivel 1 Básico → Nivel 2 Intermedio → Nivel 3 Reto tipo prueba), con una plantilla más extensa y casos de prueba listos en `Main.cpp`.

Además, tienes la guía visual en PDF: [Guia_Grafica_Prueba_2.pdf](Guia_Grafica_Prueba_2.pdf).

---

## Recorrido por Clases y Módulos

| Módulo | Clase / Fuente | Contenidos (`README.md`) | Práctica y Apuntes | Enunciados Escalados |
| :--- | :--- | :--- | :--- | :--- |
| **00** | Base obligatoria | [Contenidos Recursión](00_Recursion_y_Bases/README.md) | [01_Practica_y_Apuntes](00_Recursion_y_Bases/01_Practica_y_Apuntes/apuntes.md) | [02_Enunciados](00_Recursion_y_Bases/02_Enunciados/README.md) |
| **01** | **Clase 06** | [TDA Árbol y Binarios](01_Clase_06_TDA_Arbol_y_Binarios/README.md) | [01_Practica_y_Apuntes](01_Clase_06_TDA_Arbol_y_Binarios/01_Practica_y_Apuntes/apuntes.md) | [02_Enunciados](01_Clase_06_TDA_Arbol_y_Binarios/02_Enunciados/README.md) |
| **02** | **Clase 07** | [Enhebrados y ABB](02_Clase_07_Enhebrados_y_ABB/README.md) | [01_Practica_y_Apuntes](02_Clase_07_Enhebrados_y_ABB/01_Practica_y_Apuntes/apuntes.md) | [02_Enunciados](02_Clase_07_Enhebrados_y_ABB/02_Enunciados/README.md) |
| **03** | **Clase 07.1** | [Ejercicios de Árboles](03_Clase_07_1_Ejercicios_Arboles/README.md) | [01_Practica_y_Apuntes](03_Clase_07_1_Ejercicios_Arboles/01_Practica_y_Apuntes/apuntes.md) | [02_Enunciados](03_Clase_07_1_Ejercicios_Arboles/02_Enunciados/README.md) |
| **04** | Complemento Prueba 2 | [Árboles AVL y Rotaciones](04_Arboles_AVL_y_Rotaciones/README.md) | [01_Practica_y_Apuntes](04_Arboles_AVL_y_Rotaciones/01_Practica_y_Apuntes/apuntes.md) | [02_Enunciados](04_Arboles_AVL_y_Rotaciones/02_Enunciados/README.md) |
| **05** | Integración | [Simulacro Prueba 2](05_Simulacro_Prueba_2/README.md) | [01_Practica_y_Apuntes](05_Simulacro_Prueba_2/01_Practica_y_Apuntes/apuntes.md) | [02_Enunciados](05_Simulacro_Prueba_2/02_Enunciados/README.md) |

---

## Forma de trabajo recomendada

1. **Lee los contenidos** del `README.md` del módulo (y mira la página correspondiente en [Guia_Grafica_Prueba_2.pdf](Guia_Grafica_Prueba_2.pdf)).
2. **Entra a `01_Practica_y_Apuntes/`:** ve siguiendo los pasos en orden junto con tus apuntes en `apuntes.md` y construyendo el código poco a poco en `Main.cpp` (plantilla leve).
3. **Pasa a `02_Enunciados/`:** resuelve los niveles **1 → 2 → 3** en orden. La plantilla ahí ya trae los casos de prueba para comprobar si tu solución cumple cada requisito.
4. **Compila desde la subcarpeta en la que estés trabajando:**
   ```powershell
   g++ -std=c++17 -Wall -Wextra -Wpedantic Main.cpp -o practica.exe
   .\practica.exe
   ```

---

## Material de apoyo en el repositorio

- [Material Teórico Prueba 2](../Material_Teorico/):
  - [06 - [U4] TDA Árbol, Árboles Binarios, Recorridos.pdf](../Material_Teorico/06%20-%20%5BU4%5D%20TDA%20%C3%81rbol,%20%C3%81rboles%20Binarios,%20Recorridos.pdf)
  - [07 - [U4] Árboles Binarios Enhebrados, ABB.pdf](../Material_Teorico/07%20-%20%5BU4%5D%20%C3%81rboles%20Binarios%20Enhebrados,%20ABB.pdf)
  - [07.1 - [U4] Ejercicios Árboles.pdf](../Material_Teorico/07.1%20-%20%5BU4%5D%20Ejercicios%20%C3%81rboles.pdf)
- Referencia del taller del curso: [Taller-2_Hospital](../Talleres/Taller-2_Hospital/README.md).
- Prácticas previas: [Practicas_y_Estructuras](../Practicas_y_Estructuras/).
