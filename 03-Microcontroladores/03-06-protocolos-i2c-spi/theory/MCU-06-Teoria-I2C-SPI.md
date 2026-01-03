<!--
::METADATA::
type: theory
topic_id: mcu-06-protocolos-i2c-spi
file_id: teoria-i2c-spi
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [microcontrolador, I2C, SPI, bus, protocolo]
search_keywords: "I2C, SPI, bus serie, maestro esclavo"
-->

> 🏠 **Navegación:** [← Volver al Índice](../03-06-Intro.md) | [Métodos →](../methods/MCU-06-Metodos-I2C-SPI.md)

---

# Protocolos I2C y SPI

## 1. Panorama General

| Protocolo | Líneas | Velocidad típica | Topología | Half/Full | Uso común |
|-----------|--------|------------------|-----------|-----------|-----------|
| I2C | SDA, SCL | 100k / 400k / 1MHz | Multimaestro, multidrop | Half | Sensores, RTC, EEPROM |
| SPI | SCK, MOSI, MISO, CS | 1-20+ MHz | Maestro-esclavo, punto-multipunto con CS | Full | Memorias Flash, pantallas, ADC rápidos |

---

## 2. I2C

### 2.1 Señales y Rol

- **SCL**: reloj generado por maestro
- **SDA**: datos bidireccionales
- Pull-ups obligatorios (open-drain)
- Direccionamiento de 7 o 10 bits (usamos 7 bits aquí)

### 2.2 Formato de Trama

```
START  Addr[6:0]  R/W  ACK  DATA  ACK ... DATA  ACK/NACK  STOP
  ↓       7b       1b   1b   8b    1b         8b     1b     ↓
```

- **START (S)**: SDA ↓ mientras SCL=1
- **STOP (P)**: SDA ↑ mientras SCL=1
- **ACK**: receptor pone SDA=0 en 9º pulso

### 2.3 Bit Rate

$$f_{I2C} = \frac{1}{t_{HIGH} + t_{LOW}}$$

Modos típicos: 100k (Standard), 400k (Fast), 1MHz (Fast Mode Plus)

### 2.4 Direcciones Especiales

- 0x00: Broadcast general call
- 0x7F: Reservada
- Algunas direcciones reservadas (0x78-0x7B, etc.)

### 2.5 Condiciones de Error

- NACK tras dirección → dispositivo no responde
- Bus ocupado (SCL o SDA en LOW)
- Arbitration lost (si multi-maestro)

---

## 3. SPI

### 3.1 Señales y Rol

- **SCK**: reloj del maestro
- **MOSI**: Master Out Slave In
- **MISO**: Master In Slave Out
- **CS/SS**: Chip Select (activo en LOW)

### 3.2 Fases y Polaridad

Controladas por CPOL y CPHA (0/1):

| Modo | CPOL | CPHA | Muestreo | Transición |
|------|------|------|----------|------------|
| 0 | 0 | 0 | Flanco de subida | Cambio en bajada |
| 1 | 0 | 1 | Flanco de bajada | Cambio en subida |
| 2 | 1 | 0 | Flanco de bajada | Cambio en subida |
| 3 | 1 | 1 | Flanco de subida | Cambio en bajada |

### 3.3 Velocidad

```
f_SPI = f_CLK / prescaler
```

Depende del micro; en AVR típicos prescaler: /2, /4, /8, /16, /32, /64, /128

### 3.4 Cadena de Bytes

SPI es **full duplex**: mientras se envía un byte por MOSI, se recibe otro por MISO.

```
Maestro: MOSI -> [b7 b6 b5 b4 b3 b2 b1 b0]
Esclavo: MISO <- [x7 x6 x5 x4 x3 x2 x1 x0]
```

---

## 4. Comparativa Rápida

| Factor | I2C | SPI |
|--------|-----|-----|
| Pines | 2 | 3 + CS por esclavo |
| Velocidad | ≤1MHz (base) | 10+ MHz |
| Direcciones | 7/10 bits | Selección por CS |
| Duplex | Half | Full |
| Hardware | Open-drain + pull-up | Push-pull |
| Longitud cable | Mejor para distancias cortas con poco ruido | Mejor con cables cortos y buenas masas |

---

## 5. I2C en AVR (TWI)

### 5.1 Registros Clave

| Registro | Función |
|----------|---------|
| TWBR | Bit rate (junto a prescaler) |
| TWSR | Status y prescaler |
| TWDR | Datos |
| TWCR | Control (START, STOP, ACK) |
| TWAR | Dirección (modo esclavo) |

### 5.2 Frecuencia I2C

$$F_{SCL} = \frac{F_{CPU}}{16 + 2 \times TWBR \times 4^{Prescaler}}$$

Prescaler en TWSR bits TWPS1:0 (00=1, 01=4, 10=16, 11=64)

Ejemplo: F_CPU=16MHz, F_SCL=100k, prescaler=1 → TWBR≈72

### 5.3 Estados TWSR (Master)

- 0x08: START transmitido
- 0x18: SLA+W ACK
- 0x40: SLA+R ACK
- 0x28: Data transmitido ACK
- 0x50: Data recibido ACK
- 0x58: Data recibido NACK (último byte)

---

## 6. SPI en AVR

### 6.1 Registros Clave

| Registro | Función |
|----------|---------|
| SPCR | Control (SPE, MSTR, CPOL, CPHA, SPR1:0) |
| SPSR | Status (SPIF, WCOL, SPI2X) |
| SPDR | Datos (TX/RX) |

### 6.2 Frecuencia SPI

$$f_{SPI} = \frac{F_{CPU}}{Prescaler} \times (2 \text{ si SPI2X=1})$$

Prescaler base (SPR1:SPR0): /4, /16, /64, /128

---

## 7. Señal Eléctrica y Pull-ups

- I2C: SDA/SCL open-drain → requiere resistencias de pull-up típicas 2.2k-10k
- SPI: líneas push-pull, no requieren pull-ups (solo CS puede necesitar)

---

## 8. Errores y Debug

- I2C: revisar ACK/NACK, usar analizador lógico, verificar pull-ups
- SPI: revisar modo (CPOL/CPHA), velocidad, CS activo

---

## 9. Ejemplo de Aplicaciones

- I2C: sensores IMU (MPU6050), RTC (DS3231), EEPROM 24Cxx
- SPI: memorias Flash W25Q, pantallas TFT, ADC MCP3008

---

<!-- IA_CONTEXT
NIVEL: Intermedio (2/3)
PREREQUISITOS: 03-01, 03-02, 03-03, 03-04, 03-05
CONEXIONES: Sensores, memoria externa, displays
ERRORES_COMUNES: Pull-ups incorrectos, CPOL/CPHA mal configurados, CS sin manejar
-->
