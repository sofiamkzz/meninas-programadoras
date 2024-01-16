# 2	-	Dúvida cruel
'''O numero de meninas que fazem cursos de computação nem sempre aumenta. Seu programa deve ler o número anterior e o número atual, e informar o que aconteceu.'''

numero_precedente = int(input())
numero_vigente = int(input())

if numero_precedente > numero_vigente:
  print('diminuiu')
elif numero_precedente == numero_vigente:
  print('igual')
else:
  print('aumentou')