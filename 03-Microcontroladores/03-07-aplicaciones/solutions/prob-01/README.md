<!--
::METADATA::
type: solution_index
topic_id: mcu-07-aplicaciones
file_id: solucion-index-aplicaciones
status: complete
audience: student
last_updated: 2026-01-03
tags: [soluciones, MCU, aplicaciones, proyectos, índice]
-->

> 🏠 **Navegación:** [← Respuestas Rápidas](../MCU-07-Respuestas.md) | [Problemas →](../../problems/MCU-07-Problemas.md)

---

# Soluciones Detalladas: Aplicaciones (MCU-07)

## Estructura de Niveles de Solución

| Nivel | Ubicación | Contenido |
|:-----:|-----------|-----------|
| **1** | `MCU-07-Respuestas.md` | Respuestas directas |
| **2** | Esta carpeta (`prob-01/`) | Diseño completo |
| **3** | Secciones "Conceptos Clave" | Metodología |

---

## Índice de Soluciones Detalladas

### Nivel 1-2: Diseño y Energía ⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 1.1 | Bloques termostato | En respuestas |
| 1.2 | Periféricos para sensor | En respuestas |
| 2.1 | Técnicas bajo consumo | En respuestas |
| 2.2 | Modos sleep | En respuestas |

### Nivel 3-4: Scheduler y Comunicaciones ⭐⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 3.1 | Diseño de tareas | [MCU-07-Sol-Problema-3.1.md](./MCU-07-Sol-Problema-3.1.md) |
| 3.2 | Sobrecarga de tareas | En respuestas |
| 4.1 | Elección I2C vs SPI | En respuestas |
| 4.2 | Protocolo para pantalla | En respuestas |

### Nivel 5-6: Robustez y Calibración ⭐⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 5.1 | Watchdog | En respuestas |
| 5.2 | Timeouts I2C | En respuestas |
| 6.1 | Calibración 2 puntos | En respuestas |
| 6.2 | Promedio vs mediana | En respuestas |

### Nivel 7-10: Control y Proyecto Final ⭐⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 7.1 | Control proporcional | En respuestas |
| 8.1 | Formato log CSV | En respuestas |
| 9.1 | Integración multibús | En respuestas |
| 10.1 | Datalogger portátil | En respuestas |

---

## Referencia Rápida

### Metodología de Diseño Embebido

```
┌─────────────────────────────────────────────────────────────┐
│                    FLUJO DE DISEÑO                          │
│                                                              │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │Requisitos│───►│Selección │───►│ Diseño   │              │
│  │          │    │   MCU    │    │ Hardware │              │
│  └──────────┘    └──────────┘    └────┬─────┘              │
│                                       │                     │
│  ┌──────────┐    ┌──────────┐    ┌────▼─────┐              │
│  │Validación│◄───│ Pruebas  │◄───│ Diseño   │              │
│  │          │    │          │    │ Software │              │
│  └──────────┘    └──────────┘    └──────────┘              │
└─────────────────────────────────────────────────────────────┘
```

### Arquitectura Super-Loop

```c
int main(void) {
    // Inicialización
    system_init();
    
    while (1) {
        // Tareas periódicas
        if (flag_10ms) {
            flag_10ms = 0;
            task_read_sensors();
        }
        
        if (flag_50ms) {
            flag_50ms = 0;
            task_control();
        }
        
        if (flag_100ms) {
            flag_100ms = 0;
            task_update_display();
        }
        
        // Tareas por evento
        if (uart_data_available()) {
            task_process_command();
        }
    }
}
```

### Scheduler Cooperativo Simple

```c
typedef struct {
    void (*task)(void);     // Puntero a función
    uint16_t period_ms;     // Período de ejecución
    uint16_t elapsed_ms;    // Tiempo transcurrido
} Task_t;

Task_t tasks[] = {
    {task_sensors,   50,  0},
    {task_control,   50,  0},
    {task_display,  200,  0},
    {task_comms,    100,  0}
};
```

### Modos de Bajo Consumo (AVR)

| Modo | Despierta por | Consumo | Tiempo despertar |
|------|---------------|:-------:|:----------------:|
| Idle | Cualquier IRQ | ~1 mA | 6 ciclos |
| ADC Noise | ADC complete | ~0.5 mA | 6 ciclos |
| Power-save | Timer2, INT | ~1 µA | 6 ciclos |
| Power-down | INT, WDT | ~0.1 µA | 1000+ ciclos |

### Template de Proyecto

```
proyecto/
├── src/
│   ├── main.c           # Loop principal
│   ├── config.h         # Configuración
│   ├── hal/             # Hardware Abstraction Layer
│   │   ├── gpio.c
│   │   ├── timer.c
│   │   ├── uart.c
│   │   └── adc.c
│   ├── drivers/         # Drivers de dispositivos
│   │   ├── sensor_temp.c
│   │   └── display.c
│   └── app/             # Lógica de aplicación
│       ├── tasks.c
│       └── control.c
├── inc/                 # Headers
├── docs/                # Documentación
└── tests/               # Pruebas
```

### Checklist de Robustez

- [ ] Watchdog configurado
- [ ] Timeouts en comunicaciones
- [ ] Validación de entradas
- [ ] Manejo de errores
- [ ] Reset recovery
- [ ] Valores por defecto seguros
- [ ] Logging de errores

---

## Ejemplo: Diagrama de Bloques Termostato

```
┌─────────────────────────────────────────────────────────────┐
│                      TERMOSTATO                              │
│                                                              │
│  ┌──────────┐         ┌──────────┐         ┌──────────┐    │
│  │ Sensor   │   ADC   │   MCU    │   PWM   │Ventilador│    │
│  │  Temp    │────────►│ Control  │────────►│   Fan    │    │
│  │ (LM35)   │         │          │         │          │    │
│  └──────────┘         └────┬─────┘         └──────────┘    │
│                            │                               │
│  ┌──────────┐         ┌────▼─────┐                        │
│  │ Botones  │   GPIO  │ Display  │                        │
│  │ UP/DOWN  │────────►│   LCD    │                        │
│  └──────────┘         └──────────┘                        │
│                                                              │
│  Tareas:                                                    │
│  - Lectura sensor: cada 500ms                              │
│  - Control PID: cada 1s                                    │
│  - Update display: cada 200ms                              │
│  - Lectura botones: cada 50ms                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Navegación

| Anterior | Arriba | Índice Módulo |
|:--------:|:------:|:-------------:|
| [I2C/SPI](../../../03-06-protocolos-i2c-spi/solutions/prob-01/) | [Módulo MCU](../../00-Index.md) | [00-Index](../../00-Index.md) |
