<!--
::METADATA::
type: detailed_solution
topic_id: mcu-07-aplicaciones
problem_id: 3.1
file_id: solucion-problema-3-1
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 3
tags: [solucion, MCU, scheduler, tareas, diseño]
-->

> 🏠 **Navegación:** [← Índice](./README.md) | [Problema 3.2 →](./MCU-07-Sol-Problema-3.2.md)

---

# Solución Detallada: Problema 3.1

## Enunciado
Diseña tareas y períodos para: sensado (50ms), control (50ms), comunicación (200ms).

---

## Paso 1: Análisis de Requisitos

| Tarea | Período | Prioridad | Duración estimada |
|-------|:-------:|:---------:|:-----------------:|
| Sensado | 50 ms | Alta | ~2 ms |
| Control | 50 ms | Alta | ~1 ms |
| Comunicación | 200 ms | Media | ~10 ms |

### Cálculo de Utilización

$$U = \sum \frac{C_i}{T_i} = \frac{2}{50} + \frac{1}{50} + \frac{10}{200} = 0.04 + 0.02 + 0.05 = 0.11 = 11\%$$

✅ Utilización < 70%, sistema factible.

---

## Paso 2: Diseño del Scheduler

### Base de Tiempo: 10 ms (tick)

Elegimos 10 ms como tick base porque es el **MCD** conveniente:
- 50 ms = 5 ticks
- 200 ms = 20 ticks

### Diagrama Temporal

```
Tiempo (ms):  0    10   20   30   40   50   60   70   80   90  100 ...
              │    │    │    │    │    │    │    │    │    │    │
Tick:         0    1    2    3    4    5    6    7    8    9   10  ...
              │                        │                        │
Sensado:      ■                        ■                        ■
              │                        │                        │
Control:      ■                        ■                        ■
              │                        │                        │
Comunicación: ■                                                 ■

■ = Tarea ejecutada
```

---

## Paso 3: Implementación

### Definición de Tareas

```c
#include <avr/io.h>
#include <avr/interrupt.h>

// Períodos en ticks (1 tick = 10ms)
#define PERIOD_SENSING   5    // 50ms
#define PERIOD_CONTROL   5    // 50ms  
#define PERIOD_COMMS    20    // 200ms

// Contadores de tick
volatile uint8_t tick_sensing = 0;
volatile uint8_t tick_control = 0;
volatile uint8_t tick_comms = 0;

// Flags de ejecución
volatile uint8_t flag_sensing = 0;
volatile uint8_t flag_control = 0;
volatile uint8_t flag_comms = 0;

// Tick del sistema (cada 10ms)
volatile uint32_t system_tick = 0;
```

### ISR del Timer (Base de Tiempo)

```c
// Timer1 configurado para 10ms @ 16MHz
ISR(TIMER1_COMPA_vect) {
    system_tick++;
    
    // Scheduler: incrementar contadores
    if (++tick_sensing >= PERIOD_SENSING) {
        tick_sensing = 0;
        flag_sensing = 1;
    }
    
    if (++tick_control >= PERIOD_CONTROL) {
        tick_control = 0;
        flag_control = 1;
    }
    
    if (++tick_comms >= PERIOD_COMMS) {
        tick_comms = 0;
        flag_comms = 1;
    }
}
```

### Loop Principal

```c
int main(void) {
    // Inicialización
    timer_init();       // Timer cada 10ms
    adc_init();         // Para sensado
    uart_init();        // Para comunicación
    control_init();     // Variables de control
    
    sei();  // Habilitar interrupciones
    
    while (1) {
        // Despacho de tareas por prioridad
        
        // 1. Sensado (alta prioridad)
        if (flag_sensing) {
            flag_sensing = 0;
            task_sensing();
        }
        
        // 2. Control (alta prioridad)
        if (flag_control) {
            flag_control = 0;
            task_control();
        }
        
        // 3. Comunicación (media prioridad)
        if (flag_comms) {
            flag_comms = 0;
            task_communication();
        }
        
        // 4. Tareas de fondo (baja prioridad)
        task_background();
    }
}
```

### Implementación de Tareas

