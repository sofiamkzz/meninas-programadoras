# 3 - Votação no Senado
'''O sistema do Senado travou e você foi encarregada de fazer rapidamente um novo programa que computa os votos. Seu programa recebe os votos de cada senador, um por linha, e computa o número de votos da materia em questão. Você sabe da importância de fazer programas reusáveis e, por isso, preparou o programa de modo que o número de eleitores seja informado no início da votação.'''

numero_eleitores = int(input())
i = 1
votos_favor = 0
votos_contra = 0
outros_votos = 0

while i <= numero_eleitores:
  voto = input()

  if voto == 'F':
    votos_favor += 1

  elif voto == 'C':
    votos_contra += 1

  else:
    outros_votos += 1

  i += 1

print('a favor:', votos_favor)
print('contra:', votos_contra)
print('outros:', outros_votos)