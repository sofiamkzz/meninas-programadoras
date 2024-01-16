# 14 - Vagas faltando ou sobrando?
'''Depois de obter o número de vagas disponíveis para uma turma, seu programa lê um nome de cada inscrita por linha. Como resultado, o programa informa se o número de vagas faltando ou sobrando. Primeira linha: o número de vagas. Linhas seguintes: um número indefinido de linhas sendo que: cada linha contém o nome de uma aluna e o fim da lista é indicado com um ponto final.'''

vagas_disponiveis = int(input())
vagas_ocupadas = 0 

while True:
    nome = input()
    if nome == '.':
      break
    else:
      vagas_ocupadas += 1

if vagas_ocupadas <= vagas_disponiveis:
  print('vagas sobrando:', vagas_disponiveis - vagas_ocupadas)
else:
  print('vagas faltando:', (vagas_disponiveis - vagas_ocupadas)* -1)