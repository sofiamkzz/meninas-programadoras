# 13 - CPF #2
'''Ao fazerem suas inscrições, algumas alunas inserem o CPF com pontos e traços e às vezes esquecem algum digito. Para ajudar o trabalho da equipe no processamento das inscrições, seu programa deve extrair os pontos e traços, caso existam. Você também deve verificar se o tamanho da string resultando é o esperado para um CPF, que deve conter 11 caracteres.'''

cpf = str(input())
cpf_novo = ''

for i in cpf:
  if i == '.' or i == '-':
    cpf_novo += ''
  else:
    cpf_novo += i

if len(cpf_novo) == 11:
  print(cpf_novo)
  print('OK')
else:
  print(cpf_novo)
  print('ERROR')