# 4 - Monitoramento de salários
'''Em seu estágio, sua supervisora pediu para você criar um programa que processa os dados de uma pesquisa sobre a diferença salarial entre homens e mulheres em uma empresa, sabendo que a empresa tem pelo menos um funcionário que se identifica com cada gênero. Os dados da pesquisa foram armazenados de forma que os salários dos homens são informados como valores inteiros positivos e o das mulheres como valores inteiros negativos. O fim da entrada de dados é indicado pelo valor nulo. Seu programa deve imprimir o salário médio de mulheres e homens, nessa ordem.'''

salario_homens = 0
salario_mulheres = 0
qtd_homens = 0
qtd_mulheres = 0

while True:
  salario = int(input())
  
  if salario == 0:
    break

  if salario > 0:
    salario_homens += salario
    qtd_homens += 1
  else:
    salario_mulheres += salario
    qtd_mulheres += 1

media_mulheres = (salario_mulheres / qtd_mulheres) * -1 
media_homens = salario_homens / qtd_homens

print('%.2f' % media_mulheres)
print('%.2f' % media_homens)