# 2 - Qual dos dois?
'''Qual entre dois anos teve maior taxa de desmatamento? Dado que a preocupação com o meio ambiente é uma prioridade, o seu programa deve ajudar a identificar a taxa de desmatamento mais alta entre dois anos quaisquer. Seu programa deve ler o valor de dois anos e a taxa de desmatamento correspondente, a seguir, calcular e informar qual ano teve a maior taxa, ou se foram iguais.'''

valor_ano1 = int(input())
taxa_desmatamento1 = float(input())
valor_ano2 = int(input())
taxa_desmatamento2 = float(input())

if taxa_desmatamento1 > taxa_desmatamento2:
  print(valor_ano1)
elif taxa_desmatamento1 == taxa_desmatamento2:
  print('iguais')
else:
  print(valor_ano2)