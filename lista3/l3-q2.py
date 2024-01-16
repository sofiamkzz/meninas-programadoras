# 2 - Contador B
'''O programa deve ler um valor inteiro positivo e imprimir, um por linha, os valores entre 1 e o inteiro lido, inclusive.'''

valor = int(input())
for item in range(1, valor + 1, 1):
    print(item)