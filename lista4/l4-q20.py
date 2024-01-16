# 20 - Newton #4 (Camile du Gast vítima de fakenews...
"""Desta vez seu programa deve identificar quantas voltas o carro dá até que que o carro comece a desacelerar. Seu programa lê a massa e a aceleração inicial, bem como a força imputada a cada volta , e imprime a aceleração máxima alcançada (com três casas decimais) e o total de voltas."""

numero_voltas = 0 
maior_aceleracao = 0

massa_inicial = float(input())
aceleracao_inicial = float(input())

while True:
  forca_imputada = float(input())

  aceleracao_final = forca_imputada / massa_inicial

  numero_voltas += 1

  if aceleracao_final >= aceleracao_inicial and aceleracao_final > maior_aceleracao:
    maior_aceleracao = aceleracao_final

  elif aceleracao_inicial >= aceleracao_final and aceleracao_inicial > maior_aceleracao:
    maior_aceleracao = aceleracao_inicial

  if forca_imputada < 0:
    break

print('maior aceleração: %.3f' % maior_aceleracao)
print('número de voltas: ', numero_voltas)