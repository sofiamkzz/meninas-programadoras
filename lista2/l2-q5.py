# 5 - A Compra Responsável
'''Seu programa deve ler duas linhas, com um valor inteiro cada. O primeiro valor corresponde ao valor em dinheiro que a pessoa tem na conta do banco. O segundo valor corresponde ao total calculado no carrinho de compras. Seu programa deve verificar se a pessoa pode ou não realizar a compra de modo a respeitar sua própria decisão, e emitir mensagens correspondentes: se o saldo for suficiente, informar 'pode comprar tudo'. Caso contrário, informar 'saldo insuficiente' '''

saldo = int(input())
carrinho = int(input())

if saldo >= carrinho:
    print('pode comprar tudo')
else:
    print('saldo insuficiente')