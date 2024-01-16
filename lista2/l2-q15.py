# 15 - O Maior e o Menor entre 3
'''Dados três valores inteiros, o programa deve identificar quem é o maior e quem é o menor'''

valor1 = int(input())
valor2 = int(input())
valor3 = int(input())

if valor1 > valor2 and valor1 > valor3:
    if valor2 > valor3:
        print('maior:', valor1)
        print('menor:', valor3)
    else:
        print('maior:', valor1)
        print('menor:', valor2)

elif valor2 > valor1 and valor2 > valor3:
    if valor1 > valor3:
        print('maior:', valor2)
        print('menor:', valor3)
    else:
        print('maior:', valor2)
        print('menor:', valor1)

elif valor3 > valor1 and valor3 > valor2:
    if valor2 > valor1:
        print('maior:', valor3)
        print('menor:', valor1)
    else:
        print('maior:', valor3)
        print('menor:', valor2)