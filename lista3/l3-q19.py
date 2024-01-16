# 19 - Segurança Duplicada
'''No seu estágio, sua supervisora pediu para você criar um programa que lê o número de algarismos do PIN e, a seguir, os algarismos que formam o PIN (um algarismo por linha).'''

numero_algarismos = int(input())
pin = ''

for i in range(numero_algarismos):
    algarismo = input()
    pin += algarismo

repetidos = False

for i in range(numero_algarismos):
    for j in range(i + 1, numero_algarismos):
        if pin[i] == pin[j]:
            repetidos = True
            break

if repetidos:
    print('ERRO')
else:
    print('OK')