<!--
::METADATA::
type: problem
topic_id: dd-05-circuitos-secuenciales
file_id: problemas-circuitos-secuenciales
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [ejercicios, secuenciales, flip-flop, FSM]
search_keywords: "ejercicios, problemas, circuitos secuenciales, máquina de estados"
-->

> 🏠 **Navegación:** [← Métodos](../methods/DD-05-Metodos-FSM.md) | [Respuestas →](../solutions/DD-05-Respuestas.md)

---

# Problemas: Circuitos Secuenciales

## Nivel 1: Latches

### Problema 1.1
Para un latch SR con compuertas NOR:
- a) Completar la tabla de verdad
- b) Dibujar el diagrama de tiempos para: S=1→0, R=0→1→0
- c) ¿Por qué S=R=1 es estado prohibido?

### Problema 1.2
Diseñar un latch D usando un latch SR:
- a) Diagrama del circuito
- b) Tabla de verdad
- c) ¿Cuál es la ventaja sobre el SR?

### Problema 1.3
Para un latch SR con enable (compuertas NAND):
- a) Completar el circuito interno
- b) Tabla de operación
- c) ¿Qué pasa cuando E=0?

---

## Nivel 2: Flip-Flops

### Problema 2.1
Para un flip-flop D disparado por flanco positivo:
- a) Dibujar el diagrama de tiempos para CLK y D dados
- b) ¿Cuál es Q después de 5 flancos si Q inicial = 0?

```
CLK: _|‾|_|‾|_|‾|_|‾|_|‾|_
D:   ‾‾‾|___|‾‾‾‾‾|___|‾‾‾
```

### Problema 2.2
Para un flip-flop JK:
- a) Completar la tabla característica
- b) Si J=K=1, ¿qué hace el flip-flop?
- c) Diagrama de tiempos con J=1, K alternando

### Problema 2.3
Convertir:
- a) Flip-flop JK a flip-flop D
- b) Flip-flop D a flip-flop T
- c) Flip-flop JK a flip-flop T

### Problema 2.4
Para el 74LS74 (dual D flip-flop):
- a) ¿Qué hacen las entradas PRE y CLR?
- b) Dibujar diagrama de tiempos con reset asíncrono
- c) ¿Cuál es la prioridad: CLK o CLR?

---

## Nivel 3: Análisis de Circuitos

### Problema 3.1
Analizar el siguiente circuito con flip-flop D:

```
       ┌───────────────┐
       │               │
X ─────┼───[XOR]───────┼── D ─┬─[D FF]─┬── Q ── Y
       │     │         │      │   CLK  │
       │     └─────────┼──────┴────────┘
       │               │
       └───────────────┘
```

- a) Obtener la ecuación de D
- b) Tabla de transición
- c) ¿Qué función realiza?

### Problema 3.2
Analizar el circuito con dos flip-flops JK:

```
        ┌──────────────────────────────┐
        │                              │
X ──────┼────────────────[AND]── J1 ───┤
        │                  │           │
        │         Q0 ──────┘           │
        │                              │
1 ──────────────────────────── K1 ──── FF1 ── Q1
        │                              │
        │         Q̄1 ─────[AND]── J0 ──┤
        │                  │           │
X ──────┼──────────────────┘           │
        │                              │
1 ──────────────────────────── K0 ──── FF0 ── Q0
        │                              │
        └──────────────────────────────┘
                                  CLK ─┘
```

- a) Ecuaciones de excitación
- b) Tabla de estados
- c) Diagrama de estados
- d) ¿Qué función realiza?

### Problema 3.3
Dado el circuito:
- Flip-flop D con $D = X \oplus Q$
- Salida $Y = XQ$

Analizar completamente (tabla de estados, diagrama, función).

---

## Nivel 4: Diseño de FSM - Detectores de Secuencia

### Problema 4.1
Diseñar un detector de la secuencia "110" (sin solapamiento):
- a) Diagrama de estados (Moore)
- b) Tabla de estados
- c) Asignación de estados
- d) Ecuaciones con flip-flops D
- e) Circuito completo

### Problema 4.2
Diseñar un detector de la secuencia "1010" (con solapamiento permitido):
- a) Diagrama de estados (Mealy)
- b) Comparar con versión Moore
- c) Implementar con flip-flops JK

### Problema 4.3
Diseñar un detector que identifique si hay más 1s que 0s en los últimos 3 bits:
- a) Definir estados necesarios
- b) Diagrama de estados
- c) Implementación

---

## Nivel 5: Diseño de FSM - Controladores

### Problema 5.1: Máquina Expendedora Simplificada
Diseñar una FSM para una máquina que:
- Acepta monedas de 5 y 10 centavos
- Producto cuesta 15 centavos
- No da cambio
- Salidas: PRODUCTO, DEVOLVER

