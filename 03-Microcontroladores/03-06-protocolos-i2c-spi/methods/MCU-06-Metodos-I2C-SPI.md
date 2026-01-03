<!--
::METADATA::
type: method
topic_id: mcu-06-protocolos-i2c-spi
file_id: metodos-i2c-spi
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [microcontrolador, método, I2C, SPI]
search_keywords: "metodos I2C SPI, inicializacion"
-->

> 🏠 **Navegación:** [← Teoría](../theory/MCU-06-Teoria-I2C-SPI.md) | [Problemas →](../problems/MCU-06-Problemas.md)

---

# Métodos: I2C y SPI

## Método 1: Inicialización I2C (Master, AVR)

```c
void i2c_init(uint32_t scl_hz) {
    uint8_t twps = 0; // prescaler=1
    TWSR = 0;
    TWBR = (uint8_t)(((F_CPU / scl_hz) - 16) / 2);
    // Habilitar TWI
    TWCR = (1 << TWEN);
}
```

## Método 2: Start, Write Byte, Stop (I2C)

```c
static uint8_t i2c_start(uint8_t address_rw) {
    TWCR = (1 << TWINT) | (1 << TWSTA) | (1 << TWEN);
    while (!(TWCR & (1 << TWINT)));
    if ((TWSR & 0xF8) != 0x08) return 0; // START OK

    TWDR = address_rw;
    TWCR = (1 << TWINT) | (1 << TWEN);
    while (!(TWCR & (1 << TWINT)));
    uint8_t status = TWSR & 0xF8;
    return (status == 0x18 || status == 0x40); // SLA+W or SLA+R ACK
}

static void i2c_stop(void) {
    TWCR = (1 << TWINT) | (1 << TWEN) | (1 << TWSTO);
}

static uint8_t i2c_write(uint8_t data) {
    TWDR = data;
    TWCR = (1 << TWINT) | (1 << TWEN);
    while (!(TWCR & (1 << TWINT)));
    return ((TWSR & 0xF8) == 0x28); // Data ACK
}
```

## Método 3: Leer Byte con ACK/NACK (I2C)

```c
static uint8_t i2c_read_ack(void) {
    TWCR = (1 << TWINT) | (1 << TWEN) | (1 << TWEA);
    while (!(TWCR & (1 << TWINT)));
    return TWDR;
}

static uint8_t i2c_read_nack(void) {
    TWCR = (1 << TWINT) | (1 << TWEN);
    while (!(TWCR & (1 << TWINT)));
    return TWDR;
}
```

## Método 4: Leer Registro de Dispositivo I2C

```c
uint8_t i2c_read_reg(uint8_t addr7, uint8_t reg) {
    i2c_start((addr7 << 1) | 0); // write
    i2c_write(reg);
    i2c_start((addr7 << 1) | 1); // read
    uint8_t val = i2c_read_nack();
    i2c_stop();
    return val;
}
```

## Método 5: Escribir Registro I2C

```c
void i2c_write_reg(uint8_t addr7, uint8_t reg, uint8_t val) {
    i2c_start((addr7 << 1) | 0);
    i2c_write(reg);
    i2c_write(val);
    i2c_stop();
}
```

## Método 6: Inicialización SPI (Master, AVR)

```c
void spi_init(uint8_t cpol, uint8_t cpha, uint8_t clk_div) {
    // MOSI, SCK, SS como salida; MISO entrada
    DDRB |= (1 << PB3) | (1 << PB5) | (1 << PB2);
    DDRB &= ~(1 << PB4);

    // Pull-up en SS (opcional)
    PORTB |= (1 << PB2);

    // Config SPCR
    SPCR = (1 << SPE) | (1 << MSTR);
    if (cpol) SPCR |= (1 << CPOL);
    if (cpha) SPCR |= (1 << CPHA);

    // clk_div: 4, 16, 64, 128; + SPI2X para /2, /8, /32
    switch (clk_div) {
        case 4:   SPCR |= 0; break;
        case 16:  SPCR |= (1 << SPR0); break;
        case 64:  SPCR |= (1 << SPR1); break;
        case 128: SPCR |= (1 << SPR1) | (1 << SPR0); break;
    }
}
```

## Método 7: Transferencia SPI Byte

```c
uint8_t spi_transfer(uint8_t data) {
    SPDR = data;
    while (!(SPSR & (1 << SPIF)));
    return SPDR; // Devuelve byte recibido
}
```

## Método 8: Selección de Esclavo (CS)

```c
#define CS_LOW()  (PORTB &= ~(1 << PB2))
#define CS_HIGH() (PORTB |= (1 << PB2))

uint8_t spi_read_reg(uint8_t reg) {
    uint8_t val;
    CS_LOW();
    spi_transfer(reg | 0x80); // bit de read según dispositivo
    val = spi_transfer(0xFF);
    CS_HIGH();
    return val;
}
```

## Método 9: Lectura Burst SPI

```c
void spi_read_burst(uint8_t reg, uint8_t *buf, uint8_t len) {
    CS_LOW();
    spi_transfer(reg | 0x80);
    for (uint8_t i = 0; i < len; i++) {
        buf[i] = spi_transfer(0xFF);
    }
    CS_HIGH();
}
```

## Método 10: Checklist Rápido

- I2C: ¿pull-ups? ¿Dirección correcta 7-bit? ¿ACK recibido?
- SPI: ¿CPOL/CPHA correcto? ¿CS activo en LOW? ¿Velocidad dentro del datasheet?
- ¿GND común entre dispositivos?
- ¿Cables cortos y trenzados si posible?

---

<!-- IA_CONTEXT
USO: Plantillas rápidas de I2C/SPI en AVR
NIVEL: Intermedio (2/3)
HERRAMIENTAS: AVR-GCC, analizador lógico
-->
