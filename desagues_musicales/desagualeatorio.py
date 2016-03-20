#!/usr/bin/python

import time
import pygame
import glob
import random
import RPi.GPIO as GPIO

PIN_MIC_DERECHA = 23
PIN_MIC_IZQUIERDA = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN_MIC_DERECHA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_MIC_IZQUIERDA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


lista_audios = glob.glob('./sonidos/*.ogg')

print("Sonidos disponibles:")
print(lista_audios)



# start pygame
pygame.init()

# load a sound file into memory
sound = pygame.mixer.Sound("got_the_power.ogg")

minTime = 1 # Espera minima (en segundos) entre cada reproduccion


def sht_detected(io):
    fichero = random.choice(lista_audios)
    sound = pygame.mixer.Sound(fichero)
    channel = sound.play()
    if io == PIN_MIC_DERECHA:
        channel.set_volume(0, 1)
    elif io == PIN_MIC_IZQUIERDA:
        channel.set_volume(1, 0)

GPIO.add_event_detect(PIN_MIC_DERECHA, GPIO.RISING, callback=playLeft, bouncetime=minTime*1000)
GPIO.add_event_detect(PIN_MIC_IZQUIERDA, GPIO.RISING, callback=playRight, bouncetime=minTime*1000)

while True:
    time.sleep(10)

GPIO.cleanup()

