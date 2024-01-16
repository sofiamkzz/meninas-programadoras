# 14 - CPF #3
'''Ao fazerem suas inscrições no nosso curso, as candidatas devem inserir seu CPF. Para ajudar o trabalho da equipe no processamento das inscrições, seu programa deve ler o valor informado de CPF e verificar se o tamanho da string resultante é o esperado para um CPF (11 caracteres) verificar se todos os caracteres são um dos algarismos entre '0' e '9'
- o CPF sem pontos e traços, se estiver tudo certo
- ENCODING ERROR se houver algum caractere inválido
- SIZE ERROR se o tamanho não for válido'''

cpf = str(input())
cpf_novo = ''

for i in cpf:
  if i == '.' or i == '-':
      cpf_novo += ''
  else:
      cpf_novo += i

  if len(cpf_novo) == 11 and cpf_novo.isdigit():
    print(cpf_novo)

  if not cpf_novo.isdigit():
    print('ENCODING ERROR')

  if len(cpf_novo) != 11:
    print('SIZE ERROR')