# 7 - Volei: um ponto por linha
"""Pontos de um set de 25 de vôlei de quadra: Uma partida de vôlei de quadra pode ter de três a cinco sets. Cada set vai no mínimo até 25 pontos, sendo que diferença de pontos entre os dois times é de no mínimos dois pontos. Assim, se o placar de um set chegar a 24 x 24, o jogo não acaba em 25: em vez disso continua até que a diferença de dois pontos seja atingida."""

pontos1 = 0
pontos2 = 0

while True:
  pontos = int(input())

  if pontos == 1:
    pontos1 += 1

  else:
    pontos2 += 1
    
  if (pontos1 >= 25 and pontos1 - pontos2 >= 2) or (pontos2 >= 25 and pontos2 - pontos1 >= 2):
    break

print('{} x {}'.format(pontos1, pontos2))