#!/bin/bash
# "Glados" voice by Antoine Amarilli (https://a3nm.net/blog/glados_espeak.html)
# Modificado a español por @CarlosGS
# ./voz_de_glados.sh "Hola humano, esto es una prueba. Llegas a tiempo para la destrucción total"
for a in "$@"; do
for b in $a; do
  V=$(((($RANDOM) % 100) - 50))
  echo -n "<prosody pitch=\"+$V\">$b</prosody> " |
    sed 's/+-/-/' 
done
done | espeak -ves+f3 -m -p 40 -s 180 -a 140 -w "voz.wav"

