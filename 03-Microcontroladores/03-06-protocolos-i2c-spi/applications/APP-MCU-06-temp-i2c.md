# 🔧 Aplicación: Monitor de Temperatura con I2C

```
::METADATA::
tipo: aplicacion
tema: MCU-06-protocolos-i2c-spi
dificultad: avanzada
objetivo: Comunicación I2C con sensor de temperatura
::END::
```

## 📋 Descripción del Proyecto

Implementar un sistema de monitoreo de temperatura usando un sensor I2C (LM75/TMP102) y mostrar datos en LCD.

## 🎯 Objetivos de Aprendizaje

- Configurar hardware I2C del MCU
- Implementar protocolo maestro I2C
- Leer registros de sensor externo
- Procesar datos de temperatura

## 📝 Especificaciones

### Hardware
| Componente | Conexión |
|------------|----------|
| Sensor LM75 | SDA (PC4), SCL (PC5) |
| LCD 16x2 I2C | Mismo bus I2C |
| LED Alarma | PB0 |

### Direcciones I2C
| Dispositivo | Dirección (7-bit) |
|-------------|-------------------|
| LM75 | 0x48 |
| LCD (PCF8574) | 0x27 |

## 🔍 Protocolo I2C del LM75

### Registros del LM75

| Registro | Puntero | Descripción |
|----------|:-------:|-------------|
| Temperature | 0x00 | Lectura de temperatura (2 bytes) |
| Configuration | 0x01 | Configuración |
| T_hyst | 0x02 | Histéresis |
| T_os | 0x03 | Temperatura límite |

### Formato de Temperatura

```
Byte 0 (MSB): Parte entera con signo (CA2)
Byte 1 (LSB): Fracción (solo bit 7 = 0.5°C)

Ejemplo: 0x19 0x80 = 25.5°C
         0001 1001 . 1000 0000
         = 25 + 0.5 = 25.5°C

Temperatura negativa:
         0xE7 0x00 = -25°C
         1110 0111 (CA2) = -25
```

## 📝 Código de Implementación

### Inicialización I2C

```c
#include <avr/io.h>
#include <util/twi.h>

#define F_CPU 16000000UL
#define F_SCL 100000UL  // 100 kHz Standard Mode

void I2C_init(void) {
    // Calcular TWBR para 100 kHz
    // F_SCL = F_CPU / (16 + 2*TWBR*Prescaler)
    // TWBR = (F_CPU/F_SCL - 16) / (2*Prescaler)
    
    TWSR = 0;                           // Prescaler = 1
    TWBR = ((F_CPU/F_SCL) - 16) / 2;    // = 72 @ 16MHz
    TWCR = (1 << TWEN);                 // Habilitar TWI
}
```

### Funciones de Comunicación I2C

```c
// Enviar condición de START
uint8_t I2C_start(void) {
    TWCR = (1 << TWINT) | (1 << TWSTA) | (1 << TWEN);
    while (!(TWCR & (1 << TWINT)));
    return TW_STATUS;
}

// Enviar condición de STOP
void I2C_stop(void) {
    TWCR = (1 << TWINT) | (1 << TWSTO) | (1 << TWEN);
    while (TWCR & (1 << TWSTO));
}

// Escribir byte
uint8_t I2C_write(uint8_t data) {
    TWDR = data;
    TWCR = (1 << TWINT) | (1 << TWEN);
    while (!(TWCR & (1 << TWINT)));
    return TW_STATUS;
}

// Leer byte con ACK
uint8_t I2C_read_ack(void) {
    TWCR = (1 << TWINT) | (1 << TWEA) | (1 << TWEN);
    while (!(TWCR & (1 << TWINT)));
    return TWDR;
}

// Leer byte con NACK (último byte)
uint8_t I2C_read_nack(void) {
    TWCR = (1 << TWINT) | (1 << TWEN);
    while (!(TWCR & (1 << TWINT)));
    return TWDR;
}
```

### Driver del LM75

