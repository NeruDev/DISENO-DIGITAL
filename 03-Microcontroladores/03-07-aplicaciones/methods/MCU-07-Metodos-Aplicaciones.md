<!--
::METADATA::
type: method
topic_id: mcu-07-aplicaciones
file_id: metodos-aplicaciones
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [microcontrolador, método, proyecto]
search_keywords: "metodos integracion proyectos MCU"
-->

> 🏠 **Navegación:** [← Teoría](../theory/MCU-07-Teoria-Aplicaciones.md) | [Problemas →](../problems/MCU-07-Problemas.md)

---

# Métodos: Aplicaciones Integradas

## Método 1: Traer-up Básico

```c
void bringup(void) {
    clock_init();          // si aplica
    gpio_init();           // LEDs, botones
    uart_init();           // debug
    timer_init_ms();       // tick de 1 ms
    sei();
}
```

## Método 2: Scheduler Cooperativo

```c
typedef void (*task_fn)(void);

typedef struct {
    task_fn fn;
    uint16_t period_ms;
    uint16_t next;
} task_t;

task_t tasks[] = {
    {task_sense, 50, 0},
    {task_control, 50, 0},
    {task_comm, 100, 0},
};

volatile uint32_t tick_ms = 0;

ISR(TIMER0_COMPA_vect) { tick_ms++; }

void scheduler_run(void) {
    while (1) {
        uint32_t now = tick_ms;
        for (uint8_t i = 0; i < sizeof(tasks)/sizeof(task_t); i++) {
            if (now >= tasks[i].next) {
                tasks[i].fn();
                tasks[i].next = now + tasks[i].period_ms;
            }
        }
    }
}
```

## Método 3: Pipeline Sensor → Filtro → Acción

```c
typedef struct {
    uint16_t raw;
    uint16_t filt;
    uint8_t ready;
} sensor_t;

sensor_t temp;

void task_sense(void) {
    temp.raw = adc_read(0);
    temp.filt = filter_add(&filt_temp, temp.raw);
    temp.ready = 1;
}

void task_control(void) {
    if (!temp.ready) return;
    temp.ready = 0;
    uint16_t mv = temp.filt * 5000UL / 1024;
    control_loop(mv);
}
```

## Método 4: Máquina de Estados Simple

```c
typedef enum { ST_INIT, ST_IDLE, ST_RUN, ST_ERROR } state_t;
state_t st = ST_INIT;

void loop_state(void) {
    switch (st) {
        case ST_INIT:
            hw_init();
            st = ST_IDLE;
            break;
        case ST_IDLE:
            if (cmd_start) st = ST_RUN;
            break;
        case ST_RUN:
            if (fault) st = ST_ERROR;
            run_cycle();
            break;
        case ST_ERROR:
            safe_stop();
            if (reset_cmd) st = ST_INIT;
            break;
    }
}
```

## Método 5: Watchdog Seguro

```c
void wdt_setup(void) {
    wdt_enable(WDTO_1S);
}

void pet_wdt(void) {
    wdt_reset();
}

// Llamar pet_wdt en tareas críticas o dentro de tick si todo OK
```

## Método 6: Anti-Bloqueo I2C

```c
uint8_t i2c_transfer_safe(...) {
    uint16_t timeout = 1000; // us
    while (!(TWCR & (1<<TWINT)) && timeout--) _delay_us(1);
    if (!timeout) {
        // intentar liberar bus
        for (uint8_t i=0; i<9; i++) { SCL_toggle(); }
        return 0;
    }
    return 1;
}
```

## Método 7: Logger Compacto

```c
void log_u16(const char *tag, uint16_t v) {
    uart_puts(tag);
    uart_putc(':');
    uart_print_uint(v);
    uart_puts("\r\n");
}
```

## Método 8: Perfil de Tiempo

```c
uint16_t t0 = TCNT1;
run_critical();
uint16_t dt = TCNT1 - t0; // ciclos CPU
```

## Método 9: Plantilla de ISR Limpia

```c
ISR(INT0_vect) {
    // Evitar lógica pesada
    flag_int0 = 1;
}
```

## Método 10: Checklist de Integración

- [ ] UART debug funciona
- [ ] ADC calibrado / filtrado
- [ ] PWM estable sin jitter perceptible
- [ ] I2C/SPI sin NACK/errores
- [ ] Watchdog habilitado
- [ ] Tests de estrés (temperatura, ruido, alimentación)

---

<!-- IA_CONTEXT
USO: Guía rápida para integrar subsistemas
-->
