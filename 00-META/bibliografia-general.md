# Bibliografía General del Repositorio

```
::METADATA::
tipo: referencia-bibliografica
nivel: repositorio
actualizado: 2026-01-03
version: 1.0
::END::
```

## Propósito

Este archivo centraliza todas las referencias bibliográficas utilizadas para validar el contenido del repositorio. Cada subtema debe referenciar las fuentes específicas que respaldan su contenido.

---

## 📚 Referencias Principales

### Diseño Digital (DD)

| ID | Referencia Completa | Abreviatura |
|----|---------------------|-------------|
| **DD-REF-01** | Morris Mano, M. & Ciletti, M. D. (2018). *Digital Design: With an Introduction to the Verilog HDL, VHDL, and SystemVerilog* (6th ed.). Pearson. | Mano & Ciletti, 2018 |
| **DD-REF-02** | Tocci, R. J., Widmer, N. S., & Moss, G. L. (2017). *Digital Systems: Principles and Applications* (12th ed.). Pearson. | Tocci et al., 2017 |
| **DD-REF-03** | Floyd, T. L. (2015). *Digital Fundamentals* (11th ed.). Pearson. | Floyd, 2015 |
| **DD-REF-04** | Wakerly, J. F. (2006). *Digital Design: Principles and Practices* (4th ed.). Pearson. | Wakerly, 2006 |
| **DD-REF-05** | Brown, S., & Vranesic, Z. (2014). *Fundamentals of Digital Logic with VHDL Design* (3rd ed.). McGraw-Hill. | Brown & Vranesic, 2014 |

### VHDL

| ID | Referencia Completa | Abreviatura |
|----|---------------------|-------------|
| **VHDL-REF-01** | Ashenden, P. J. (2008). *The Designer's Guide to VHDL* (3rd ed.). Morgan Kaufmann. | Ashenden, 2008 |
| **VHDL-REF-02** | Pedroni, V. A. (2010). *Circuit Design and Simulation with VHDL* (2nd ed.). MIT Press. | Pedroni, 2010 |
| **VHDL-REF-03** | Zwolinski, M. (2004). *Digital System Design with VHDL* (2nd ed.). Prentice Hall. | Zwolinski, 2004 |
| **VHDL-REF-04** | IEEE Std 1076-2019. *IEEE Standard VHDL Language Reference Manual*. IEEE. | IEEE 1076-2019 |
| **VHDL-REF-05** | Chu, P. P. (2008). *FPGA Prototyping by VHDL Examples*. Wiley. | Chu, 2008 |

### Microcontroladores (MCU)

| ID | Referencia Completa | Abreviatura |
|----|---------------------|-------------|
| **MCU-REF-01** | Mazidi, M. A., Naimi, S., & Naimi, S. (2017). *PIC Microcontroller and Embedded Systems*. Pearson. | Mazidi et al., 2017 |
| **MCU-REF-02** | Valdez, J., & Becker, J. (2015). *Understanding PIC Microcontrollers*. Microchip Technology. | Valdez & Becker, 2015 |
| **MCU-REF-03** | Wilmshurst, T. (2010). *Designing Embedded Systems with PIC Microcontrollers* (2nd ed.). Newnes. | Wilmshurst, 2010 |
| **MCU-REF-04** | Microchip Technology. (2023). *PIC16F887 Data Sheet*. Microchip. | DS41291G |
| **MCU-REF-05** | Microchip Technology. (2023). *MPLAB XC8 C Compiler User's Guide*. Microchip. | MPLAB XC8 Guide |

---

## 🗺️ Mapeo de Capítulos a Subtemas

### Diseño Digital (DD)

