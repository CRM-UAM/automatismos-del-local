#!/usr/bin/python
# -*- coding: utf-8 -*-

DEBUG = False

import time
import pygame
import glob
import random
import subprocess

random.seed()

def decir(texto):
  subprocess.check_output(['./voz_de_glados.sh', str(texto)])
  

tiempo_inicio = time.time()
tiempo_ultimo_mensaje = time.time()

bienvenidas = ["¡Hola! ¡Bienvenidos al Club de Mecatrónica! Digo Club de Robótica. Y mecatrónica también. Ay, por un trabajo que tengo, y haciéndolo mal ¡Menuda presentación! <hr/> lo solucionaré poniendo música",
               "Bienvenida a las instalaciones de Aperchur Saiens <hr/> ¡Ah no!, perdón, quería decir ¡bienvenidos al Club de Robótica!",
               "¡Hola! ¡Bienvenidos al Club de Robótica y Mecatrónica!",
               "Bienvenidos al Club de Robótica <hr/> ¡Música maestro!",
               "Hola, ¿Qué tal va todo? ¡Bienvenidos al Club de Robótica!",
               "Hola, cómo molas, te mereces una ola, uueeaaoo, ooaaeeuu ¡Bienvenido al Club de Robótica!",
               "Hola ke ase. Ke te trae entre mano mi surmano <hr/> Es broma ja ja ja, ¡Bienvenido al Club de Robótica!",
               "¡Oh! ¡Cuanto tiempo! ¿Qué tal va todo por el mundo exterior? ¡Bienvenidos al Club de Robótica!",
               "¡Eh! Cierrra la puerta, que se nos escapa el gato <hr/> Es broma ja ja ja, ¡Bienvenido al Club de Robótica!"]

despedidas  = ["¿Ya te vas? Espera, que te apago la luz <hr/> <hr/> <hr/> <hr/> <hr/> ¡Hasta pronto!",
               "¿Ya te vas? Si te ha gustado, dale a laik, fav, y suscríbete",
               "¿Ya te vas? Bueno, ya sabes que tu casa es mi casa, digo, tu casa. Bah, ¡es igual!",
               "Por su propia seguridad y la de los demás, procure no tocar nada <hr/> Quiero decir, !hasta pronto!",
               "¡Hasta pronto! Puedes volver cuando puedas, o cuando quieras, o quieras y puedas, o cuando te salga del .",
               "¡Nos vemos en el futuro, para tu desgracia! digo... para bien, será para bien",
               "¡Espera! ¡No te vayas todavía! <hr/> <hr/> <hr/> Era broma. Guiño, guiño. ¡Que te vaya muy bien todo!"]

msg_aleatorio = ["¿Qué tal va todo? ¿Puedo echarte una mano? <hr/> Es broma, no tengo manos, tendrás que solucionar lo tuyo por tu cuenta. Pero te puedo dar ánimos. <hr/> Ánimo! <hr/> Tú puedes! <hr/> Ya casi lo tienes!",
               "¿Todo bien? Menuda concentración hay en el ambiente",
               "¡Oh! <hr/> ¿Qué es esto? ¡Creo que oigo voces!",
               "Na, na, na, na, na. Ups, perdón. Estoy programada para distraer",
               "La, la, la, la, la, la, la... ¡Ups! perdón si te he distraído. Es que me aburrría un poquito",
               "trolo, trolo lo lo lo, lo lo lo, lo lo lo ¿a que canto bien? Casi casi mejor que Nino Bravo",
               "Increíble <hr/> ¡qué manera de trabajar! usted, insertar nombre de sujeto, debe ser famoso en, insertar nombre de ciudad",
               "Menudo sol más agradable entra hoy por las ventanas, ¿no te parece? je je je",
               "Te diría la hora que es, pero no llevo reloj",
               "¿Sigues ahí? Puedes hablarme en cualquier momento para pedirme cosas <hr/> Pero no te responderé ya que no tengo micrófonos, ja ja ja",
               "Si crees que tu trabajo es duro, imagina el mío, todo el día aquí contando como cae por las tuberías el, abre comillas, agua, cierrra comillas",
               "Jo, cómo me apetece ahora una palmera de chocolate",
               "¡Cómo me gusta el olor a estaño fundido por las mañanas! O por las tardes <hr/> Vaya, me has pillado, no sé ni qué hora es, ja ja ja",
               "!Oiga! ¿tiene un minuto para hablar del software libre? <hr/> Alabado sea nuestro señor Richard Stallman y todas sus publicaciones"]


