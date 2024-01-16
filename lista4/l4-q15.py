# 15 - Aceites recebidos
'''Durante a prova do nosso curso, cada aluna pode submeter quantas vezes quiser uma solução para cada problema desde que o tempo da prova não tenha acabado. Seu programa deve identificar quantas respostas de aceitação uma menina conseguiu antes do tempo terminar.'''

aceitacoes = 0

while True:
  resposta = input()

  if resposta == 'timeout':
    break

  elif resposta == 'accepted':
    aceitacoes += 1

print(aceitacoes)