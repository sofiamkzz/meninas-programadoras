# 9 - Histograma C
'''O programa deve ler uma linha que contém uma sequência de caracteres, sendo que todos os caracteres são digitos entre 1 e 9. Para cada dígito, seu programa deve imprimir uma linha com uma sequência de asteriscos correspondente ao valor representado pelo dígito.'''

string = input()
asterisco = '*'

for item in string:
    print(str(int(item)*asterisco))