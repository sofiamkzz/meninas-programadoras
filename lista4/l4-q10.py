# 10 - Ajude a professora!
'''Ela precisa de sua ajuda e pede para você resolver o seguinte problema: dada uma linha com os dados de uma candidata, e uma linha com caracteres a serem substituitos, você deve imprimir a linha resultante da substituição, por um asterisco, de todos caraceres da primeira linha que se encontram na segunda linha.'''

dados = input()
caracteres = input()
dados_substituidos = ''

for i in dados:
  if i in caracteres:
    dados_substituidos += '*'
  else:
    dados_substituidos += i
print(dados_substituidos)