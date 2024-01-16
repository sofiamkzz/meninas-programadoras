# 17 - Gorjeta
'''Dados o total de uma conta (valor decimal) e a porcentagem escolhida pelo cliente para a gorjeta (valor inteiro), o programa deve calcular o valor final da conta (com duas casas decimais).'''

totalConta = float(input())
porcentagem = int(input())

print('%.2f' % (totalConta + (totalConta * porcentagem / 100)))