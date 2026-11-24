# Módulo 8 — Colas, prioridades y combinaciones

**Estado:** pendiente. **Práctica orientativa:** 4–5 horas.

[Anterior: módulo 7](../07_Modificacion_de_Listas/README.md)

## Explicación sencilla

Una cola conserva el orden de llegada. Aquí debes elegir entre sus primeros cinco elementos y mantener el orden de los que no eliges.

Empieza con FIFO sencillo. Después agrega una regla a la vez: candidatos, prioridad, tiempo y cierre de jornada.

Con std::queue, front() consulta el primero y pop() lo retira sin retornarlo. Lee el elemento antes de retirarlo.

## Datos y función

Cada Ticket contiene código, área, prioridad A/M/B y minutos positivos. Asume datos válidos y horasJornada mayor o igual a cero.

~~~cpp
struct Ticket {
    std::string codigo;
    std::string area;
    char prioridad;
    int minutos;
};

std::queue<Ticket> processTickets(
    std::queue<Ticket> pendientes,
    int horasJornada
);
~~~

Usa std::queue y, si te ayuda, std::stack. Puedes guardar hasta cinco candidatos en un arreglo fijo. La función recibe una copia de pendientes y retorna únicamente los tickets atendidos.

## Enunciado

Procesa los tickets según su orden de llegada y el tiempo disponible, expresado inicialmente en horas.

### Atención habitual

- Convierte las horas disponibles a minutos.
- Sigue los turnos A, A, M, A, B, repitiendo la secuencia.
- Considera solo los cinco pendientes más antiguos, o todos si hay menos.
- Elige el más antiguo de la prioridad del turno que quepa en el tiempo restante.
- Avanza de turno tanto si atiendes como si no encuentras candidato.
- Descuenta tiempo únicamente al atender.
- Los no elegidos conservan su orden relativo. Después de atender, actualiza la ventana de candidatos.
- Si una vuelta completa de turnos no produce atención y la ventana no cambia, termina.

### Cierre de jornada

Cuando resten 60 minutos o menos, considera los cinco candidatos disponibles en ese momento una sola vez:
1. Elige la combinación que permita atender más tickets sin superar el tiempo.
2. Ante empate, prefiere más tickets A; luego más tickets M.
3. Si persiste el empate, prefiere los de llegada más antigua.
4. Atiende los seleccionados por prioridad A, M, B, manteniendo llegada entre iguales.
5. Finaliza la jornada después de esa selección, aunque sobre tiempo.

Para concretar el último desempate en esta práctica, compara las posiciones de llegada de cada selección ordenadas de menor a mayor; prefiere la que tenga la menor posición en la primera diferencia.

Si no hay tickets, no queda tiempo o ningún candidato cabe, retorna lo atendido hasta ese momento.

## Pasos de práctica

1. Atiende una cola completa en FIFO y muestra los códigos.
2. Selecciona un ticket entre los primeros cinco.
3. Reconstruye los pendientes conservando el orden.
4. Incorpora la secuencia de prioridades y el límite de tiempo.
5. Practica combinaciones con dos candidatos; luego con tres y con cinco.
6. Integra el cierre y comprueba cuándo termina.

**Cuidado con el orden:** si retiras los primeros cinco, sus sobrevivientes deben quedar delante de los que nunca retiraste. Puedes construir una cola auxiliar con esos sobrevivientes y agregar después el resto.

Con cinco candidatos hay 32 subconjuntos, incluido el vacío. Puedes comprobarlos y comparar sus resultados; no basta con elegir el ticket más corto o el de mayor prioridad.

## Ejemplo 1: cierre desde el inicio

Jornada de 1 hora:

| Llegada | Código | Prioridad | Minutos |
| --- | --- | --- | --- |
| 1 | T1 | A | 60 |
| 2 | T2 | M | 30 |
| 3 | T3 | M | 30 |
| 4 | T4 | B | 10 |

Salida: **T2, T3**. Atiendes dos tickets medios; un ticket alto resolvería menos incidentes. La jornada termina después del cierre.

## Ejemplo 2: atención y cierre

Jornada de 2 horas:

| Llegada | Código | Prioridad | Minutos |
| --- | --- | --- | --- |
| 1 | T1 | B | 10 |
| 2 | T2 | A | 20 |
| 3 | T3 | M | 15 |
| 4 | T4 | A | 50 |
| 5 | T5 | B | 15 |
| 6 | T6 | A | 10 |

La atención habitual resuelve T2 y T4; quedan 50 minutos. El cierre selecciona los cuatro restantes.

Salida: **T2, T4, T6, T3, T1, T5**.

## Para avanzar

- Pruebas vacío, tiempo cero, menos de cinco candidatos y ninguno que quepa.
- No examinas tickets fuera de la ventana para elegir el próximo.
- Una prioridad sin candidato hace avanzar el turno.
- El cierre usa su ventana fija y termina después de atender su selección.
- Justificas los empates y el orden final.
- Puedes explicar el tiempo y la memoria de tu implementación.

[Continuar al módulo 9](../09_Complejidad_y_POO/README.md)
