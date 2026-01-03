<!--
::METADATA::
type: solution
topic_id: mcu-01-arquitectura
file_id: respuestas-arquitectura-mcu
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [respuestas, soluciones, microcontrolador, arquitectura]
search_keywords: "respuestas, soluciones, arquitectura MCU"
-->

> 🏠 **Navegación:** [← Problemas](../problems/MCU-01-Problemas.md)

---

# Respuestas: Arquitectura de Microcontroladores

## Nivel 1: Conceptos Básicos

### Respuesta 1.1

**Diferencia principal:**

| Microcontrolador | Microprocesador |
|------------------|-----------------|
| Sistema completo en un chip | Solo la CPU |
| Memoria integrada (Flash, RAM) | Requiere memoria externa |
| Periféricos integrados | Requiere chips adicionales |
| Diseñado para control embebido | Diseñado para computación general |

### Respuesta 1.2

Periféricos comunes:
1. **GPIO** - Entrada/Salida digital
2. **Timer/Counter** - Temporización y conteo
3. **UART** - Comunicación serial asíncrona
4. **ADC** - Convertidor analógico-digital
5. **PWM** - Modulación por ancho de pulso
6. **I2C/SPI** - Buses de comunicación
7. **Watchdog Timer** - Recuperación de errores

### Respuesta 1.3

**Arquitectura Harvard:**
- Buses separados para instrucciones y datos
- Memorias separadas para programa y datos

**Ventaja:** Puede acceder a instrucciones y datos simultáneamente, aumentando el rendimiento (no hay "cuello de botella de Von Neumann").

---

## Nivel 2: Componentes de la CPU

### Respuesta 2.1

Funciones de la ALU:
- **Operaciones aritméticas:** suma, resta, multiplicación, división
- **Operaciones lógicas:** AND, OR, XOR, NOT
- **Operaciones de desplazamiento:** shift left, shift right, rotate
- **Comparaciones:** genera flags basados en resultados

### Respuesta 2.2

| Flag | Nombre | Significado |
|------|--------|-------------|
| Z | Zero | Resultado es cero |
| C | Carry | Hubo acarreo/préstamo |
| N | Negative | Resultado es negativo (bit MSB = 1) |
| V | Overflow | Desbordamiento en operación con signo |

### Respuesta 2.3

El **Contador de Programa (PC)** almacena la dirección de la siguiente instrucción a ejecutar. Se incrementa automáticamente después de cada fetch, y se modifica por instrucciones de salto/llamada.

---

## Nivel 3: Sistema de Memoria

### Respuesta 3.1

| Memoria | Tamaño | Uso |
|---------|--------|-----|
| Flash | 32 KB | Almacenar el programa (código) |
| SRAM | 2 KB | Variables durante ejecución |
| EEPROM | 1 KB | Datos persistentes (configuración, calibración) |

### Respuesta 3.2

Con bus de direcciones de 16 bits:
```
Espacio direccionable = 2^16 = 65,536 bytes = 64 KB
```

### Respuesta 3.3

- **RAM (volátil):** Usa condensadores/transistores que pierden carga sin alimentación. Ventaja: rápida lectura/escritura.

- **Flash (no volátil):** Usa celdas de puerta flotante que retienen electrones. Ventaja: conserva datos sin alimentación.

**Impacto en diseño:** El programa se almacena en Flash (sobrevive apagados), mientras las variables temporales van en RAM.

---

## Nivel 4: Sistema de Reloj

### Respuesta 4.1

| Fuente | Cuándo usar |
|--------|-------------|
| RC interno (±10%) | Proyectos simples sin comunicación crítica, bajo costo |
| Cristal (±20 ppm) | UART, USB, medición precisa de tiempo, RTC |

### Respuesta 4.2

```
Período = 1 / Frecuencia
T = 1 / 16,000,000 Hz = 62.5 ns

Una instrucción de 1 ciclo toma 62.5 nanosegundos.
```

### Respuesta 4.3

