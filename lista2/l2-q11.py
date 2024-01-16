# 11 - Secular
'''Seu programa deve ler um valor inteiro, correspondente a um ano (e.g. 2023), calcular qual o século correspondente (e.g. 21), e imprimir o valor calculado. Você deve imprimir o número do século utilizando algarismos arábicos em vez de algarismos romanos, que são normalmente utilizados nesse caso.'''

ano = int(input())

if ano % 100 == 0:
    print(ano//100)
else:
    print((ano//100)+1)