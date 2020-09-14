#!/usr/bin/python3
from gpiozero import LED
from time import sleep
import sys
print(str(sys.argv))
light_action = sys.argv[1] == 'true'
pin_number = sys.argv[2]
led = LED(pin_number)
if(light_action == 1):
    led.on()
    print('turning on LED at pin number', pin_number)
if(light_action == 0):
    led.off()
    print('turning off LED at pin number', pin_number)
