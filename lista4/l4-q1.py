# 1 - Base 2
'''O programa deve ler símbolos que compõem um valor binário e imprimir o valor decimal correspondente.'''

linha1 = int(input())
linha2 = int(input())
linha3 = int(input())
linha4 = int(input())

base = (linha1*(2**3) + linha2*(2**2) + linha3*(2**1) + linha4*(2**0))
print(base)
