# 3 - Contador C
'''Seu programa deve ler um valor inteiro positivo e imprimir, um por linha, os valores pares entre 0 e o inteiro lido, inclusive.'''

valor = int(input())
for item in range(0, valor + 1, 1):
    if item % 2 == 0:
        print(item)