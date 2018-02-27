#!/bin/sh

SERVICE="python"
RESULT=`ps -a | sed -n /${SERVICE}/p`

if [ "${RESULT:-null}" = null ]; then
    echo "Launching script $0"
    # Volumen de reproduccion al valor deseado (maximo: 100%)
    amixer set PCM 98%
    cd "$HOME/Codigos/automatismos-del-local/desagues_musicales"
    python desagualeatorio.py
else
    echo "Script $0 already running"
fi
