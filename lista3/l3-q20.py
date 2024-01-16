# 20 - Senha regrada
'''Desta vez a sua supervisora no estágio quer que você verifique se a senha escolhida por um usuário obedece às regras: mais vogais que dígitos, pelo menos dois dígitos, pelo menos 8 caracteres'''

vogais = 'aeiouAEIOU'
digitos = '0123456789'
qtdDigitos = 0
qtdVogais = 0

senha = input()

for item in senha:
    if item in vogais:
        qtdVogais += 1
    elif item in digitos:
        qtdDigitos += 1

if qtdVogais > qtdDigitos and qtdDigitos >= 2 and len(senha) >= 8:
    print('OK')
else:
    print('ERRO')