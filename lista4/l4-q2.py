# 2 - Base 10
'''O programa deve ler símbolos que compõem um valor inteiro e imprimir o dobro do valor correspondente. Entrada: Quatro linhas contendo um único símbolo da Base 10, a primeira linha corresponde à posição mais significativa. Saída: Uma linha: o dobro do valor inteiro correspondente.'''

simbolo1 = int(input())
simbolo2 = int(input())
simbolo3 = int(input())
simbolo4 = int(input())

base = simbolo1 * (10**3) + simbolo2 * (10**2) + simbolo3 * (10**1) + simbolo4 * (10**0)
print(base * 2)