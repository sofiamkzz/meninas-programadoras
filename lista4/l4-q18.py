# 18 - Carlos Drummond de Andrade #1
'''Seu programa deve ler um número indeterminado de linhas, e imprimir cada linha como saída. O programa deve terminar quando a string CDA for lida. Saída esperada: cada uma das strings lidas (menos a última CDA) e incluir como última linha a string CDA 1942'''

while True:
  linha = input()
  
  if linha == 'CDA':
    print('CDA 1942')
    break
  else:
    print(linha)