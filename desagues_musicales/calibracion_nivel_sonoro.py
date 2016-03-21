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


pygame.init()

sonido = pygame.mixer.Sound("./sonidos/chan.ogg")


canal_derecho = pygame.mixer.Channel(0)
canal_izquierdo = pygame.mixer.Channel(1)


def sht_detected(io):
    if io == PIN_MIC_DERECHA:
        canal_derecho.play(sonido)
        canal_derecho.set_volume(0, 1)
    elif io == PIN_MIC_IZQUIERDA:
        canal_izquierdo.play(sonido)
        canal_izquierdo.set_volume(1, 0)


GPIO.add_event_detect(PIN_MIC_DERECHA, GPIO.RISING, callback=sht_detected, bouncetime=500)
GPIO.add_event_detect(PIN_MIC_IZQUIERDA, GPIO.RISING, callback=sht_detected, bouncetime=500)


while True:
    time.sleep(1)

GPIO.cleanup()

