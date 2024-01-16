# 10 - Romanos
'''Seu programa deve ler uma letra e verificar a qual algarismo romano ela corresponde. Garante-se que apenas um dos seguintes valores será fornecido como entrada: I, V, X, L, C, D, M'''

letra = input()

if letra == 'I':
    print(1)
elif letra == 'V':
    print(5)
elif letra == 'X':
    print(10)
elif letra == 'L':
    print(50)
elif letra == 'C':
    print(100)
elif letra == 'D':
    print(500)
elif letra == 'M':
    print(1000)
else:
    print('Algarismo inválido!')