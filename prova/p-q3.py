# 3	- Resiliência
'''Resiliência vem do latim `resilire`, esse termo significa *voltar atrás*. Ele está associado à capacidade que temos de de superar momentos difíceis. Nós meninas praticamos um monte para a prova. Seu programa deve, dado o numero de listas de exercícios e o número de exercícios em cada lista, informar quantos exercícios elas resolveram.'''

numero_listas = int(input())
numero_exercicios_resolvidos = 0

for i in range(numero_listas):
  numero_exercicios = int(input())

  if numero_exercicios > 0:
    numero_exercicios_resolvidos += numero_exercicios
    
print(numero_exercicios_resolvidos)