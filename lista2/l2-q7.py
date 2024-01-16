# 7 - Voto obrigatório ou facultativo?
'''Seu programa deve ler um valor inteiro, correspondente à idade de uma pessoa, e informar se essa pessoa tem idade para votar e, se for, se o voto é obrigatório ou facultativo.'''

idade = int(input())

if idade == 16 or idade == 17 or idade >= 70:
    print('Seu voto é facultativo: você pode votar ou não') 
elif idade >= 18 and idade <= 69:
    print('Seu voto é obrigatório')
else:
    print('Jovem demais para votar, espere até 16')