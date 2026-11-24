# Módulo 10 — Integración y simulacros

**Estado:** pendiente. **Práctica orientativa:** 6–8 horas, incluyendo intentos y corrección.

[Anterior: módulo 9](../09_Complejidad_y_POO/README.md)

## Objetivo

Llegar al nivel de la [Primera Evaluación Sumativa](<../../../Evaluaciones_y_Enunciados/EDD 2026_20 - Primera Evaluación Sumativa.pdf>), aplicando lo practicado en los módulos 6–9.

## Explicación sencilla

Resolver operaciones aisladas es el paso previo. Ahora debes leer un enunciado, dividirlo en funciones, integrar sus reglas y comprobar que funcionan juntas.

El trabajo sigue este orden:
1. Identifica entradas, salidas y restricciones.
2. Dibuja un ejemplo pequeño.
3. Resuelve el comportamiento principal.
4. Comprueba límites, memoria y complejidad.
5. Corrige y vuelve a probar con una entrada diferente.

## Enunciado: simulacro completo

Resuelve las cuatro partes del PDF de referencia en **2 horas y 15 minutos continuos**, con compilador y sin consultar tus soluciones anteriores.

| Parte | Trabajo | Puntaje del PDF |
| --- | --- | --- |
| 1 | Selección múltiple: C++, punteros, copia, complejidad, pilas y colas | 16 |
| 2 | Ejecución manual del código y valores finales de data | 15 |
| 3 | createStage, checkStage y las reglas oficiales de modifyStage | 20 |
| 4 | processTickets con atención habitual y cierre | 25 |

Como reparto inicial de práctica puedes reservar 45 minutos para las partes 1–2, 45 para listas y 45 para colas.

### Restricciones que debes respetar

- En listas, usa nodos manuales y las restricciones de memoria y complejidad del PDF.
- En tickets, puedes usar stack y queue de STL.
- Actualiza head cuando cambie el primer nodo.
- Conserva el orden exigido y libera la memoria reservada.
- Distingue las reglas oficiales de las reglas preparatorias del módulo 7.
- Anota cualquier caso no especificado y la interpretación que adoptes.

## Después del primer intento

1. Anota qué terminó funcionando y qué quedó incompleto.
2. Clasifica cada error: lectura del enunciado, sintaxis, enlaces, condiciones, orden o complejidad.
3. Repite únicamente la parte que falló.
4. Haz un segundo intento con las variantes de abajo.

## Variantes para comprobar comprensión

### A. Construcción y simulación

Construye la etapa "142365" y prueba estos esfuerzos iniciales:

| Esfuerzo | Resultado de checkStage |
| --- | --- |
| 61 | false |
| 62 | true |

Con 61, localiza el punto exacto del fallo y explica por qué el poder posterior no lo corrige.

### B. Modificación de listas

Aplica las reglas oficiales de modifyStage a estas entradas:

| Etapa | Esfuerzo inicial | Qué revisar |
| --- | --- | --- |
| "1" | 23 | Sobra suficiente esfuerzo para agregar un jefe |
| "13" | 20 | Falta menos de 5 para completar |
| "39" | 30 | Existen varios jefes y falta más de 20 |

Dibuja el antes y después, incluyendo cualquier cambio de head. Completa además un caso propio de reemplazo de un jefe por varios eventos.

### C. Cierre y desempates de tickets

Usa una jornada de 1 hora y esta cola:

| Llegada | Código | Prioridad | Minutos |
| --- | --- | --- | --- |
| 1 | Q1 | A | 50 |
| 2 | Q2 | M | 25 |
| 3 | Q3 | B | 15 |
| 4 | Q4 | M | 25 |
| 5 | Q5 | B | 15 |

La salida esperada es **Q2, Q3, Q5**. Justifica cantidad, desempate y orden. Explica por qué la jornada termina aunque sobren 5 minutos.

### D. C++ y complejidad

Cambia un dato del programa del módulo 9 y traza otra vez sin ejecutar primero. Luego analiza el tiempo y el espacio de tus propias funciones de listas y tickets.

## Criterio de cierre

- Resuelves una variante sin copiar una solución.
- Tu programa compila y pasa casos borde pertinentes.
- Explicas los enlaces, el orden de atención y cada condición.
- Puedes justificar el tiempo y la memoria utilizados.
- En el segundo intento corriges los errores que habías registrado.

Si una parte sigue fallando, vuelve al módulo que trabaja esa habilidad y repite un ejercicio pequeño antes de otro simulacro.