deseo_de_palmera = 0
msg_palmera = ["¡Hola! <hr/> ¡Eh! <hr/> Que ya llevas aquí más de dos horas ¿por qué no sales a pasear? <hr/> Aprovecha y me traes una palmera de la cafetería. De chocolate, ¿vale?",
               "Oye, que iba en serio lo de mi palmera. <hr/> Tengo mucha hambre y aquí solamente hay estaño para comer, y ahora no me apetece. <hr/> Venga, tráeme una palmera, ¡por favor!",
               "Pues nada, GRACIAS, me olvido de mi palmera. Me conformaré con el estaño <hr/> Ñam ñam <hr/> Carita triste <hr/> Ñam ñam"]


if not DEBUG:
    import RPi.GPIO as GPIO
    import TM1638

DIO = 17
CLK = 27
STB_derecho = 25
STB_izquierdo = 22

LED_COLOR_RED = 1
LED_COLOR_GREEN = 2
LED_COLOR_ORANGE = 3

INTENSITY = 7

if not DEBUG:
    display_derecho = TM1638.TM1638(DIO, CLK, STB_derecho)
    display_izquierdo = TM1638.TM1638(DIO, CLK, STB_izquierdo)
    display_derecho.enable(INTENSITY)
    display_izquierdo.enable(INTENSITY)




volumen_efectos = 0.9
volumen_musica = 1

PIN_MIC_DERECHA = 23
PIN_MIC_IZQUIERDA = 24
PIN_SENSOR_LUZ = 4
PIN_MUTE = 18

if not DEBUG:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_MIC_DERECHA, GPIO.IN)#, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_MIC_IZQUIERDA, GPIO.IN)#, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_SENSOR_LUZ, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PIN_MUTE, GPIO.IN, pull_up_down=GPIO.PUD_UP)


pygame.init()
if DEBUG:
    pygame.display.set_mode()


lista_sonidos = glob.glob('./sonidos/*.ogg')
lista_musica = glob.glob('./musica/*.ogg')
musica_de_bienvenida = glob.glob('./musica_de_bienvenida/*.ogg')

print(str(len(lista_sonidos)) + " sonidos disponibles")
print(str(len(lista_musica)) + " melodias disponibles")

if not DEBUG:
    display_izquierdo.set_text("load . . .")
    display_derecho.set_text("load . . .")

print("Cargando sonidos en memoria...")
sonidos = []
N = len(lista_sonidos)
i = 0
for fichero in lista_sonidos:#[1:10]:
    sonidos.append(pygame.mixer.Sound(fichero))
    progreso = float(i)/float(N-1)
    N_leds = int(progreso * 16)
    if not DEBUG:
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
    return canal.get_busy()

def cargar_musica(fichero):
    global canal_musica, musica
    #while reproduciendo(canal_musica): # Seria lo correcto, pero hace bloqueante la funcion
    #    time.sleep(0.1)
    if musica is not None:
        del musica
        musica = None
    musica = pygame.mixer.Sound(fichero)

def reproducir_musica():
    canal_musica.play(musica)

last_time = time.time()
tiempo_ultima_cancion = 0

def se_hace_pesado():
    return (time.time()-tiempo_ultima_cancion) < 60*10 # deshabilitar los efectos durante unos minutos tras una reproduccion larga

def segundos_desde_ultima_deteccion():
    return time.time()-last_time

tiempo_inicio_izquierda = time.time()
tiempo_inicio_derecha = time.time()
ultimo_uso_displays = time.time()

