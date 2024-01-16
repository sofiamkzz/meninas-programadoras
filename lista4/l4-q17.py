# 17 - Carlos Drummond de Andrade #2
'''Seu programa deve ler um número indeterminado de strings, e imprimir o número de strings lidas como saída. O programa deve terminar quando a string CDA 1942 for lida. Saída esperada: um valor inteiro com o número de strings lidas, menos a ultima que tem conteúdo CDA 1942'''

qtd_strings = 0

while True:
  linha = input()
  
  if linha == 'CDA 1942':
    print(qtd_strings)
    break
  else:
    qtd_strings += 1