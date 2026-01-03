<!--
::METADATA::
type: method
topic_id: dd-04-circuitos-combinacionales
file_id: metodos-diseno-combinacionales
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [diseno, metodologia, analisis, implementacion]
search_keywords: "diseño circuitos combinacionales, metodología, análisis"
-->

> 🏠 **Navegación:** [← Teoría](../theory/DD-04-Teoria-CircuitosCombinacionales.md) | [Problemas →](../problems/DD-04-Problemas.md)

---

# Métodos de Diseño de Circuitos Combinacionales

## Método 1: Diseño Sistemático con Compuertas

### Algoritmo General

**Pasos:**
1. Entender el problema y definir entradas/salidas
2. Construir la tabla de verdad
3. Obtener expresiones booleanas (minterms)
4. Simplificar usando Karnaugh o álgebra
5. Dibujar el circuito
6. Verificar el diseño

### Ejemplo: Detector de Números Primos (0-7)

**Paso 1:** Entradas: A, B, C (3 bits); Salida: P

**Paso 2:** Tabla de verdad
| A | B | C | Decimal | ¿Primo? | P |
|---|---|---|---------|---------|---|
| 0 | 0 | 0 | 0 | No | 0 |
| 0 | 0 | 1 | 1 | No* | 0 |
| 0 | 1 | 0 | 2 | Sí | 1 |
| 0 | 1 | 1 | 3 | Sí | 1 |
| 1 | 0 | 0 | 4 | No | 0 |
| 1 | 0 | 1 | 5 | Sí | 1 |
| 1 | 1 | 0 | 6 | No | 0 |
| 1 | 1 | 1 | 7 | Sí | 1 |

**Paso 3:** $P = \sum m(2, 3, 5, 7)$

**Paso 4:** Mapa K → $P = \overline{A}B + AC$

**Paso 5:** Circuito: 1 NOT, 2 AND, 1 OR

---

## Método 2: Implementación con Multiplexor

### Algoritmo

**Pasos:**
1. Identificar número de variables (n)
2. Seleccionar MUX $2^{n-1}$:1
3. Usar n-1 variables como selectores
4. Determinar entradas del MUX usando la variable restante

### Ejemplo: $F(A,B,C) = \sum m(1, 2, 4, 6, 7)$ con MUX 4:1

**Paso 1:** 3 variables → MUX 4:1

**Paso 2:** Selectores: A, B; Variable residual: C

**Paso 3:** Tabla de análisis
| A | B | Minterms Cubiertos | Entrada MUX |
|---|---|--------------------|-------------|
| 0 | 0 | $m_0$=0, $m_1$=1 | C |
| 0 | 1 | $m_2$=1, $m_3$=0 | $\overline{C}$ |
| 1 | 0 | $m_4$=1, $m_5$=0 | $\overline{C}$ |
| 1 | 1 | $m_6$=1, $m_7$=1 | 1 |

**Resultado:**
- $I_0 = C$
- $I_1 = \overline{C}$
- $I_2 = \overline{C}$
- $I_3 = 1$

---

## Método 3: Implementación con Decodificador

### Algoritmo

**Pasos:**
1. Obtener la función en minterms
2. Seleccionar decodificador de n entradas a $2^n$ salidas
3. Conectar las salidas correspondientes a los minterms con OR

### Ejemplo: $F(A,B,C) = \sum m(0, 2, 5, 7)$

**Implementación:**
```
        ┌──────────┐
A ──────┤A2        │
B ──────┤A1      Y0├────┐
C ──────┤A0      Y2├──┐ │
        │        Y5├─┐│ │
        │        Y7├┐││ │
        │  DEC3:8  │││││
        └──────────┘││││
                    │││└──[OR]── F
                    ││└───┘ │
                    │└──────┘
                    └───────┘
```

---

## Método 4: Diseño de Sumadores

### Half Adder

**Ecuaciones:**
$$S = A \oplus B$$
$$C = AB$$

### Full Adder

**Ecuaciones:**
$$S = A \oplus B \oplus C_{in}$$
$$C_{out} = AB + C_{in}(A \oplus B)$$

**Alternativa para $C_{out}$:**
$$C_{out} = AB + AC_{in} + BC_{in}$$

### Sumador de n bits (Ripple Carry)

Conectar n Full Adders donde $C_{out}$ de cada etapa es $C_{in}$ de la siguiente.

