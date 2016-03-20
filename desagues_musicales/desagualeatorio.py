#!/usr/bin/python

import time
import pygame
import glob
import random
import RPi.GPIO as GPIO

volumen_efectos = 1.
volumen_musica = 0.9

PIN_MIC_DERECHA = 23
PIN_MIC_IZQUIERDA = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN_MIC_DERECHA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_MIC_IZQUIERDA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


pygame.init()


lista_sonidos = glob.glob('./sonidos/*.ogg')
lista_musica = glob.glob('./musica/*.ogg')
musica_de_bienvenida = glob.glob('./musica_de_bienvenida/*.ogg')

print(str(len(lista_sonidos)) + " sonidos disponibles")
print(str(len(lista_musica)) + " melodias disponibles")

print("Cargando sonidos en memoria...")
sonidos = [pygame.mixer.Sound(fichero) for fichero in lista_sonidos]#[1:10]]
print("OK")


canal_derecho = pygame.mixer.Channel(0)
canal_izquierdo = pygame.mixer.Channel(1)
canal_musica = pygame.mixer.Channel(2)
musica = None

panning_musica = 0.5

def reproduciendo(canal):
    return canal.get_busy() # (canal is not None) and (canal.get_sound() is not None)

def reproducir_musica(fichero):
    global canal_musica, musica
    if musica is not None:
        del musica
        musica = None
    musica = pygame.mixer.Sound(fichero)
    while reproduciendo(canal_musica) or reproduciendo(canal_izquierdo) or reproduciendo(canal_derecho):
        time.sleep(0.1)
    canal_musica.play(musica)

def sht_detected(io):
    global canal_izquierdo, canal_derecho, canal_musica, panning_musica, musica
    #print(io)
    if io == PIN_MIC_DERECHA:
        panning_musica = 0.1
        if not reproduciendo(canal_derecho):
            sound = random.choice(sonidos)
            canal_derecho.play(sound)
            canal_derecho.set_volume(0, volumen_efectos)
    elif io == PIN_MIC_IZQUIERDA:
        panning_musica = 0.9
        if not reproduciendo(canal_izquierdo):
            sound = random.choice(sonidos)
            canal_izquierdo.play(sound)
            canal_izquierdo.set_volume(volumen_efectos, 0)
    if not reproduciendo(canal_musica):
        fichero = random.choice(lista_musica)
        reproducir_musica(fichero)
        canal_musica.set_volume(0,0)


def set_panning_musica(filtrado = False):
    global panning_musica_filtrado, canal_musica
    if filtrado:
        panning_musica_filtrado = panning_musica_filtrado * 0.8 + panning_musica * 0.2
    else:
        panning_musica_filtrado = 0.5
    if reproduciendo(canal_musica):
        L = volumen_musica*(panning_musica_filtrado)
        R = volumen_musica*(1-panning_musica_filtrado)
        canal_musica.set_volume(L,R)



random.seed()


reproducir_musica("./sonidos/portal_turret_salute.ogg")
set_panning_musica() # sonido al centro

fichero = random.choice(musica_de_bienvenida)
reproducir_musica(fichero)



GPIO.add_event_detect(PIN_MIC_DERECHA, GPIO.RISING, callback=sht_detected, bouncetime=5000)
GPIO.add_event_detect(PIN_MIC_IZQUIERDA, GPIO.RISING, callback=sht_detected, bouncetime=5000)


while True:
    set_panning_musica(True)
    time.sleep(0.3)

GPIO.cleanup()

