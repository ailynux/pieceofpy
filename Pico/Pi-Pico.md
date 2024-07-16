# Raspberry Pi Pico Basics & Beyond

Welcome to the **Raspberry Pi Pico Basics & Beyond** repository! 🚀 This repository is designed to help you learn and teach the fundamentals of the Raspberry Pi Pico, including its unique features and how it differs from other microcontrollers and Raspberry Pi boards.

![image](https://github.com/user-attachments/assets/975ad139-f791-4ba6-9fab-d9fab4203202)


## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Hardware Requirements](#hardware-requirements)
  - [Software Setup](#software-setup)
- [Hello World](#hello-world)
- [Unique Features](#unique-features)
- [Projects](#projects)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **Raspberry Pi Pico** is a low-cost, high-performance microcontroller board built around the RP2040 silicon platform. This repository aims to provide you with a comprehensive guide to get started with the Pico, learn about its unique features, and explore its potential through various projects.

## Getting Started

### Hardware Requirements

- Raspberry Pi Pico
- USB micro-B cable
- Breadboard
- Jumper wires
- LEDs, resistors, and other basic electronic components

### Software Setup

1. **Download and Install Thonny**:
   - Thonny is a Python IDE perfect for beginners.
   - [Download Thonny](https://thonny.org/)

2. **Install MicroPython on the Pico**:
   - Connect your Raspberry Pi Pico to your computer while holding the `BOOTSEL` button.
   - It will mount as a mass storage device named `RPI-RP2`.
   - Download the latest MicroPython `.uf2` file from the [official site](https://micropython.org/download/rp2-pico/).
   - Drag and drop the `.uf2` file onto the `RPI-RP2` drive.

3. **Configure Thonny**:
   - Open Thonny.
   - Go to `Tools > Options > Interpreter`.
   - Select `MicroPython (Raspberry Pi Pico)` and the appropriate COM port.

## Hello World

Let's write our first program to blink an LED.

```python
import machine
import time

led = machine.Pin(25, machine.Pin.OUT)

while True:
    led.toggle()
    time.sleep(1)
```
- Save the script as blink.py in Thonny.
- Click the Run button to execute the script on your Pico.

  
## Unique Features
- RP2040 Microcontroller: Dual-core Arm Cortex-M0+ processor, flexible clock running up to 133 MHz.
- Low Power Consumption: Ideal for battery-powered projects.
- Rich Interface: 26 multi-function GPIO pins, including I2C, SPI, and UART.
- Programmable I/O (PIO): Custom peripheral support.
- Affordable: Cost-effective solution for various applications.

# Projects
Explore the projects to enhance your skills and understanding of the Raspberry Pi Pico:

- Blinking Multiple LEDs
- Temperature Sensor
- Simple Alarm System
- Remote Control Car
- Resources
- Raspberry Pi Pico Documentation
- MicroPython Documentation
- Thonny IDE

# Contributing
Contributions are welcome! Please read my Contributing Guidelines before submitting a pull request.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

#### Happy hacking! 💻✨
