#!/bin/bash
# "Glados" voice by Antoine Amarilli (https://a3nm.net/blog/glados_espeak.html)
# Modificado por @CarlosGS
# ./voz_de_glados.sh "Hola humano, esto es una prueba. Llegas a tiempo para la destrucción total"

tones=(9.19 20.21 32.6 39.38 54.1 70.62 89.19)

for a in "$@"; do
for b in $a; do
  selectedTone=${tones[$RANDOM % ${#tones[@]}]}
  if [[ ${b:0:1} != "<" ]];
  then echo -n "<prosody pitch=\"$selectedTone\">$b</prosody> ";
  else echo $b; fi \
  | sed 's/>r/>rh/' | sed 's/r</rrr</' | sed 's/R</Rr</' | sed 's/ll/y/'
done
done | espeak -m --stdout -p 60 -s 100 -a 140 -v spanish-mbrola-1 | play -t wav - \
speed 1.5 \
echos 1 1 50 0.5 10 0.5