```c
#define LM75_ADDR 0x48
#define LM75_TEMP_REG 0x00

typedef struct {
    int8_t integer;    // Parte entera con signo
    uint8_t fraction;  // 0 o 5 (décimas)
} temperature_t;

temperature_t LM75_read_temp(void) {
    temperature_t temp;
    uint8_t msb, lsb;
    
    // START
    I2C_start();
    
    // Dirección + Write
    I2C_write((LM75_ADDR << 1) | 0);
    
    // Seleccionar registro de temperatura
    I2C_write(LM75_TEMP_REG);
    
    // REPEATED START
    I2C_start();
    
    // Dirección + Read
    I2C_write((LM75_ADDR << 1) | 1);
    
    // Leer 2 bytes
    msb = I2C_read_ack();
    lsb = I2C_read_nack();
    
    // STOP
    I2C_stop();
    
    // Procesar datos
    temp.integer = (int8_t)msb;  // CA2 automático
    temp.fraction = (lsb & 0x80) ? 5 : 0;  // bit 7 = 0.5°C
    
    return temp;
}
```

### Conversión y Display

```c
void print_temperature(temperature_t temp) {
    char buffer[16];
    
    if (temp.integer < 0 && temp.fraction > 0) {
        // Caso especial: -0.5 a -0.9
        sprintf(buffer, "Temp: -%d.%d C", 
                -temp.integer, temp.fraction);
    } else {
        sprintf(buffer, "Temp: %d.%d C", 
                temp.integer, temp.fraction);
    }
    
    LCD_set_cursor(0, 0);
    LCD_print(buffer);
}

// Verificar alarma
void check_alarm(temperature_t temp, int8_t threshold) {
    if (temp.integer >= threshold) {
        PORTB |= (1 << PB0);   // Encender LED
    } else {
        PORTB &= ~(1 << PB0);  // Apagar LED
    }
}
```

### Loop Principal

```c
int main(void) {
    temperature_t current_temp;
    const int8_t ALARM_THRESHOLD = 30;
    
    // Inicializaciones
    I2C_init();
    LCD_init();
    DDRB |= (1 << PB0);  // LED alarma
    
    LCD_print("Sensor LM75");
    _delay_ms(1000);
    LCD_clear();
    
    while (1) {
        current_temp = LM75_read_temp();
        print_temperature(current_temp);
        check_alarm(current_temp, ALARM_THRESHOLD);
        
        _delay_ms(500);  // Actualizar cada 500ms
    }
    
    return 0;
}
```

## 📐 Diagrama de Conexiones

```
            ATmega328P                    LM75
         ┌─────────────┐              ┌─────────┐
         │             │              │         │
         │  PC4 (SDA) ─┼──────┬───────┤ SDA     │
         │             │      │       │         │
         │  PC5 (SCL) ─┼────┬─┼───────┤ SCL     │
         │             │    │ │       │         │
         │             │    │ │  ┌────┤ A0-A2   │ → GND (addr 0x48)
         │             │    │ │  │    │         │
         │             │    │ │  │    │ VCC ────┼── +3.3V/5V
         │             │    │ │  │    │ GND ────┼── GND
         │             │    │ │  │    └─────────┘
         │             │    │ │  │
         │        VCC ─┼────┴─┴──┴── Pull-ups 4.7k
         │             │
         │   PB0 ──────┼─── LED Alarma
         │             │
         └─────────────┘

Bus I2C con pull-ups:
                      +VCC
                       │
                      4.7k
         SDA ─────────┼────────── Dispositivos I2C
                      │
                      4.7k
         SCL ─────────┼────────── Dispositivos I2C
                      │
                      GND
```

## 📊 Secuencia de Comunicación

```
Lectura de temperatura LM75:

START │ ADDR+W │ ACK │ REG │ ACK │ Sr │ ADDR+R │ ACK │ MSB │ ACK │ LSB │ NACK │ STOP
  ↓       ↓       ↓     ↓     ↓    ↓      ↓       ↓      ↓     ↓      ↓      ↓      ↓
  S    0x90     A     0x00   A    Sr    0x91     A    0x19   A    0x80    NA     P

Resultado: 0x1980 = 25.5°C
```

## ✅ Criterios de Éxito

- [ ] Comunicación I2C a 100 kHz estable
- [ ] Lectura correcta de temperatura
- [ ] Manejo de temperaturas negativas
- [ ] Alarma funcional sobre umbral
- [ ] Display actualizado cada 500ms

## 📚 Recursos Relacionados

- [MCU-06-Intro.md](../MCU-06-Intro.md)
- [GLOSSARY: i2c](../../../GLOSSARY/README.md#i2c)
- [GLOSSARY: pull-up](../../../GLOSSARY/README.md#pull-up)

---

> 💡 **Tip**: Siempre usar pull-ups externos para I2C; los internos del MCU son demasiado débiles
