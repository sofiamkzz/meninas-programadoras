# 2 - Menor ou igual
'''Seu programa deve receber três valores números inteiros, um por linha. O programa imprime True se o primeiro valor é menor ou igual ao segundo, e ao mesmo tempo, os dois últimos valores não são iguais. Caso contrário, deve exibir a resposta False'''

valor1 = int(input())
valor2 = int(input())
valor3 = int(input())

if valor1 <= valor2 and valor2 != valor3:
    print('True')
else:
    print('False')