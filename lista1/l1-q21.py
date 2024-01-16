# 21 - ENEM#1
'''Dados as notas em cada área obtidas por uma candidata mas provas do ENEM, e os pesos de cada área, apresente o total de pontos correspondentes.'''

nota1 = int(input())
nota2 = int(input())
nota3 = int(input())
nota4 = int(input())
nota5 = int(input())

peso1 = int(input())
peso2 = int(input())
peso3 = int(input())
peso4 = int(input())
peso5 = int(input())

pontos = (float((nota1 * peso1 + nota2 * peso2 + nota3 * peso3 + nota4 * peso4 + nota5 * peso5) / (peso1 + peso2 + peso3 + peso4 + peso5)))
print(pontos)