# 15 - O Salário Reajustado
'''Seu programa deve ler duas linhas, com um valor inteiro cada. O primeiro valor corresponde ao salário de uma pessoa. O segundo valor corresponde à porcentagem de aumento que deve ser adicionada ao salário. Seu programa deve calcular o novo salário, e imprimir o valor calculado.'''

salario = int(input())
porcentagem = float(input())

print(salario + (salario * porcentagem / 100))