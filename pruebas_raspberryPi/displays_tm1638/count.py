#!/usr/bin/env python

# TM1638 playground

import RPi.GPIO as GPIO
import TM1638
import time

# These are the pins the display is connected to. Adjust accordingly.
# In addition to these you need to connect to 5V and ground.

DIO = 17
CLK = 27
STB = 25 #22

LED_COLOR_RED = 1
LED_COLOR_GREEN = 2
LED_COLOR_ORANGE = 3

display = TM1638.TM1638(DIO, CLK, STB)

display.enable(4)

#display.set_text("abcdefgh")
#display.set_text("01234567")

#time.sleep(5)

def led_color(color):
    for i in range(8):
        display.set_led(i, color)

count = 0
while True:
    if (count % 2) == 0:
        led_color(LED_COLOR_RED)
    else:
        led_color(LED_COLOR_GREEN)
    text = str(count)
    text = text.center(8)
    display.set_text(text)
    count += 1
    time.sleep(0.1)

GPIO.cleanup()

