# 11 - EMAIL #1
'''Dado o número de candidatas inscritas, analise cada email para verificar se ele contém o caractere obrigatório. Seu programa deve informar quantas das entradas não correspondem a um potencial email.'''

numero_inscritas = int(input())
contador = 0 

for i in range(numero_inscritas):
  email = input()

  if '@' in email and '.' in email:
    continue
  else: 
    contador += 1

print(contador)