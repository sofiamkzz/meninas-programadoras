# 12 - Usando o teclado para jogar
'''As teclas A S W D são parte importante de qualquer jogo que utilize o teclado. (Quase) Todo mundo sabe que elas correspondem a teclas de direção e sentido. Seu programa deve ler um valor correspondente a uma tecla (como uma string normal, ou seja, usando diretamente o resultado da função input()). A seguir, seu programa deve identificar se o valor lido corresponde uma das teclas A S W D,  que podem ser digitadas com letra minúsculas ou maiúsculas. Se for uma dessas teclas, informar qual é, em inglês e sempre em letras maísculas (veja os exemplos). Se nao for, seu programa informa um ponto de interrogação'''

tecla = input()

if tecla == 'W' or tecla == 'w':
    print('UP')
elif tecla == 'A' or tecla == 'a':
    print('LEFT')
elif tecla == 'S' or tecla == 's':
    print('DOWN')
elif tecla == 'D' or tecla == 'd':
    print('RIGHT')
else:
    print('?')