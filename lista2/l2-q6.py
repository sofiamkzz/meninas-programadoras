# 6 - A Compra Responsável Informada
'''Seu programa deve ler duas linhas, com um valor inteiro cada.
 - o primeiro valor corresponde ao valor em dinheiro que a pessoa tem na conta do banco
 - o segundo valor corresponde ao total calculado no carrinho de compras.
Seu programa deve verificar se a pessoa pode ou não realizar a compra de modo a respeitar sua própria decisão, e emitir mensagens correspondentes. Caso não deve ser efetuada para respeitar a decisão, informar 'seu saldo é insuficiente para essa compra'.'''

saldo = int(input())
carrinho = int(input())

if saldo >= carrinho:
    print('se você comprar tudo o saldo será:', saldo - carrinho)
else:
    print('seu saldo é insuficiente para essa compra')