# 16 - O operador in (OBRIGATÓRIO)
'''O operador `in` é usado em Python para verificar se um valor está presente em uma sequência como uma string etc. Dada uma string, ela está contida em outra?'''

parteString = input()
string = input()

if parteString in string:
    print('{} in {}'.format(parteString, string))
else:
    print('{} not in {}'.format(parteString, string))