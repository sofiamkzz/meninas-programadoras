# 3 - Quantos valores superam a pior estimativa?
'''Para ajudar aqueles que se preocupam com o meio ambiente, seu programa deve ajudar a monitorar o desmatamento na Amazônia. Para isso, seu programa deve ajudar a identificar o número de ocorrências com taxa de desmatamento superior à pior estimativa calculada pelas autoridades da área. Seu programa recebe o valor correspondente à pior estimativa e o número de valores a ser processado. A seguir, o programa recebe as taxas informadas pelas agências de monitoramento. Seu programa deve informar quantas entre as taxas informadas superam a pior estimativa.'''

pior_estimativa = float(input())
numero_valores = int(input())
contador = 0
i = 1

while i <= numero_valores:
  taxas = float(input())
  i += 1
  if taxas > pior_estimativa:
    contador += 1

print(contador)