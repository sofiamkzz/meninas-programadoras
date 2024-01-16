# 13 - Dispositivos inteligentes
'''O programa deve ler um conjunto de valores do sensor e informar se o portador do dispositivo está sedentário ou ativo, assumindo que: o usuário está ativo quando o número de leituras que indicam movimento é maior que o de leituras que indicam parado e que o dispositivo já começa parado'''

leitura_parado = 1
leitura_movimento = 0

while True:
  valores = input()

  if valores == 'f':
    break

  elif valores == 'm':
    leitura_movimento += 1

  elif valores == 'p':
    leitura_parado += 1

if leitura_movimento > leitura_parado:
  print('ativo')
else:
  print('sedentário')