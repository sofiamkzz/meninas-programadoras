# 18 - Contido ou nao contido? (OBRIGATÓRIO)
'''Trava línguas - Contido ou nao contido?'''

parteString = input()
string1 = input()
string2 = input()

if parteString in string1:
    if parteString in string2:
        print('{} CONTIDO EM {} E {} CONTIDO EM {}'.format(parteString, string1, parteString, string2))
    else:
        print('{} CONTIDO EM {} MAS {} NÃO CONTIDO EM {}'.format(parteString, string1, parteString, string2))
elif parteString in string2:
    if parteString in string1:
        print('{} CONTIDO EM {} E {} CONTIDO EM {}'.format(parteString, string1, parteString, string2))
    else:
        print('{} NÃO CONTIDO EM {} MAS {} CONTIDO EM {}'.format(parteString, string1, parteString, string2))
else:
    print('{} NÃO CONTIDO EM {} E {} NÃO CONTIDO EM {}'.format(parteString, string1, parteString, string2))