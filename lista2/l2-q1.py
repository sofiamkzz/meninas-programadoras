# 1 - VV ou FF?
'''Seu programa deve receber duas strings, uma por linha.  Se ambas forem 'V', o programa deve exibir a resposta 'VV'. Se ambas as entradas forem 'F', o programa deve exibir a resposta 'FF'. Se nenhuma dessas condições for atendida, o programa deve exibir a resposta '?' para indicar uma resposta desconhecida.'''

string1 = input()
string2 = input()

if string1 == 'V' and string2 == 'V':
    print('VV')
elif string1== 'F' and string2 == 'F':
    print('FF')
else:
    print('?')
