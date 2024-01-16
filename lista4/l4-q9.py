# 9 - Ajude as crianças!
'''As crianças estão aprendendo o conceito de valor mínimo, e a professora delas pediu sua ajuda. Seu programa deve ler o valor mínimo esperado e, a seguir, um conjuntos de valores. Quanto o valor mínimo for atingido, você imprime o mínimo, o total e quanto sobrou além do mínimo. '''

valor_minimo = int(input())
contador = 0

while True:
  i = int(input())

  contador += i

  if contador >= valor_minimo:
    break

print('minimo', valor_minimo)
print('total', contador)
print('sobra', contador - valor_minimo)