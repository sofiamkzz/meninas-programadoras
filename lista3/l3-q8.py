# 8 - Histograma B
'''Vamos desenhar outro histograma? Desta vez, seu programa deve ler uma linha que contém um algaritsmo entre 0 e 9. Se o valor for 0, imprimir um ponto final. Caso contrário, imprimir uma sequência de asteriscos correspondente ao valor lido.'''

algarismo = int(input())
asterisco = '*'

for item in str(algarismo):
    if algarismo != 0:
        histograma = str(int(item)*asterisco)
        print(histograma)
    else:
        print('.')