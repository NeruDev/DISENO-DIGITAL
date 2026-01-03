# 🔧 Aplicación: Data Logger I2C + UART

```
::METADATA::
tipo: aplicacion
tema: MCU-07-aplicaciones
dificultad: avanzada
objetivo: Registrar temperatura y tiempo en EEPROM I2C y enviar por UART
::END::
```

## 📋 Descripción del Proyecto

Diseñar un data logger que lea temperatura vía I2C (sensor LM75/DS1621), almacene muestras con timestamp en una EEPROM I2C (24LC256) y permita descargar los datos por UART en formato CSV.

## 🎯 Objetivos de Aprendizaje

- Integrar múltiples periféricos I2C (sensor + EEPROM) en el bus
- Gestionar direccionamiento y páginas de escritura en EEPROM
- Formatear registros como CSV y transmitirlos por UART
- Implementar comandos de control (`START`, `STOP`, `DUMP`)

## 🛠️ Pasos Clave

1) Inicializar I2C maestro (100 kHz), UART 115200 bps.
2) Cada 1 s, leer temperatura del sensor (registro `TEMP`) y el contador RTC (software o DS1307 opcional).
3) Guardar registro `timestamp, temp_c` en EEPROM secuencial (dirección auto-incremental).
4) Comando `DUMP` en UART: leer todos los registros y enviarlos como líneas CSV.
5) Comando `START/STOP`: habilitar o pausar el muestreo.

## 🧩 Estructura de Registro (16 bytes)

| Byte(s) | Campo |
|---------|-------|
| 0-3 | Timestamp (segundos, uint32) |
| 4-5 | Temperatura ×100 (int16) |
| 6-15 | Reservado / futuro |

## 🧩 Código Base (fragmento)

```c
#include "i2c.h"
#include "uart.h"

uint16_t eeprom_ptr = 0;
uint8_t sampling = 0;

void log_sample(uint32_t ts_ms, int16_t temp_cx100) {
    uint8_t buf[6];
    buf[0] = (ts_ms >> 24) & 0xFF;
    buf[1] = (ts_ms >> 16) & 0xFF;
    buf[2] = (ts_ms >> 8)  & 0xFF;
    buf[3] = (ts_ms)       & 0xFF;
    buf[4] = (temp_cx100 >> 8) & 0xFF;
    buf[5] = (temp_cx100)      & 0xFF;
    eeprom_write_seq(0x50, eeprom_ptr, buf, 6);
    eeprom_ptr += 6;
}

void dump_uart(void) {
    uint16_t ptr = 0;
    while (ptr < eeprom_ptr) {
        uint32_t ts = eeprom_read_u32(0x50, ptr); ptr += 4;
        int16_t t  = eeprom_read_i16(0x50, ptr); ptr += 2;
        printf("%lu,%d.%02d\r\n", ts, t/100, abs(t%100));
    }
}
```

## ✅ Checklist

- [x] I2C maestro inicializado
- [x] Lectura de sensor de temperatura I2C
- [x] Escritura secuencial en EEPROM
- [x] Comandos UART (`START/STOP/DUMP`)
- [x] Formato CSV

## 🔗 Referencias

- [MCU-06-Teoria-I2C-SPI.md](../theory/MCU-06-Teoria-I2C-SPI.md) *(para repaso de bus)*
- [MCU-07-Teoria-Aplicaciones.md](../theory/MCU-07-Teoria-Aplicaciones.md)
- Datasheets: LM75/DS1621, 24LC256
