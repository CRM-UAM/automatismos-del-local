# Desagües musicales

Desarrollado por [CarlosGS](https://github.com/CarlosGS) con la Raspberry Pi de [Víctor Uceda](https://github.com/VictorUceda)


Setup de la Raspberry
--

Tiene una instalación básica de [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) (ver [cómo instalar un .img en una tarjeta SD](https://www.raspberrypi.org/documentation/installation/installing-images/linux.md) )

Para evitar ruido en la reproducción de audio, hay que definir:
```
disable_audio_dither=1
```
En el fichero "/boot/config.txt"

Para que se ejecute al inicio hay que poner en el script ".profile":
```
run_desagualeatorio.sh &
```


Origen de los sonidos
--

Los audios han sido obtenidos de <http://www.instantsfun.es/> y <http://github.com/Diogenesthecynic/FullScreenMario/>

El volumen de los .ogg fue normalizado con:
```
for audio_file in *.ogg; do
    normalize-ogg $audio_file;
done
```


