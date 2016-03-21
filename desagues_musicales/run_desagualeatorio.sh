#!/bin/sh

SERVICE="run_desagualeatorio.sh"
RESULT=`ps -a | sed -n /${SERVICE}/p`

if [ "${RESULT:-null}" = null ]; then
    echo "Launching script $0"
    while true
    do
      # Volumen de reproduccion al valor deseado (maximo: 100%)
      amixer set PCM 95%
      cd "$HOME/Codigos/automatismos-del-local/desagues_musicales"
      python desagualeatorio.py
      sleep 1
    done
else
    echo "Script $0 already running"
fi

