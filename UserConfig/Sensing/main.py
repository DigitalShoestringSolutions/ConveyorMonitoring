# standard imports
from time import sleep

# installed inports
import gpiozero

# local imports
from utilities.mqtt_out import publish
from hardware.generic.QuadratureEncoder import EncoderWheel

# My quadrature encoder is connected to GPIO pins 27 and 22 (BCM numbering), has 1024 pulses per revolution and circumference is 0.2 m
MyConveyorEncoder = EncoderWheel(22, 27, 1024, circ=0.2)

# Sensing loop
while True:
    sleep(0.2)
    publish( {"machine": "MachineNameHere"} | MyConveyorEncoder())
