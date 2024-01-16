# 7 - Histograma A
'''Vamos desenhar um histograma? Seu programa deve ler uma linha que contém um algaritsmo entre 1 e 9, e imprimir uma sequência de asteriscos correspondente ao valor lido.'''

algarismo = int(input())
asterisco = '*'

for item in str(algarismo):
    histograma = str(int(item)*asterisco)
    print(histograma)