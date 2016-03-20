
while true
do
  # Volumen de reproduccion al valor deseado (maximo: 100%)
  amixer set PCM 95%
  python desagualeatorio.py
  sleep 1
done

