# 4 - Bandeira
'''As crianças estão aprendendo a desenhar a bandeira brasileira e precisam da sua ajuda. Elas sabem o nome das cores mas não sabem o nome das figuras geométricas. 
Seu programa deve ler o nome de uma cor e informar qual a forma geométrica correspondente. '''

cor = input()

if cor == 'azul':
    print('circunferência')
elif cor == 'amarelo':
    print('losango')
elif cor == 'verde':
    print('retângulo')
elif cor == 'branco':
    print('faixa')
else:
    print('não tem essa cor')