```
Frecuencia base: 20 MHz

Prescaler /1: 20 MHz
Prescaler /2: 10 MHz
Prescaler /4: 5 MHz
Prescaler /8: 2.5 MHz
```

---

## Nivel 5: Selección de MCU

### Respuesta 5.1

**Recomendación: ATmega328P** (familia AVR)

Razones:
- 23 GPIO (sobra para 10 entradas)
- 6 canales PWM (sobra para 4)
- 6 entradas ADC (sobra para 2)
- 1 UART
- Bajo costo (~$2-3)
- Amplio ecosistema (Arduino)

### Respuesta 5.2

| Característica | PIC16F | ATmega328 | STM32F103 |
|----------------|--------|-----------|-----------|
| Arquitectura | Harvard | Harvard | Harvard modificada |
| Ancho datos | 8 bits | 8 bits | 32 bits |
| Ecosistema | MPLAB X | Arduino/avr-gcc | STM32CubeIDE |
| Complejidad | Baja | Baja | Media-Alta |

### Respuesta 5.3

**Elegir 8 bits cuando:**
- Aplicaciones simples
- Bajo costo es crítico
- Bajo consumo
- I/O básico

**Elegir 32 bits cuando:**
- Procesamiento matemático intensivo
- Interfaz gráfica
- Múltiples periféricos complejos
- Sistemas operativos embebidos

---

## Nivel 6: Cálculos de Recursos

### Respuesta 6.1

**Flash:**
```
Código: 12 KB
Disponible: 16 KB
Uso: 12/16 = 75% ✓ (OK, < 80%)
```

**RAM:**
```
Variables: 500 bytes
Stack: 200 bytes
Buffers: 256 bytes
Total: 956 bytes

Disponible: 1 KB = 1024 bytes
Uso: 956/1024 = 93% ✗ (PELIGRO, > 80%)
```

**Conclusión:** Flash OK, RAM insuficiente. Necesita MCU con más RAM.

### Respuesta 6.2

```
Muestreo: 10 kHz = 100 µs entre muestras
Tiempo por conversión: 13 ciclos ADC

El ADC necesita: 13 ciclos × 10,000 conversiones/s = 130,000 ciclos/s mínimo

Recomendación: F_CPU ≥ 50 × F_sample = 50 × 10,000 = 500 kHz mínimo

En la práctica, usar al menos 1-2 MHz para dejar margen para procesamiento.
```

### Respuesta 6.3

```
Consumo activo: 25 mA × 10% = 2.5 mA promedio
Consumo sleep: 50 µA × 90% = 45 µA = 0.045 mA promedio
Consumo total promedio: 2.545 mA

Tiempo: 30 días × 24 horas = 720 horas

Capacidad = Consumo × Tiempo
Capacidad = 2.545 mA × 720 h = 1,832 mAh

Con margen de seguridad (20%): ~2,200 mAh
```

---

## Nivel 7: Mapa de Memoria

### Respuesta 7.1

Colocar en los **primeros 32 registros** (0x0000-0x001F) si está disponible, o en SRAM baja (0x0060+).

Los registros de CPU tienen acceso más rápido (1 ciclo) que la SRAM (2 ciclos en AVR).

### Respuesta 7.2

```
Direccionamiento I/O de 8 bits:
Dispositivos = 2^8 = 256 dispositivos de I/O
```

### Respuesta 7.3

Los vectores de interrupción están al inicio porque:
1. El reset salta a dirección 0x0000
2. Las interrupciones usan direcciones fijas bajas
3. Permite que el código arranque inmediatamente
4. Facilita el bootloader (si existe)

---

## Nivel 8: Consumo de Energía

### Respuesta 8.1

```
Consumo activo: 5 mA × 1% = 0.05 mA
Consumo idle: 1 mA × 99% = 0.99 mA
Consumo promedio: 1.04 mA

(Nota: Power-down no se usa en este escenario)
```

### Respuesta 8.2

