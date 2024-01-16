# 20 - Mais velha e mais nova entre 4 amigas
'''Mais uma vez... agora maior e menor entre 4 (No máximo 4 comparações)'''

idade1 = int(input())
idade2 = int(input())
idade3 = int(input())
idade4 = int(input())

if idade1 > idade2:
    idadeMaior1 = idade1
    idadeMenor1 = idade2
else:
    idadeMaior1 = idade2
    idadeMenor1 = idade1

if idade3 > idade4:
    idadeMaior2 = idade3
    idadeMenor2 = idade4
else:
    idadeMaior2 = idade4
    idadeMenor2 = idade3

if idadeMaior1 > idadeMaior2:
    idadeMaior = idadeMaior1
    print('A mais velha tem', idadeMaior)
else:
    idadeMaior = idadeMaior2
    print('A mais velha tem', idadeMaior)

if idadeMenor1 < idadeMenor2:
    idadeMenor = idadeMenor1
    print('A mais nova tem', idadeMenor)
else:
    idadeMenor = idadeMenor2
    print('A mais nova tem', idadeMenor)