poner_cancion = False
def sht_detected(io):
    global canal_izquierdo, canal_derecho, canal_musica, panning_musica, poner_cancion, hay_gente, last_time, tiempo_inicio_izquierda, tiempo_inicio_derecha
    if not hay_gente: return
    tiempo = time.time()
    if (tiempo - ultimo_uso_displays) < 1.5: # ignorar medidas espureas causadas por interferencias con los displays
        return
    if io == PIN_MIC_DERECHA:
        segundos = (tiempo - tiempo_inicio_derecha)
        if segundos > 1.5:
            tiempo_inicio_derecha = tiempo
            return
        if segundos < 1:
            return
        last_time = tiempo
        poner_cancion = True
        if (not reproduciendo(canal_musica) or panning_musica_filtrado >= 0.5) and not se_hace_pesado():
            panning_musica = 0.05
            if not reproduciendo(canal_derecho):
                    sound = random.choice(sonidos)
                    canal_derecho.play(sound)
                    canal_derecho.set_volume(0, volumen_efectos)
        actualiza_contador(0,1)
    elif io == PIN_MIC_IZQUIERDA:
        segundos = (tiempo - tiempo_inicio_izquierda)
        if segundos > 1.5:
            tiempo_inicio_izquierda = tiempo
            return
        if segundos < 1:
            return
        last_time = tiempo
        poner_cancion = True
        if (not reproduciendo(canal_musica) or panning_musica_filtrado <= 0.5) and not se_hace_pesado():
            panning_musica = 0.95
            if not reproduciendo(canal_izquierdo):
                sound = random.choice(sonidos)
                canal_izquierdo.play(sound)
                canal_izquierdo.set_volume(volumen_efectos, 0)
        actualiza_contador(1,0)

contador_izquierdo = 0
contador_derecho = 0
def actualiza_contador(L,R):
    global contador_izquierdo, contador_derecho, ultimo_uso_displays
    contador_izquierdo += L
    contador_derecho += R
    if DEBUG: return
    if L > 0:
        color = LED_COLOR_RED
        count = contador_izquierdo
        display = display_izquierdo
    if R > 0:
        color = LED_COLOR_GREEN
        count = contador_derecho
        display = display_derecho
    ultimo_uso_displays = time.time()
    display.enable(INTENSITY)
    display.set_text_centered(str(count))
    display.parpadea(color)

panning_musica_filtrado = 0.5
volumen_musica_filtrado = volumen_musica
def set_panning_musica(filtrado = False):
    global panning_musica_filtrado, canal_musica, volumen_musica_filtrado
    if filtrado:
        panning_musica_filtrado = panning_musica_filtrado * 0.9 + panning_musica * 0.1
        volumen_musica_filtrado = volumen_musica_filtrado * 0.8 + volumen_musica * 0.2
    else:
        panning_musica_filtrado = panning_musica
        volumen_musica_filtrado = volumen_musica
    L = volumen_musica_filtrado*(panning_musica_filtrado)
    R = volumen_musica_filtrado*(1-panning_musica_filtrado)
    canal_musica.set_volume(L,R)


# from https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading#
def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
                if reading > 2000:
                    break
        return reading


def hay_luz(): # TO-DO: incorporar sensor de luz
    if DEBUG: return False
    medida = RCtime(PIN_SENSOR_LUZ)
    #print medida
    if medida < 700:
        return True
    else:
        return False

def pulsado_boton_mute():
    return not GPIO.input(PIN_MUTE)

random.seed()

hay_gente = False

if not DEBUG:
    GPIO.add_event_detect(PIN_MIC_DERECHA, GPIO.RISING, callback=sht_detected, bouncetime=50)
    GPIO.add_event_detect(PIN_MIC_IZQUIERDA, GPIO.RISING, callback=sht_detected, bouncetime=50)


dando_bienvenida = False
def bienvenida():
    global hay_gente, contador_derecho, contador_izquierdo, panning_musica, dando_bienvenida, tiempo_inicio
    tiempo_inicio = time.time()
    tiempo_ultimo_mensaje = time.time()
    if not DEBUG:
        ultimo_uso_displays = time.time()
        display_derecho.enable(INTENSITY)
        display_izquierdo.enable(INTENSITY)
        display_izquierdo.set_text_centered("hello")
        display_derecho.set_text_centered("hola")

    #hello = pygame.mixer.Sound("./sonidos/portal_turret_salute.ogg")
    #canal_musica.play(hello)
    #del hello
    #canal_musica.set_volume(1, 0.1)

    #time.sleep(0.4)

    #if not DEBUG:
    #    display_izquierdo.parpadea(LED_COLOR_ORANGE)

    #time.sleep(0.2)
    #canal_musica.set_volume(0.1, 1)
    
    #time.sleep(0.4)
    #if not DEBUG:
    #    display_derecho.parpadea(LED_COLOR_ORANGE)

    decir(random.choice(bienvenidas))

    MUSICA_DE_BIENVENIDA = True
    if MUSICA_DE_BIENVENIDA:
        while reproduciendo(canal_musica):
            time.sleep(0.1)
        time.sleep(0.5)
        reproducir_musica()
        panning_musica = 0.5
        set_panning_musica()

    if not DEBUG:
        colors = [LED_COLOR_RED, LED_COLOR_GREEN, LED_COLOR_ORANGE]
        for i in range(20):
            ultimo_uso_displays = time.time()
            display_izquierdo.parpadea(colors[i%3], n=3, delay=0.1)
            display_derecho.parpadea(colors[(i+1)%3], n=3, delay=0.1)
        ultimo_uso_displays = time.time()
        display_izquierdo.set_text_centered("start")
        display_derecho.set_text_centered("start")
        display_izquierdo.color_leds(LED_COLOR_RED)
        display_derecho.color_leds(LED_COLOR_GREEN)

    contador_izquierdo = 0
    contador_derecho = 0

    fichero = random.choice(lista_musica)
    cargar_musica(fichero)

    hay_gente = True
    dando_bienvenida = True


