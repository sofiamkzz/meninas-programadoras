# 4	-	A prática leva à perfeição
'''Nossas meninas são resilientes! Elas não desistem enquanto o problema não é aceito. Você deve calcular quanta tentativas foram executadas até o programa ser aceito.'''

numero_tentativas = 0

while True:
  tentativas = input()
  numero_tentativas += 1

  if tentativas == 'accepted':
    break

print(numero_tentativas)