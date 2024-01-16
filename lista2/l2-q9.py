# 9 - Rodízio de automóveis
'''Seu programa deve ler um inteiro que corresponde ao número da placa de um veículo, e informar em qual dia da semana aquele veículo não deve circular.
Na segunda-feira não devem circular carros com final 1 e 2
Na terça-feira não devem circular carros com final 3 e 4
Na quarta-feira não devem circular carros com final 5 e 6
Na quinta-feira não devem circular carros com final 7 e 8
Na sexta-feira não devem circular carros com final 9 e 0'''

placa = int(input())

if placa >= 0 and placa <= 9999:
    final_placa = str(placa)[-1]
    
    if(final_placa == '1' or final_placa == '2'):
        print('segunda-feira')
    elif(final_placa == '3' or final_placa == '4'):
        print('terça-feira')
    elif(final_placa == '5' or final_placa == '6'):
        print('quarta-feira')
    elif(final_placa == '7' or final_placa == '8'):
        print('quinta-feira')
    elif(final_placa == '9' or final_placa == '0'):
        print('sexta-feira')