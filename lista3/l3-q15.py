# 15 - Participação de monitorias
'''Verificar se cada uma de um conjunto de alunas tem horas de monitorias suficientes durante as quatro semanas do curso. Para cada aluna, 5 linhas: 1. nome da aluna, 2. numero de minutos de monitoria na semana 1, 3. numero de minutos de monitoria na semana 2, 4. numero de minutos de monitoria na semana 3, 5. numero de minutos de monitoria na semana 4'''

numero_alunas = int(input())

for i in range(numero_alunas):
  nome = input()
  mnts_semana1 = int(input())
  mnts_semana2 = int(input())
  mnts_semana3 = int(input())
  mnts_semana4 = int(input())
  
  if (mnts_semana1 >= 120) and (mnts_semana2 >= 120) and (mnts_semana3 >= 120) and (mnts_semana4 >= 120):
    print(nome, 'tem monitorias OK! :-)')
  else:
    print(nome, 'não tem monitorias suficientes :-(')