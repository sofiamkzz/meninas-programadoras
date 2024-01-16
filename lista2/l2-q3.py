# 3 - Dentro?
'''Seu programa recebe três valores inteiros, um por linha, e deve imprimir True se o último falor estiver contido na faixa estabelecida entre os dois primeiros, e False caso contrário.'''

valor1 = int(input())
valor2 = int(input())
valor3 = int(input())

if valor1 <= valor3 <= valor2:
    print('True')
else:
    print('False')