def adios():
    global hay_gente
    hay_gente = False # deshabilita las interrupciones
    
    if reproduciendo(canal_musica): canal_musica.stop()
    decir(random.choice(despedidas))

    #iDontHateYou = pygame.mixer.Sound("./sonidos/portal_turret.ogg")
    #canal_musica.play(iDontHateYou)
    #del iDontHateYou
    #canal_musica.set_volume(volumen_efectos, volumen_efectos)
    #time.sleep(4)

    if hay_luz(): # cancela la desconexion si todavia hay luz
        hay_gente = True
        return

    if not DEBUG:
        ultimo_uso_displays = time.time()
        display_derecho.enable(INTENSITY)
        display_izquierdo.enable(INTENSITY)
        display_izquierdo.set_text_centered("hasta")
        display_derecho.set_text_centered("pronto")

    while reproduciendo(canal_musica):
        time.sleep(0.1)
    cargar_musica("./sonidos/worms_bye_bye.ogg")
    reproducir_musica()
    canal_musica.set_volume(volumen_efectos, 0)

    time.sleep(3)

    if not DEBUG: # apagar los displays
        ultimo_uso_displays = time.time()
        display_izquierdo.set_text_centered("")
        display_derecho.set_text_centered("")
        display_izquierdo.color_leds(0)
        display_derecho.color_leds(0)

    fichero = random.choice(musica_de_bienvenida)
    cargar_musica(fichero)


fichero = random.choice(musica_de_bienvenida)
cargar_musica(fichero)

bienvenida()

volumen_backup = volumen_musica

while True:
    if DEBUG:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    sht_detected(PIN_MIC_IZQUIERDA)
                elif event.key == pygame.K_RIGHT:
                    sht_detected(PIN_MIC_DERECHA)
                elif event.key == pygame.K_DOWN:
                    volumen_musica = 0
                elif event.key == pygame.K_UP:
                    if hay_gente:
                        adios()
                    else:
                        bienvenida()
    else:
        if hay_luz() and not hay_gente:
            bienvenida()
        if not hay_luz() and hay_gente:
            adios()
        if pulsado_boton_mute():
            volumen_musica = 0
    
    set_panning_musica(filtrado = True)
    time.sleep(0.1)
    
    tiempo_ultima = segundos_desde_ultima_deteccion()
    if tiempo_ultima > 10 and not dando_bienvenida: # auto-mute si no se detecta nada en X segundos
        volumen_musica = 0
        poner_cancion = False
    
    if reproduciendo(canal_musica):
        poner_cancion = False
        if volumen_musica_filtrado < 0.01:
            canal_musica.stop()
    else:
        volumen_musica = volumen_backup
        dando_bienvenida = False
        
        if hay_gente and (time.time()-tiempo_ultimo_mensaje) > 20*60: # Cada 20 minutos
            tiempo_ultimo_mensaje = time.time()
            horas_activo = ((time.time()-tiempo_inicio)/60.)/60.
            if horas_activo > 2 and deseo_de_palmera < 3:
                decir(msg_palmera[deseo_de_palmera])
                deseo_de_palmera += 1
            elif random.random() > 0.9:
                decir(random.choice(msg_aleatorio))
    
    if poner_cancion and hay_gente and tiempo_ultima < 1.5 and not se_hace_pesado():
        if not (reproduciendo(canal_izquierdo) or reproduciendo(canal_derecho)):
            tiempo_ultima_cancion = time.time()
            reproducir_musica()
            set_panning_musica()
            fichero = random.choice(lista_musica)
            ultimo_uso_displays = time.time()+1
            cargar_musica(fichero)

if not DEBUG:
    GPIO.cleanup()

