# 3 - Comprando enquanto ... dá 
'''Seu programa deve terminar quando o valor disponível não permite gastar um item que se pretende comprar e, ao terminar, informar quantos itens foram comprados e o valor restante.'''

valor_disponivel = int(input())
item = 0

while True:
  valor_item = int(input())

  if valor_disponivel - valor_item < 0:
    break

  else: 
    valor_disponivel -= valor_item
    item += 1

print('Número de itens', item)
print('Saldo: %.2f' % valor_disponivel)