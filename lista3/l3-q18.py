# 18 - Palavras ao vento #0
'''Seu programa deve ler um número indeterminado de pares de linhas. Cada par é composto por uma palavra e uma linha de texto. Para cada par, o programa deve verificar se a palavra está presente na linha e exibir 'Y' se estiver, ou 'N' caso contrário. O programa encerra quando a palavra digitada for um ponto final.'''

while True:
  palavra = input()

  if palavra == '.':
    break

  linha = input()

  if palavra in linha:
    print('Y')
  else:
    print('N')