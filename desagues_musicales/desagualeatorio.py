#!/usr/bin/python

import time
import pygame
import glob
import random
import RPi.GPIO as GPIO
import TM1638


DIO = 17
CLK = 27
STB_derecho = 25
STB_izquierdo = 22

LED_COLOR_RED = 1
LED_COLOR_GREEN = 2
LED_COLOR_ORANGE = 3

display_derecho = TM1638.TM1638(DIO, CLK, STB_derecho)
display_izquierdo = TM1638.TM1638(DIO, CLK, STB_izquierdo)

display_derecho.enable(6)
display_izquierdo.enable(6)




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

display_izquierdo.set_text("load . . .")
display_derecho.set_text("load . . .")

print("Cargando sonidos en memoria...")
sonidos = []
N = len(lista_sonidos)
i = 0
for fichero in lista_sonidos:
    sonidos.append(pygame.mixer.Sound(fichero))
    progreso = float(i)/float(N-1)
    N_leds = int(progreso * 16)
    display_izquierdo.enciende_n_leds(LED_COLOR_GREEN, N_leds)
    display_derecho.enciende_n_leds(LED_COLOR_GREEN, N_leds-8)
    i += 1
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


poner_cancion = False
def sht_detected(io):
    global canal_izquierdo, canal_derecho, canal_musica, panning_musica, poner_cancion
    #print(io)
    poner_cancion = True
    if io == PIN_MIC_DERECHA:
        panning_musica = 0.1
        if not reproduciendo(canal_derecho):
            sound = random.choice(sonidos)
            canal_derecho.play(sound)
            canal_derecho.set_volume(0, volumen_efectos)
        actualiza_contador(0,1)
    elif io == PIN_MIC_IZQUIERDA:
        panning_musica = 0.9
        if not reproduciendo(canal_izquierdo):
            sound = random.choice(sonidos)
            canal_izquierdo.play(sound)
            canal_izquierdo.set_volume(volumen_efectos, 0)
        actualiza_contador(1,0)


contador_izquierdo = 0
contador_derecho = 0
def actualiza_contador(L,R):
    global contador_izquierdo, contador_derecho
    contador_izquierdo += L
    contador_derecho += R
    if L > 0:
        color = LED_COLOR_GREEN
        count = contador_izquierdo
        display = display_izquierdo
    if R > 0:
        color = LED_COLOR_RED
        count = contador_derecho
        display = display_derecho
    display.set_text_centered(str(count))
    display.parpadea(color)

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


display_izquierdo.set_text_centered("hola")
display_derecho.set_text_centered("hola")

reproducir_musica("./sonidos/portal_turret_salute.ogg")
set_panning_musica() # sonido al centro

display_izquierdo.parpadea(LED_COLOR_ORANGE)
time.sleep(0.6)
display_derecho.parpadea(LED_COLOR_ORANGE)

fichero = random.choice(musica_de_bienvenida)
reproducir_musica(fichero)
set_panning_musica() # sonido al centro

time.sleep(5)

display_izquierdo.set_text_centered("start")
display_derecho.set_text_centered("start")
display_izquierdo.color_leds(LED_COLOR_GREEN)
display_derecho.color_leds(LED_COLOR_GREEN)


GPIO.add_event_detect(PIN_MIC_DERECHA, GPIO.RISING, callback=sht_detected, bouncetime=500)
GPIO.add_event_detect(PIN_MIC_IZQUIERDA, GPIO.RISING, callback=sht_detected, bouncetime=500)


while True:
    set_panning_musica(True)
    time.sleep(0.3)
    if reproduciendo(canal_musica):
        poner_cancion = False
    if poner_cancion:
        fichero = random.choice(lista_musica)
        reproducir_musica(fichero)
        canal_musica.set_volume(0,0)

GPIO.cleanup()

