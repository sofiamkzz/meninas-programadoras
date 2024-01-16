# 16 - Democracia: ... quem ganhou?
'''O programa deve computar os votos obtidos por duas candidatas. Ele considera as candidatas como candidata 'X' e candidata 'Y'. Cada eleitor vota com as letras 'X', 'Y', 'B' ou 'N, correspondendo aos votos para candidata 'X', para a candidata 'Y', a voto em branco e a voto nulo. Seu programa deve informar o número de votos obtidos por cada candidata, o total de votos brancos e nulos, e indicar quem ganhou ou se houve empate. Primeira linha: o número de votos a serem computados. E as próximas linhas: uma linha para cada voto.'''

numero_votos = int(input())
i = 0
numero_x = 0
numero_y = 0
numero_brancos_nulos = 0

while i < numero_votos:
    voto = input()
    i += 1
    
    if voto == 'X':
      numero_x += 1

    elif voto == 'Y':
      numero_y += 1

    else:
      numero_brancos_nulos += 1

print('X', numero_x)
print('Y', numero_y)
print('Brancos e nulos', numero_brancos_nulos)

if numero_x > numero_y:
  print('vitoria: X')
elif numero_x == numero_y:
  print('empate!')
else:
  print('vitoria: Y')