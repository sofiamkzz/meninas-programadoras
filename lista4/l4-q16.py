# 16 - Carlos Drummond de Andrade #3
'''Seu programa deve ler um número indeterminado de strings, e imprimir o número de strings lidas como saída desde que a string não seja nula, ou seja, vazia. O programa deve terminar quando a string CDA 1942 for lida.'''

qtd_strings = 0

while True:
  linha = input()

  if linha == 'CDA 1942':
    print(qtd_strings)
    break
    
  if linha != '':
    qtd_strings += 1