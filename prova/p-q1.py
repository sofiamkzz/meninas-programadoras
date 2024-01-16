# 1 - Devagar e sempre
'''O número de meninas que fazem cursos de exatas está aumentando lentamente. Seu programa deve ler o número anterior e o número atual, e informar a porcentagem de aumento.'''

numero_anterior = int(input())
numero_atual = int(input())
aumento = (numero_atual - numero_anterior) / numero_anterior * 100
print('%.2f' % aumento)
