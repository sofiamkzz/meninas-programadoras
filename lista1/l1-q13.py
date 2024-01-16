# 13 - A Compra Questionável
'''Seu programa deve ler duas linhas, com um valor inteiro cada. O primeiro valor corresponde ao valor em dinheiro que a pessoa tem na conta do banco. O segundo valor corresponde ao total calculado no carrinho de compras. Seu programa deve calcular qual o saldo na conta depois que a pessoa pagar a conta com PIX.'''

valorConta = int(input())
valorCarrinho = int(input())
print(valorConta - valorCarrinho)