```
       ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐
A₀,B₀──┤ FA  ├──┤ FA  ├──┤ FA  ├──┤ FA  ├── C₄
       │  0  │  │  1  │  │  2  │  │  3  │
C₀=0───┤     │  │     │  │     │  │     │
       └──┬──┘  └──┬──┘  └──┬──┘  └──┬──┘
          S₀      S₁      S₂      S₃
```

---

## Método 5: Diseño de Restador

### Usando Complemento a 2

$$A - B = A + \overline{B} + 1$$

### Circuito Sumador/Restador

Usar XOR para inversión condicional:
- Modo = 0: Suma ($B$ pasa directo)
- Modo = 1: Resta ($B$ se invierte, $C_{in}$ = 1)

```
B ──[XOR]── FA ── S
      │
Modo ─┴──────────── C₀
```

---

## Método 6: Diseño de Comparadores

### Comparador de n bits (método iterativo)

**Para cada bit (de MSB a LSB):**
$$G_i = A_i\overline{B_i} + G_{i+1}(A_i \odot B_i)$$
$$L_i = \overline{A_i}B_i + L_{i+1}(A_i \odot B_i)$$
$$E_i = E_{i+1}(A_i \odot B_i)$$

Inicializar: $G_{MSB+1} = 0$, $L_{MSB+1} = 0$, $E_{MSB+1} = 1$

### Cascada de Comparadores

Para comparar números más grandes, usar entradas de cascada:
- Conectar $(G_{out}, E_{out}, L_{out})$ del MSB al $(G_{in}, E_{in}, L_{in})$ del LSB

---

## Método 7: Conversión de Códigos

### Gray a Binario

$$B_n = G_n$$
$$B_i = B_{i+1} \oplus G_i \quad \text{para } i < n$$

### Binario a Gray

$$G_n = B_n$$
$$G_i = B_{i+1} \oplus B_i \quad \text{para } i < n$$

### BCD a Excess-3

$$E_3 = BCD + 0011$$

Sumar 3 usando un sumador de 4 bits.

---

## Método 8: Análisis de Circuitos Existentes

### Algoritmo

**Pasos:**
1. Etiquetar todas las señales intermedias
2. Escribir la expresión de cada compuerta
3. Sustituir hasta obtener expresión final
4. Construir tabla de verdad si es necesario
5. Identificar la función

### Ejemplo

```
A ──────┬──[AND]─────────┐
        │                │
B ──[NOT]┴───────────────[OR]── Y
                         │
C ────────────[AND]──────┘
D ────────────┘
```

**Análisis:**
- Señal 1: $\overline{B}$
- Señal 2: $A \cdot \overline{B}$
- Señal 3: $CD$
- Salida: $Y = A\overline{B} + CD$

---

## Método 9: Detección y Eliminación de Hazards

### Identificar Hazard Estático-1

1. Obtener mapa K
2. Buscar 1s adyacentes NO cubiertos por el mismo grupo
3. Agregar término redundante

### Ejemplo

$F = \overline{A}C + AB$ tiene hazard cuando C=B=1 y A cambia.

**Solución:** Agregar $BC$ → $F = \overline{A}C + AB + BC$

---

## Método 10: Verificación de Diseños

### Lista de Verificación

1. ☐ Tabla de verdad completa
2. ☐ Expresión simplificada correcta
3. ☐ Circuito coincide con expresión
4. ☐ Fan-out respetado
5. ☐ Tiempos de propagación aceptables
6. ☐ Entradas no utilizadas conectadas apropiadamente

### Simulación

Usar herramientas como:
- LogiSim
- Digital
- Proteus
- ModelSim (para VHDL)

---

## Resumen de Selección de Método

| Situación | Método Recomendado |
|-----------|-------------------|
| Pocas variables (≤4) | Compuertas + Karnaugh |
| Funciones múltiples | Decodificador + OR |
| Datos enrutados | Multiplexor |
| Operaciones aritméticas | Sumadores en cascada |
| Comparación | Comparadores en cascada |
| Alta velocidad requerida | Carry Look-Ahead |

---

<!-- IA_CONTEXT
USO: Referencia para diseño de circuitos combinacionales
NIVEL: Intermedio (2/3)
HERRAMIENTAS: LogiSim, Digital, Quartus para síntesis
-->