| Subtema | Referencia | Capítulos/Secciones |
|---------|------------|---------------------|
| `01-01-sistemas-numericos` | DD-REF-01 | Cap. 1: Digital Systems and Binary Numbers |
| | DD-REF-02 | Cap. 1-2: Digital Concepts, Number Systems |
| | DD-REF-03 | Cap. 2: Number Systems, Operations, and Codes |
| `01-02-algebra-booleana` | DD-REF-01 | Cap. 2: Boolean Algebra and Logic Gates |
| | DD-REF-02 | Cap. 3-4: Logic Gates, Boolean Algebra |
| | DD-REF-03 | Cap. 3-4: Logic Gates, Boolean Algebra |
| `01-03-compuertas-logicas` | DD-REF-01 | Cap. 2-3: Boolean Algebra, Gate-Level Minimization |
| | DD-REF-02 | Cap. 3: Logic Gates |
| | DD-REF-03 | Cap. 3: Logic Gates |
| `01-04-circuitos-combinacionales` | DD-REF-01 | Cap. 4: Combinational Logic |
| | DD-REF-02 | Cap. 5-6: Combinational Logic |
| | DD-REF-03 | Cap. 5-6: Combinational Logic Analysis |
| `01-05-circuitos-secuenciales` | DD-REF-01 | Cap. 5-6: Synchronous Sequential Logic |
| | DD-REF-02 | Cap. 7-8: Latches, Flip-Flops, Counters |
| | DD-REF-03 | Cap. 7-8: Latches, Flip-Flops |
| `01-06-contadores-registros` | DD-REF-01 | Cap. 6: Registers and Counters |
| | DD-REF-02 | Cap. 8-9: Counters, Shift Registers |
| | DD-REF-03 | Cap. 8-9: Counters, Shift Registers |
| `01-07-memorias` | DD-REF-01 | Cap. 7: Memory and Programmable Logic |
| | DD-REF-02 | Cap. 11: Memory Devices |
| | DD-REF-03 | Cap. 11: Data Storage |

### VHDL

| Subtema | Referencia | Capítulos/Secciones |
|---------|------------|---------------------|
| `02-01-introduccion-vhdl` | VHDL-REF-01 | Cap. 1-2: Introduction, Scalar Data Types |
| | VHDL-REF-05 | Cap. 1-2: Gate-Level Combinational Circuit |
| `02-02-entidades-arquitecturas` | VHDL-REF-01 | Cap. 3-4: Entity, Architecture |
| | VHDL-REF-02 | Cap. 2-3: Basic Concepts |
| `02-03-tipos-datos` | VHDL-REF-01 | Cap. 5-6: Composite, Access Types |
| | VHDL-REF-04 | Sec. 5: Types |
| `02-04-sentencias-concurrentes` | VHDL-REF-01 | Cap. 7: Concurrent Statements |
| | VHDL-REF-02 | Cap. 4: Concurrent Code |
| `02-05-sentencias-secuenciales` | VHDL-REF-01 | Cap. 8: Sequential Statements |
| | VHDL-REF-02 | Cap. 5: Sequential Code |
| `02-06-maquinas-estados` | VHDL-REF-01 | Cap. 10: FSM Design |
| | VHDL-REF-05 | Cap. 10: Finite State Machine |
| `02-07-sintesis-simulacion` | VHDL-REF-01 | Cap. 21-22: Test Benches |
| | VHDL-REF-03 | Cap. 9-10: Synthesis |

### Microcontroladores (MCU)

| Subtema | Referencia | Capítulos/Secciones |
|---------|------------|---------------------|
| `03-01-arquitectura-mcu` | MCU-REF-01 | Cap. 1-2: Introduction to MCU |
| | MCU-REF-04 | Sec. 1-3: Device Overview |
| `03-02-registros-puertos` | MCU-REF-01 | Cap. 3-4: I/O Port Programming |
| | MCU-REF-04 | Sec. 4: I/O Ports |
| `03-03-timers-interrupciones` | MCU-REF-01 | Cap. 9-11: Timer, Interrupts |
| | MCU-REF-04 | Sec. 6, 14: Timer, Interrupts |
| `03-04-adc-dac` | MCU-REF-01 | Cap. 13: ADC, DAC |
| | MCU-REF-04 | Sec. 9: Analog-to-Digital Converter |
| `03-05-comunicacion-serial` | MCU-REF-01 | Cap. 10: Serial Communication |
| | MCU-REF-04 | Sec. 12: EUSART Module |
| `03-06-protocolos-i2c-spi` | MCU-REF-01 | Cap. 14-15: I2C, SPI |
| | MCU-REF-04 | Sec. 13, 15: MSSP Module |
| `03-07-aplicaciones` | MCU-REF-01 | Cap. 16-18: Applications |
| | MCU-REF-03 | Cap. 10-12: Practical Projects |

---