Estrategias para reducir consumo con UART:
1. Reducir frecuencia de CPU al mínimo para 9600 baud (~150 kHz)
2. Entrar en modo idle entre recepciones
3. Usar interrupción de recepción para despertar
4. Apagar UART TX cuando no transmite
5. Usar modo de bajo consumo del transceiver (si hay)

### Respuesta 8.3

```
Estrategia:
1. MCU en Power-down
2. Timer (WDT o RTC externo) genera interrupción cada 10 s
3. MCU despierta
4. Lee sensor, procesa, transmite
5. Vuelve a Power-down

Timeline:
[Sleep 10s]->[Active 50ms]->[Sleep 10s]->[Active 50ms]...

Duty cycle activo: 50ms / 10s = 0.5%
```

---

## Nivel 9: Diseño de Sistema

### Respuesta 9.1

**ATmega328P - Asignación de pines:**

| Pin | Puerto | Función |
|-----|--------|---------|
| 2 | PD0 | UART RX |
| 3 | PD1 | UART TX |
| 4 | PD2 | Botón 1 (INT0) |
| 5 | PD3 | Botón 2 (INT1) |
| 14-17 | PB0-PB3 | LED 1-4 |
| 23 | PC0 | Entrada analógica (ADC0) |
| 27 | PC4 | I2C SDA |
| 28 | PC5 | I2C SCL |

### Respuesta 9.2

```
┌─────────────────────────────────────────────────┐
│                  Sistema de                     │
│              Control de Temperatura             │
├─────────────────────────────────────────────────┤
│                                                 │
│  ┌─────────┐      ┌─────────────┐      ┌─────┐│
│  │ Sensor  │─ADC─▶│             │─GPIO▶│Relé ││
│  │ (NTC)   │      │     MCU     │      │     ││
│  └─────────┘      │             │      └──┬──┘│
│                   │  ATmega328  │         │   │
│  ┌─────────┐      │             │      ┌──▼──┐│
│  │ Display │◀─GPIO│             │      │Calef││
│  │ 7-seg   │      │             │      │actor││
│  └─────────┘      │             │      └─────┘│
│                   │             │             │
│                   │             │─UART─▶ PC   │
│                   └─────────────┘             │
└─────────────────────────────────────────────────┘
```

### Respuesta 9.3

**Circuito mínimo:**

```
                 VCC (5V)
                  │
          ┌──────┴──────┐
          │             │
    ┌─────┼─────────────┼─────┐
    │     │    MCU      │     │
    │  VCC┤             ├AVCC │
    │     │             │     │
    │  GND┤             ├AREF─┼─ VCC (o ref)
    │     │             │     │
    │RESET┤     ┌───────┤     │
    │     │     │       │     │
    └──┬──┴─────┴───────┴──┬──┘
       │                   │
      10k                 GND
       │
      VCC

Componentes mínimos:
1. Capacitor 100nF entre VCC-GND (bypass)
2. Capacitor 100nF entre AVCC-GND
3. Resistor 10k pullup en RESET
4. (Opcional) Cristal + 2 capacitores de 22pF
```

---

## Nivel 10: Integración

### Respuesta 10.1

**MCU seleccionado: STM32F103C8T6**

**Justificación:**
- 8 ADC + 4 PWM + I2C + UART = cubierto
- 32 bits para cálculos eficientes
- 20 KB RAM, 64 KB Flash
- Opera a 3.3V (compatible con batería LiPo 3.7V con regulador)

**a) Memoria estimada:**
- Código: ~15-20 KB
- RAM: 8 × buffer ADC + buffers UART + variables = ~2 KB
- Conclusión: 64 KB Flash y 20 KB RAM es suficiente ✓

**b) Consumo:**
- Activo @ 72 MHz: ~30 mA
- Reduciendo a 8 MHz: ~8 mA
- Con sleep entre lecturas (100ms activo, 900ms sleep):
  - Promedio: 8 mA × 10% + 0.1 mA × 90% = 0.89 mA

**c) Asignación de pines:** (ver datasheet para pines específicos)

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas para ejercicios de arquitectura MCU
NOTA: Pueden existir soluciones alternativas válidas
-->
