# 17 - Balanço Financeiro Simplificado
'''Você deve ler um conjunto de valores correspondentes a pagamentos (valores negativos) e recebimentos (valores positivos) e informar o balanço final. Primeira linha: inteiro positivo com o número de movimentações financeiras a serem processadas. Próximas linhas: um total de linhas que correspondente ao número de movimentações financeiras (cada valor pode ter até duas casas decimais)'''

numero_movimentacoes = int(input())
balanca = 0

for i in range(numero_movimentacoes):
  valor = float(input())
  balanca += valor
print('%.2f' % balanca)