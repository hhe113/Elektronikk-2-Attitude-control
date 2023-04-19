# Denne koden skanner alle adresser på I2C busen og printer ut alle adresser som gir respons.
# Brukes for å teste om en modul er tilkoblet.

import machine
import time
import sys

# Define the I2C bus
sdaPIN=machine.Pin(4)
sclPIN=machine.Pin(5)

# Initialize the I2C bus
i2c=machine.I2C(0,sda=sdaPIN, scl=sclPIN, freq=400000)

# Scan the I2C bus for devices
print("Scanning I2C bus...")
devices = i2c.scan()
if len(devices) == 0:
    print("No I2C devices found!")
else:
    print("I2C devices found:",len(devices))
    for device in devices:
        print("Decimal address: ",device," | Hexa address: ",hex(device))