# 12 - CPF #1
'''Ao fazerem suas inscrições, algumas alunas inserem o CPF com pontos e traços. Para ajudar o trabalho da equipe no processamento das inscrições, seu programa deve ler o valor informado de CPF e informar o CPF após extrair os pontos e traços, caso existam.'''

cpf = str(input())
cpf_novo = ''

for i in cpf:
  if i == '.' or i == '-':
    cpf_novo += ''
  else:
    cpf_novo += i

print(cpf_novo)