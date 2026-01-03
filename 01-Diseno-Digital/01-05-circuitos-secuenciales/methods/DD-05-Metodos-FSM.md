<!--
::METADATA::
type: method
topic_id: dd-05-circuitos-secuenciales
file_id: metodos-fsm
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [FSM, diseno, sintesis, analisis, maquina-estados]
search_keywords: "máquina de estados, FSM, diseño secuencial, síntesis"
-->

> 🏠 **Navegación:** [← Teoría](../theory/DD-05-Teoria-CircuitosSecuenciales.md) | [Problemas →](../problems/DD-05-Problemas.md)

---

# Métodos de Diseño de Máquinas de Estados Finitos

## Método 1: Diseño Sistemático de FSM

### Algoritmo Completo

**Pasos:**
1. **Especificación:** Entender el problema completamente
2. **Diagrama de estados:** Dibujar todos los estados y transiciones
3. **Tabla de estados:** Convertir diagrama a formato tabular
4. **Minimización:** Eliminar estados redundantes (opcional)
5. **Asignación de estados:** Codificar estados en binario
6. **Tabla de transición:** Incluir códigos binarios
7. **Ecuaciones de excitación:** Obtener entradas a flip-flops
8. **Ecuaciones de salida:** Determinar lógica de salida
9. **Implementación:** Dibujar circuito completo
10. **Verificación:** Simular y verificar

---

## Método 2: De Especificación a Diagrama de Estados

### Ejemplo: Detector de Secuencia "101"

**Especificación:** Detectar la secuencia 101 en una entrada serial X. Salida Z=1 cuando se detecta.

**Paso 1:** Identificar estados necesarios
- S0: Estado inicial / ningún bit correcto
- S1: Recibido "1"
- S2: Recibido "10"
- S3: Recibido "101" → Z=1

**Paso 2:** Dibujar diagrama (Moore)

```
         X=0           X=0
    ┌──────────┐  ┌──────────┐
    │          │  │          │
    ▼    X=1   │  ▼    X=1   │
┌──────┐    ┌──────┐    ┌──────┐
│  S0  │───>│  S1  │───>│  S2  │
│ Z=0  │    │ Z=0  │<───│ Z=0  │
└──────┘    └──────┘    └──────┘
    ↑           │           │
    │           │ X=1       │ X=1
    │           ▼           │
    │       ┌──────┐        │
    └───────│  S3  │<───────┘
     X=0    │ Z=1  │
            └──────┘
```

---

## Método 3: Tabla de Estados a Tabla de Transición

### Ejemplo Continuado

**Tabla de Estados:**

| Estado Actual | X=0 | X=1 | Salida Z |
|---------------|-----|-----|----------|
| S0 | S0 | S1 | 0 |
| S1 | S2 | S1 | 0 |
| S2 | S0 | S3 | 0 |
| S3 | S0 | S1 | 1 |

**Asignación de Estados:**

| Estado | Q1 | Q0 |
|--------|----|----|
| S0 | 0 | 0 |
| S1 | 0 | 1 |
| S2 | 1 | 0 |
| S3 | 1 | 1 |

**Tabla de Transición:**

| Q1 | Q0 | X | Q1+ | Q0+ | Z |
|----|----|---|-----|-----|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 | 1 | 1 |

---

## Método 4: Obtener Ecuaciones con Flip-Flop D

### Algoritmo

Para flip-flop D: **D = Q+** (el valor deseado del siguiente estado)

### Mapas de Karnaugh

**Para D1 (entrada de Q1):**
```
         Q0X
        00  01  11  10
      ┌────┬────┬────┬────┐
Q1=0  │ 0  │ 0  │ 0  │ 1  │
      ├────┼────┼────┼────┤
Q1=1  │ 0  │ 1  │ 0  │ 0  │
      └────┴────┴────┴────┘
```
$$D_1 = \overline{Q_1}Q_0\overline{X} + Q_1\overline{Q_0}X$$

**Para D0 (entrada de Q0):**
```
         Q0X
        00  01  11  10
      ┌────┬────┬────┬────┐
Q1=0  │ 0  │ 1  │ 1  │ 0  │
      ├────┼────┼────┼────┤
Q1=1  │ 0  │ 1  │ 1  │ 0  │
      └────┴────┴────┴────┘
```
$$D_0 = X$$

**Para Z (salida):**
$$Z = Q_1Q_0$$

---

## Método 5: Obtener Ecuaciones con Flip-Flop JK

### Tabla de Excitación JK

| Q | Q+ | J | K |
|---|-----|---|---|
| 0 | 0 | 0 | X |
| 0 | 1 | 1 | X |
| 1 | 0 | X | 1 |
| 1 | 1 | X | 0 |

