# 6 - Tabuada: flex
'''As crianças acharam o máximo quando descobriam que você sabe programar! e você está super orgulhosa de poder ajudar, claro! Por conta disso, a professora pediu para você fazer um programa que gera tabuadas flexíveis! vamos lá? Na primeira linha: numero do qual queremos calcular a tabuada (valor entre 1 e 99). Na segunda linha: primeiro valor da tabuada a ser gerado (valor entre 1 e 999). E, por fim, na terceira linha: último valor da tabuada a ser gerado (valor entre 1 e 999)'''

multiplicando = int(input())
multiplicador1 = int(input())
multiplicador2 = int(input())

print('Tabuada do {} de {} até {}'.format(multiplicando, multiplicador1, multiplicador2))

for item in range(multiplicador1, multiplicador2 + 1, 1):
    print('{} x {} ='.format(multiplicando, item), (multiplicando*item))