# Soluciones Detalladas: Máquinas de Estados (VHDL-06)

```
::METADATA::
tipo: indice-soluciones
tema: vhdl-06-maquinas-estados
actualizado: 2026-01-03
::END::
```

## Estructura de Niveles de Solución

| Nivel | Archivo | Contenido |
|-------|---------|-----------|
| 1️⃣ | [`VHDL-06-Respuestas.md`](../VHDL-06-Respuestas.md) | Solo respuestas finales |
| 2️⃣ | Esta carpeta `prob-01/` | Soluciones paso a paso |
| 3️⃣ | Secciones "Conceptos Clave" | Explicación profunda del método |

---

## Índice de Soluciones Detalladas

### Nivel 1: Conceptos FSM ⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 1.1 | Moore vs Mealy | [VHDL-06-Sol-Problema-1.1.md](VHDL-06-Sol-Problema-1.1.md) | ⭐⭐ |
| 1.2 | Diagrama de estados | [VHDL-06-Sol-Problema-1.2.md](VHDL-06-Sol-Problema-1.2.md) | ⭐⭐ |

### Nivel 2: FSM Moore ⭐⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 2.1 | Detector secuencia simple | [VHDL-06-Sol-Problema-2.1.md](VHDL-06-Sol-Problema-2.1.md) | ⭐⭐⭐ |
| 2.2 | Semáforo básico | [VHDL-06-Sol-Problema-2.2.md](VHDL-06-Sol-Problema-2.2.md) | ⭐⭐⭐ |
| 2.3 | Controlador simple | [VHDL-06-Sol-Problema-2.3.md](VHDL-06-Sol-Problema-2.3.md) | ⭐⭐⭐ |

### Nivel 3: FSM Mealy ⭐⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 3.1 | Detector con salida inmediata | [VHDL-06-Sol-Problema-3.1.md](VHDL-06-Sol-Problema-3.1.md) | ⭐⭐⭐ |
| 3.2 | Comparación Moore-Mealy | [VHDL-06-Sol-Problema-3.2.md](VHDL-06-Sol-Problema-3.2.md) | ⭐⭐⭐ |

### Nivel 4: Codificación de Estados ⭐⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 4.1 | One-hot encoding | [VHDL-06-Sol-Problema-4.1.md](VHDL-06-Sol-Problema-4.1.md) | ⭐⭐⭐ |
| 4.2 | Binary encoding | [VHDL-06-Sol-Problema-4.2.md](VHDL-06-Sol-Problema-4.2.md) | ⭐⭐⭐ |
| 4.3 | Gray encoding | [VHDL-06-Sol-Problema-4.3.md](VHDL-06-Sol-Problema-4.3.md) | ⭐⭐⭐ |

---

## Referencia FSM

### Comparación Moore vs Mealy

| Característica | Moore | Mealy |
|----------------|-------|-------|
| Salidas dependen de | Solo estado actual | Estado + entradas |
| Cambio de salida | Con cambio de estado | Inmediato con entrada |
| Número de estados | Generalmente más | Generalmente menos |
| Timing | Más predecible | Puede tener glitches |
| Complejidad | Más estados, lógica simple | Menos estados, más lógica |

### Plantilla FSM Moore (2 procesos)

```vhdl
architecture fsm of modulo is
    type state_type is (IDLE, STATE1, STATE2, STATE3);
    signal current_state, next_state : state_type;
begin
    -- Proceso 1: Registro de estado
    state_reg: process(clk, reset)
    begin
        if reset = '1' then
            current_state <= IDLE;
        elsif rising_edge(clk) then
            current_state <= next_state;
        end if;
    end process;
    
    -- Proceso 2: Lógica de siguiente estado + salidas
    fsm_logic: process(current_state, inputs)
    begin
        -- Valores por defecto
        next_state <= current_state;
        output <= '0';
        
        case current_state is
            when IDLE =>
                if start = '1' then
                    next_state <= STATE1;
                end if;
            when STATE1 =>
                output <= '1';
                next_state <= STATE2;
            when STATE2 =>
                next_state <= IDLE;
            when others =>
                next_state <= IDLE;
        end case;
    end process;
end architecture;
```

### Plantilla FSM Mealy (2 procesos)

```vhdl
-- Proceso de salidas (Mealy: depende de estado Y entradas)
output_logic: process(current_state, input)
begin
    output <= '0';  -- Default
    case current_state is
        when WAITING =>
            if input = '1' then
                output <= '1';  -- Salida depende de entrada
            end if;
        when others =>
            output <= '0';
    end case;
end process;
```

---

## Codificación de Estados

### Comparación

| Codificación | 4 estados | FFs | Ventaja |
|--------------|-----------|-----|---------|
| Binary | 00,01,10,11 | 2 | Menos FF |
| One-hot | 0001,0010,0100,1000 | 4 | Decodificación simple |
| Gray | 00,01,11,10 | 2 | 1 bit cambia por transición |

### Atributos de Codificación

```vhdl
type state_type is (S0, S1, S2, S3);
attribute syn_encoding : string;
attribute syn_encoding of state_type : type is "one-hot";
-- Opciones: "sequential", "gray", "one-hot", "safe"
```

---

## Detector de Secuencia "1011" (Ejemplo)

### Diagrama de Estados

```
        ┌─0─┐
        │   │
        ▼   │
      ┌─────┴─┐    1     ┌───────┐    0     ┌───────┐
  ───►│  S0   ├─────────►│  S1   ├─────────►│  S10  │
      │(idle) │          │(got 1)│          │(got 10)│
      └───────┘          └───┬───┘          └───┬───┘
          ▲                  │                  │
          │                  │0                 │1
          │                  ▼                  ▼
          │              ┌───────┐          ┌───────┐
          └──────────────┤  S0   │◄────0────┤ S101  │
                         └───────┘          │(got 101)
                              ▲             └───┬───┘
                              │                 │1
                              │             ┌───▼───┐
                              └─────────────┤ S1011 │ OUT=1
                                            │(MATCH)│
                                            └───────┘
```

---

## Navegación

| ⬅️ Respuestas | 🏠 Intro | ➡️ Problemas |
|:-------------:|:--------:|:------------:|
| [VHDL-06-Respuestas.md](../VHDL-06-Respuestas.md) | [VHDL-06-Intro.md](../../VHDL-06-Intro.md) | [VHDL-06-Problemas.md](../../problems/VHDL-06-Problemas.md) |
