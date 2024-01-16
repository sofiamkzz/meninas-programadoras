# 17 - Classificando caracteres..... (OBRIGATÓRIO)
'''Dado um caractere qual sua classificacao? - vogal, algarismo, especial ou outro? Neste caso, um caractere especial é um entre @#$%&*()_-+=!'''

algarismos = '0123456789'
especiais = '@#$%&*()_-+=!'
vogais = 'aeiouAEIOU'

caractere = input()

if caractere in algarismos:
    print('algarismo')
elif caractere in especiais:
    print('especial')
elif caractere in vogais:
    print('vogal')
else:
    print('outro')