```c
// Variables compartidas
volatile int16_t temperature = 0;
volatile int16_t setpoint = 250;  // 25.0°C
volatile uint8_t pwm_output = 0;

//------------------------------------------------------------------------------
// Tarea de Sensado (cada 50ms)
//------------------------------------------------------------------------------
void task_sensing(void) {
    // Leer ADC (sensor de temperatura)
    uint16_t adc_raw = adc_read(0);
    
    // Convertir a temperatura (escalado x10 para decimales)
    // LM35: 10mV/°C, ADC 10-bit, Vref=5V
    // temp = adc * 5000 / 1024 / 10 = adc * 500 / 1024
    temperature = (int16_t)((uint32_t)adc_raw * 500 / 1024);
}

//------------------------------------------------------------------------------
// Tarea de Control (cada 50ms)
//------------------------------------------------------------------------------
void task_control(void) {
    // Control proporcional simple
    int16_t error = setpoint - temperature;
    
    // Ganancia Kp = 2
    int16_t output = error * 2;
    
    // Saturar a rango PWM (0-255)
    if (output < 0) output = 0;
    if (output > 255) output = 255;
    
    pwm_output = (uint8_t)output;
    
    // Aplicar salida PWM
    OCR0A = pwm_output;
}

//------------------------------------------------------------------------------
// Tarea de Comunicación (cada 200ms)
//------------------------------------------------------------------------------
void task_communication(void) {
    // Formato: "T:XXX,S:XXX,P:XXX\r\n"
    char buffer[32];
    
    sprintf(buffer, "T:%d,S:%d,P:%d\r\n", 
            temperature, setpoint, pwm_output);
    
    uart_puts(buffer);
    
    // Procesar comandos recibidos
    if (uart_available()) {
        process_command();
    }
}

//------------------------------------------------------------------------------
// Tarea de Fondo (cuando hay tiempo libre)
//------------------------------------------------------------------------------
void task_background(void) {
    // Actualizar display (si existe)
    // Verificar botones
    // Diagnósticos
}
```

---

## Paso 4: Configuración del Timer

```c
void timer_init(void) {
    // Timer1 en modo CTC para 10ms @ 16MHz
    // OCR1A = (F_CPU / Prescaler / Freq) - 1
    // OCR1A = (16000000 / 64 / 100) - 1 = 2499
    
    TCCR1A = 0;
    TCCR1B = (1 << WGM12) | (1 << CS11) | (1 << CS10);  // CTC, /64
    OCR1A = 2499;
    TIMSK1 = (1 << OCIE1A);  // Habilitar interrupción
}
```

---

## Paso 5: Diagrama de Secuencia

```
    0ms     10ms    20ms    30ms    40ms    50ms    60ms   ...
     │       │       │       │       │       │       │
     ▼       ▼       ▼       ▼       ▼       ▼       ▼
    ┌─┐     ┌─┐     ┌─┐     ┌─┐     ┌─┐     ┌─┐     ┌─┐
ISR │T│     │T│     │T│     │T│     │T│     │T│     │T│
    └┬┘     └─┘     └─┘     └─┘     └─┘     └┬┘     └─┘
     │                                       │
     ▼                                       ▼
    ┌──┐                                    ┌──┐
Sen │S │                                    │S │
    └┬─┘                                    └┬─┘
     │                                       │
     ▼                                       ▼
    ┌─┐                                     ┌─┐
Ctl │C│                                     │C│
    └┬┘                                     └┬┘
     │                                       │
     ▼
    ┌────────┐
Com │ COMMS  │
    └────────┘

T = Tick ISR (~10µs)
S = Sensado (~2ms)
C = Control (~1ms)
COMMS = Comunicación (~10ms)
```

---

## Conceptos Clave

| Concepto | Descripción |
|----------|-------------|
| **Tick** | Unidad mínima de tiempo del scheduler |
| **Período** | Cada cuántos ticks se ejecuta una tarea |
| **Utilización** | % de CPU usada por tareas |
| **Prioridad** | Orden de despacho cuando hay conflicto |
| **Flag** | Señaliza que una tarea debe ejecutarse |

---

## Errores Comunes

| Error | Consecuencia | Solución |
|-------|--------------|----------|
| Tarea muy larga | Pierde ticks | Dividir en partes |
| No usar `volatile` | Variables no actualizan | Agregar `volatile` |
| ISR muy larga | Jitter, pérdida de eventos | Solo flags en ISR |
| Sin prioridades | Tareas críticas retrasadas | Ordenar despacho |

---

> 💡 **Tip:** Mide el tiempo real de cada tarea con un pin de debug y osciloscopio para verificar que no exceden sus períodos.
