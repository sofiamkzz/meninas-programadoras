# 13 - (+ - * ** / // %)
'''Seu programa deve ler três linhas. Na primeira, um símbolo correspondendo a uma operação entre dois inteiros. (+ - * / // % **). Nas linhas seguintes, um valor inteiro cada. O programa deve calcular o resultado da operação entre os dois inteiros e imprimir o resultado.'''

simbolo = input()
valor1 = int(input())
valor2 = int(input())

if simbolo == '+':
    print(valor1 + valor2)
elif simbolo == '-':
    print(valor1 - valor2)
elif simbolo == '*':
    print(valor1 * valor2)
elif simbolo == '/':
    print(valor1 / valor2)
elif simbolo == '//':
    print(valor1 // valor2)
elif simbolo == '%':
    print(valor1 % valor2)
elif simbolo == '**':
    print(valor1 ** valor2)