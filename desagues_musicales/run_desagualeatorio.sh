
while true
do
  # Volumen de reproduccion al valor deseado (maximo: 1000)
  amixer set PCM -- 800
  python desaguealeatorio.py
  sleep 1
done