### Proceso

1. Agregar columnas J y K para cada flip-flop
2. Llenar según la tabla de excitación
3. Crear mapas K con don't cares
4. Simplificar

### Ejemplo

| Q1 | Q0 | X | Q1+ | Q0+ | J1 | K1 | J0 | K0 |
|----|----|----|-----|-----|----|----|----|----|
| 0 | 0 | 0 | 0 | 0 | 0 | X | 0 | X |
| 0 | 0 | 1 | 0 | 1 | 0 | X | 1 | X |
| 0 | 1 | 0 | 1 | 0 | 1 | X | X | 1 |
| 0 | 1 | 1 | 0 | 1 | 0 | X | X | 0 |
| 1 | 0 | 0 | 0 | 0 | X | 1 | 0 | X |
| 1 | 0 | 1 | 1 | 1 | X | 0 | 1 | X |
| 1 | 1 | 0 | 0 | 0 | X | 1 | X | 1 |
| 1 | 1 | 1 | 0 | 1 | X | 1 | X | 0 |

---

## Método 6: Minimización de Estados

### Algoritmo de Partición

**Pasos:**
1. Crear partición inicial: estados con misma salida
2. Refinar: separar estados con diferentes transiciones
3. Repetir hasta que no haya cambios
4. Estados en misma partición final son equivalentes

### Ejemplo

Estados con salida 0: {S0, S1, S2}
Estados con salida 1: {S3}

Verificar transiciones... (continuar proceso)

---

## Método 7: Diseño Moore vs Mealy

### Conversión Moore → Mealy

1. La salida asociada al estado destino se asocia a la transición
2. Generalmente reduce el número de estados

### Conversión Mealy → Moore

1. Crear un estado para cada combinación (estado, salida) única
2. Generalmente aumenta el número de estados

### Cuándo Usar Cada Una

| Moore | Mealy |
|-------|-------|
| Salidas síncronas con CLK | Respuesta más rápida |
| Más fácil de depurar | Menos estados |
| Salidas más estables | Puede tener glitches |

---

## Método 8: Diseño con One-Hot Encoding

### Concepto

Un flip-flop por estado. Solo uno activo a la vez.

### Ventajas

- Lógica de siguiente estado simple
- Fácil de implementar y depurar
- Rápido (pocas compuertas por transición)

### Desventajas

- Más flip-flops necesarios
- Detección de estados inválidos más compleja

### Ejemplo (4 estados)

| Estado | Q3 | Q2 | Q1 | Q0 |
|--------|----|----|----|----|
| S0 | 0 | 0 | 0 | 1 |
| S1 | 0 | 0 | 1 | 0 |
| S2 | 0 | 1 | 0 | 0 |
| S3 | 1 | 0 | 0 | 0 |

---

## Método 9: Análisis de Circuitos Secuenciales

### Algoritmo

**Pasos:**
1. Identificar flip-flops y tipo
2. Obtener ecuaciones de entrada a FF (excitación)
3. Aplicar ecuación característica → ecuaciones de estado siguiente
4. Obtener ecuaciones de salida
5. Construir tabla de estados
6. Dibujar diagrama de estados

### Ecuaciones Características

| FF | Ecuación |
|----|----------|
| D | Q+ = D |
| JK | Q+ = JQ̄ + K̄Q |
| T | Q+ = T ⊕ Q |
| SR | Q+ = S + R̄Q |

---

## Método 10: Verificación de Diseños

### Lista de Verificación

1. ☐ Todos los estados son alcanzables
2. ☐ No hay estados trampa (sin salida)
3. ☐ Estado inicial definido (reset)
4. ☐ Tiempos de setup/hold respetados
5. ☐ Frecuencia máxima calculada
6. ☐ Estados no usados manejados
7. ☐ Simulación completa

### Manejo de Estados No Usados

Con n flip-flops hay $2^n$ estados posibles.

**Opciones:**
1. Ignorar (diseño puede quedar atrapado)
2. Forzar transición a estado válido
3. Usar como don't care para simplificar

---

## Resumen de Fórmulas

### Número de Flip-Flops

$$n = \lceil \log_2(\text{número de estados}) \rceil$$

### Frecuencia Máxima

$$f_{max} = \frac{1}{t_{CQ} + t_{comb} + t_{setup}}$$

### Estados con One-Hot

$$n_{FF} = \text{número de estados}$$

---

<!-- IA_CONTEXT
USO: Referencia para diseño y análisis de FSM
NIVEL: Intermedio (2/3)
HERRAMIENTAS: LogiSim, Digital, ModelSim, Quartus
-->
