# 19 - Mais velha entre 4 irmãs
'''Dadas as idades de quatro irmãs, quem é a mais velha? Condições: no máximo 4 comparações e sem comando de repetição.'''

idade1 = int(input())
idade2 = int(input())
idade3 = int(input())
idade4 = int(input())

if idade1 > idade2 and idade1 > idade3 and idade1 > idade4:
    print('A mais velha tem {} anos'.format(idade1))
elif idade2 > idade1 and idade2 > idade3 and idade2 > idade4:
    print('A mais velha tem {} anos'.format(idade2))
elif idade3 > idade1 and idade3 > idade2 and idade3 > idade4:
    print('A mais velha tem {} anos'.format(idade3))
elif idade4 > idade1 and idade4 > idade2 and idade4 > idade3:
    print('A mais velha tem {} anos'.format(idade4))