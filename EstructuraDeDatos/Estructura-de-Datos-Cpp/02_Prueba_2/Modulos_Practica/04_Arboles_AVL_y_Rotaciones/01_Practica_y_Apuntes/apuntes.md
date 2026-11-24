# Apuntes y Práctica Guiada — Módulo 04 (Árboles AVL)

[Volver a Contenidos](../README.md) · [Código de práctica](Main.cpp) · [Ir a Enunciados](../02_Enunciados/README.md)

---

## Mis apuntes de clase

### 1. Fórmula de Factor de Balance (`FB`) y qué indica el signo
```text
FB(N) = ____________ - ____________
FB = +2 significa que pesa hacia: __________
FB = -2 significa que pesa hacia: __________
```

### 2. ¿Cómo distingo rápido en prueba entre LL, RR, LR y RL?
> *(Anota aquí la regla con los signos del nodo desbalanceado Z y de su hijo Y...)*

### 3. ¿Cuál es el orden obligatorio al recalcular alturas tras rotar?
> *(¿Por qué falla si actualizo la nueva raíz antes que el nodo que bajó?...)*

---

## Guía paso a paso (para programar en `Main.cpp`)

1. **Paso 1 — Nodo con altura:** define `struct NodoAVL` (`clave`, `izq`, `der`, `altura`) y dos funciones cortas: `int altura(NodoAVL* n)` y `int fb(NodoAVL* n)`.
2. **Paso 2 — Probar una rotación simple aislada:** en `main()`, arma a mano la cadena desbalanceada `30 -> 20 -> 10` (con `altura` correcta), llama a `rotarDerecha(raiz)` e imprime la nueva raíz, sus hijos y sus alturas (`20` debe quedar arriba con `altura = 2`, y `10` y `30` con `altura = 1`).
3. **Paso 3 — Probar rotación doble aislada:** arma a mano el zigzag `30 -> 10 -> 20`, aplica `rotarIzquierda(raiz->izq)` y luego `rotarDerecha(raiz)` para ver cómo sube `20`.
4. **Paso 4 — Conectar `insertar`:** una vez que dominas las rotaciones en árboles de 3 nodos, escribe `insertar(NodoAVL* n, int k)` llamando a `balancear(n)` al final del retorno recursivo.
