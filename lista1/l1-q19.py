# 19 - Horas e minutos 
'''Dado um número de minutos, seu programa deve calcular os números de horas e de minutos correspondente, ou seja, um dado número de minutos corresponde a quantas horas e minutos?'''

qtdMin = int(input())

horas = qtdMin // 60
minutos = qtdMin % 60

print('{}min = {}h{}min'.format(qtdMin, horas, minutos))