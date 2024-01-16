# 4 - Tabuada: tabulada
'''Dado um valor inteiro, imprimir a tabulada correspondente na faixa entre 1 e 11'''

valor = int(input())
print('Tabuada do', valor)

for item in range(1, 10 + 2, 1):
    print('{} x {} ='.format(valor, item), (valor*item))