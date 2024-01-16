# 5 - Infinito enquanto dure
'''Ou ... Programa comilão... Seu programa deve consumir a sua própria condição de parada e, depois, consumir linhas da entrada até que seja fornecida a condição de parada lida originariamente, contando o número de linhas consumidas. Saída: O número de linhas consumidas, sem considerar a condição de parada'''

condicao_parada = input()
numero_linhas = 0 

while True:
    linha = input()
  
    if linha == condicao_parada:
        break
    else:
      numero_linhas += 1

print(numero_linhas)