Estados: Esperando, 5¢, 10¢

### Problema 5.2: Controlador de Semáforo
Diseñar FSM para semáforo con:
- 4 estados: Verde(30s), Amarillo(5s), Rojo(30s), RojoAmarillo(5s)
- Entrada: Temporizador expirado
- Salidas: luces R, A, V

### Problema 5.3: Controlador de Motor
Un motor tiene estados: DETENIDO, ACELERANDO, VELOCIDAD_CONSTANTE, FRENANDO
- Entrada START inicia aceleración
- Entrada STOP inicia frenado
- Sensor VELOCIDAD_MAX indica velocidad alcanzada
- Sensor DETENIDO indica motor parado

---

## Nivel 6: Temporización

### Problema 6.1
Para un flip-flop con:
- $t_{setup} = 5ns$
- $t_{hold} = 2ns$
- $t_{CQ} = 8ns$

Y lógica combinacional con $t_{comb} = 15ns$:

- a) Calcular frecuencia máxima
- b) ¿Qué pasa si CLK es más rápido?
- c) ¿Cómo mejorar la frecuencia?

### Problema 6.2
Dibujar diagrama de tiempos detallado mostrando:
- Setup time
- Hold time
- Propagation delay
- Margen de tiempo

### Problema 6.3
Un sistema tiene 3 etapas de lógica combinacional en serie (10ns cada una) entre flip-flops.
- a) Frecuencia máxima actual
- b) Proponer pipelining y calcular nueva frecuencia

---

## Nivel 7: Implementación

### Problema 7.1
Implementar el detector de secuencia "101" usando:
- a) CI 74LS74 (D flip-flops)
- b) CI 74LS76 (JK flip-flops)
- c) Comparar número de compuertas

### Problema 7.2
Para la FSM del semáforo:
- a) Elegir codificación de estados
- b) Lista de componentes necesarios
- c) Diagrama de conexiones

### Problema 7.3
Diseñar el circuito de reset para:
- a) Reset al encender (power-on reset)
- b) Reset por botón (debounced)
- c) Reset combinado

---

## Nivel 8: Análisis Avanzado

### Problema 8.1
Dado un circuito secuencial con 3 flip-flops D y las ecuaciones:
- $D_0 = X \oplus Q_0$
- $D_1 = Q_0$
- $D_2 = Q_1$

- a) ¿Qué función realiza?
- b) ¿Cuántos estados tiene?
- c) Dibujar diagrama de estados para X=1 constante

### Problema 8.2
Un circuito tiene la tabla de estados:

| Q1Q0 | X=0 | X=1 | Z |
|------|-----|-----|---|
| 00 | 00 | 01 | 0 |
| 01 | 10 | 01 | 0 |
| 10 | 00 | 11 | 0 |
| 11 | 10 | 01 | 1 |

- a) Dibujar diagrama de estados
- b) ¿Es Moore o Mealy?
- c) ¿Qué secuencia detecta?

### Problema 8.3
Minimizar la FSM con estados {A, B, C, D, E} donde:
- A y C tienen la misma salida y mismas transiciones
- B y D tienen la misma salida pero diferentes transiciones
- E es único

---

## Nivel 9: Problemas Integradores

### Problema 9.1: Cerradura Digital
Diseñar una FSM para cerradura con secuencia 1-2-3:
- Entradas: botones 1, 2, 3
- Salida: ABRIR (cuando secuencia correcta)
- Volver al inicio si se presiona botón incorrecto

### Problema 9.2: Detector de Flancos
Diseñar un circuito que detecte:
- Flanco de subida → pulso en RISE
- Flanco de bajada → pulso en FALL

### Problema 9.3: Generador de Patrones
Diseñar una FSM que genere la secuencia repetitiva:
1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, ...

Un bit por ciclo de reloj.

---

## Nivel 10: Diseño Completo

### Problema 10.1
Diseñar un controlador de elevador para 3 pisos:
- Entradas: botones de piso (P1, P2, P3), sensores de piso
- Salidas: SUBIR, BAJAR, PUERTA
- Estados: en cada piso, subiendo, bajando

Incluir:
- Diagrama de estados completo
- Tabla de transición
- Ecuaciones
- Estimación de componentes

### Problema 10.2
Diseñar un árbitro de bus para 2 dispositivos:
- Entradas: REQ0, REQ1 (solicitudes)
- Salidas: GNT0, GNT1 (concesiones)
- Prioridad rotatoria (round-robin)

---

<!-- IA_CONTEXT
PROPÓSITO: Banco de ejercicios para circuitos secuenciales
RESPUESTAS: Ver archivo solutions/DD-05-Respuestas.md
HERRAMIENTAS: LogiSim, Digital, ModelSim
-->
