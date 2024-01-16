# 8 - Final da placa
'''Seu programa deve ler um inteiro que corresponde aos dígitos da placa de um veículo, e verificar qual é o último dígido daquela placa.''' 

placa = int(input())

if placa >= 0 and placa <= 9999:
    print(str(placa)[-1])