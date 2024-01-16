# 5 - Tabuada: valores
'''Dado um número entre 1 e 11, imprimir os valores da tabulada para multiplicações de 1 a 11'''

numero = int(input())
for item in range(1, 11 + 1, 1):
    print(numero*item)