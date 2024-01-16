# 14 - O Aumento no Salário
'''Seu programa deve ler duas linhas, com um valor inteiro cada. O primeiro valor corresponde ao salário de uma pessoa. O segundo valor corresponde à porcentagem de aumento que deve ser adicionada ao salário. Seu programa deve calcular o valor correspondente ao aumento do salário informado, quando aplicada a porcentagem informada, e imprimir o valor calculado.'''

salario = int(input())
porcentagem = int(input())
aumento = salario * (porcentagem / 100)
print(aumento)