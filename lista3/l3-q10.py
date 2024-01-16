# 10 - Desenhando...
'''O programa deve ler uma string composta por dígitos e produzir um desenho que possua tantas linhas quanto a string possua dígitos, sendo que cada linha possui um número de asteriscos correspondente ao valor inteiro do dígito correspondente àquela linha. *mesma lógica da questão 9*'''

string = input()
asterisco = '*'

for item in string:
    print(str(int(item)*asterisco))