## ✅ Estado de Validación por Subtema

### Leyenda de Estados
- `✅ validado` - Contenido revisado contra bibliografía
- `⚠️ parcial` - Algunas secciones validadas
- `🔄 pendiente` - En proceso de validación
- `❌ sin-validar` - No ha sido verificado

### Diseño Digital

| Subtema | Estado | Validador | Fecha | Notas |
|---------|--------|-----------|-------|-------|
| `01-01-sistemas-numericos` | 🔄 pendiente | - | - | Estructura creada |
| `01-02-algebra-booleana` | 🔄 pendiente | - | - | Estructura creada |
| `01-03-compuertas-logicas` | 🔄 pendiente | - | - | Estructura creada |
| `01-04-circuitos-combinacionales` | 🔄 pendiente | - | - | Estructura creada |
| `01-05-circuitos-secuenciales` | 🔄 pendiente | - | - | Estructura creada |
| `01-06-contadores-registros` | 🔄 pendiente | - | - | Estructura creada |
| `01-07-memorias` | 🔄 pendiente | - | - | Estructura creada |

### VHDL

| Subtema | Estado | Validador | Fecha | Notas |
|---------|--------|-----------|-------|-------|
| `02-01-introduccion-vhdl` | 🔄 pendiente | - | - | Estructura creada |
| `02-02-entidades-arquitecturas` | 🔄 pendiente | - | - | Estructura creada |
| `02-03-tipos-datos` | 🔄 pendiente | - | - | Estructura creada |
| `02-04-sentencias-concurrentes` | 🔄 pendiente | - | - | Estructura creada |
| `02-05-sentencias-secuenciales` | 🔄 pendiente | - | - | Estructura creada |
| `02-06-maquinas-estados` | 🔄 pendiente | - | - | Estructura creada |
| `02-07-sintesis-simulacion` | 🔄 pendiente | - | - | Estructura creada |

### Microcontroladores

| Subtema | Estado | Validador | Fecha | Notas |
|---------|--------|-----------|-------|-------|
| `03-01-arquitectura-mcu` | 🔄 pendiente | - | - | Estructura creada |
| `03-02-registros-puertos` | 🔄 pendiente | - | - | Estructura creada |
| `03-03-timers-interrupciones` | 🔄 pendiente | - | - | Estructura creada |
| `03-04-adc-dac` | 🔄 pendiente | - | - | Estructura creada |
| `03-05-comunicacion-serial` | 🔄 pendiente | - | - | Estructura creada |
| `03-06-protocolos-i2c-spi` | 🔄 pendiente | - | - | Estructura creada |
| `03-07-aplicaciones` | 🔄 pendiente | - | - | Estructura creada |

---

## 📋 Instrucciones para Validación

### Proceso de Validación

1. **Seleccionar subtema** a validar
2. **Consultar mapeo** de capítulos correspondiente
3. **Verificar** que el contenido sea consistente con las fuentes
4. **Documentar** discrepancias o mejoras necesarias
5. **Actualizar** estado en la tabla de validación
6. **Actualizar** el campo `validation_status` en el `manifest.json` del subtema

### Formato para `manifest.json`

```json
{
  "references": [
    {
      "id": "DD-REF-01",
      "chapters": ["Cap. 1"],
      "pages": "1-45"
    }
  ],
  "validation_status": {
    "status": "pendiente",
    "validated_by": null,
    "validation_date": null,
    "notes": "Estructura creada, pendiente validación de contenido"
  }
}
```

---

## 🔗 Referencias Adicionales

### Recursos en Línea
- [All About Circuits](https://www.allaboutcircuits.com/) - Tutoriales de electrónica digital
- [NAND2Tetris](https://www.nand2tetris.org/) - Curso de computación desde compuertas
- [EDA Playground](https://www.edaplayground.com/) - Simulador VHDL en línea
- [Microchip Developer Help](https://microchipdeveloper.com/) - Recursos oficiales MCU

### Herramientas Recomendadas
- **VHDL:** GHDL, ModelSim, Vivado
- **MCU:** MPLAB X IDE, XC8 Compiler, Proteus
- **Simulación:** Logisim Evolution, Digital

---

> **Nota:** Este archivo debe actualizarse cada vez que se agreguen nuevas referencias o se valide contenido.
