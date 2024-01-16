# 8 - Soletrando: até acertar!
'''A professora do Ensino Fundamental gostou tanto do programa que você fez para o problema Soletrando que pediu para você fazer uma nova versão! Ela quer que, em caso de erro em uma tentativa de soletrar a palavra, as crianças possam realizar novas tentativa elas mesmas! Para isso, vocês combinaram com as crianças que elas podem tentar quantas vezes quiserem, e que
- quando elas acertarem, o programa imprime 8-)
- quando elas errarem, o programa imprime 8-| e elas podem tentar a mesma palavra outra vez'''

palavra = input()
nova_palavra = ''

while True:
    tentativa = input()

    if tentativa == '.':
      if nova_palavra == palavra:
        print('8-)')
        break
      else:
        nova_palavra = ''
        print('8-|')

    if tentativa != '.':
      nova_palavra += tentativa