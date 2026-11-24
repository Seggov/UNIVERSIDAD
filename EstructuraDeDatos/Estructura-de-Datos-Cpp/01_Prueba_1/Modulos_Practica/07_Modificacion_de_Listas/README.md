# Módulo 7 — Modificar una lista durante el recorrido

**Estado:** pendiente. **Práctica orientativa:** 3–4 horas.

[Anterior: módulo 6](../06_Construccion_y_Laberinto/README.md)

## Explicación sencilla

El recorrido ahora también cambia la lista. Piensa siempre en:

~~~text
ANTERIOR -> ACTUAL -> SIGUIENTE
~~~

- Antes de desconectar actual, conserva el siguiente.
- Si eliminas actual, el anterior debe enlazar con siguiente.
- Si modificas el primer nodo, cambia head.
- Para sustituir un nodo por varios, conecta la nueva cadena con el resto antes de perder su referencia.

Todas las funciones de este ejercicio retornan el nuevo head. Recoge ese resultado al llamarlas.

## Enunciado

Usa NodoEvento y las funciones del módulo 6. Implementa estas tres operaciones por separado:

~~~cpp
NodoEvento* adaptarEtapa(NodoEvento* head, int esfuerzoInicial);
NodoEvento* eliminarJefeMasCostoso(NodoEvento* head);
NodoEvento* reemplazarPrimerJefe(NodoEvento* head);
~~~

Estas son **reglas preparatorias de práctica**. El reto final será aplicar las reglas de modifyStage del PDF.

### A. Adaptar una etapa

Asume esfuerzo inicial positivo. Simula la etapa original:
1. Si encuentras un primer fallo, inserta un POWER_UP(5) inmediatamente antes de ese evento y termina la adaptación.
2. Si completas la etapa y sobran 21 o más puntos, agrega un BOSS(20) al final.
3. Si completas la etapa y sobran menos de 21 puntos, conserva la lista.

Aplica solamente una de estas acciones por llamada. Insertar un poder una vez puede ser insuficiente para volver superable la etapa.

### B. Eliminar el jefe más costoso

Elimina un único BOSS: el de mayor esfuerzo. Ante empate, elimina el primero de los empatados. Si no existe ninguno, conserva la lista. Libera el nodo eliminado.

### C. Reemplazar el primer jefe

Sustituye el primer BOSS por esta cadena:

~~~text
POWER_UP(10) -> ENEMY(2) -> ENEMY(2)
~~~

Conserva lo que venía antes y después. Libera el jefe reemplazado. Si no hay jefe, conserva la lista.

## Pasos de práctica

1. Inserta antes del primer nodo y devuelve el nuevo head.
2. Repite la inserción antes de un nodo intermedio.
3. Elimina un jefe situado al inicio, en medio y al final.
4. Busca el jefe más costoso guardando también su anterior.
5. Reemplaza un nodo por una cadena de tres.
6. Ejecuta cada operación sobre una lista recién construida y compara el antes y después.

## Ejemplos esperados

| Operación | Entrada | Resultado |
| --- | --- | --- |
| adaptarEtapa, esfuerzo 1 | "1" | POWER_UP(5) -> ENEMY(2) |
| adaptarEtapa, esfuerzo 23 | "1" | ENEMY(2) -> BOSS(20) |
| adaptarEtapa, esfuerzo 22 | "1" | ENEMY(2), sin cambios |
| adaptarEtapa, esfuerzo 17 | "123" | ENEMY(2) -> POWER_UP(5) -> POWER_UP(5) -> BOSS(20) |
| eliminarJefeMasCostoso | "369" | BOSS(20) -> BOSS(40) |
| reemplazarPrimerJefe | "13" | ENEMY(2) -> POWER_UP(10) -> ENEMY(2) -> ENEMY(2) |

También prueba lista vacía, un solo jefe, varios jefes empatados y una lista sin jefes.

## Para avanzar

- Actualizas head cuando corresponde.
- No accedes a un nodo después de hacer delete.
- Creas únicamente los nodos que requiere la transformación.
- Cada operación trabaja en O(n), con espacio auxiliar constante aparte de los nodos nuevos.
- Comprendes que una cantidad fija de recorridos completos sigue siendo O(n).

## Reto al nivel de la prueba

Implementa modifyStage con las reglas de la [primera evaluación](<../../../Evaluaciones_y_Enunciados/EDD 2026_20 - Primera Evaluación Sumativa.pdf>): colocación de jefe, alternativa de dos enemigos, potenciador antes del fallo y eliminación o sustitución de jefes.

Identifica las diferencias con las reglas preparatorias anteriores. Prueba los límites de cada condición y anota los casos que el enunciado no especifique. Evita recorrer toda la etapa de nuevo por cada posición candidata: eso puede producir O(n²).

[Continuar al módulo 8](../08_Colas_y_Prioridades/README.md)
