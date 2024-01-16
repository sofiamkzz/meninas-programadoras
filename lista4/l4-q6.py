# 6 - Soletrando....
'''Seu programa primeiro lê a palavra que as crianças devem soletrar. A seguir, a criança digita uma sequencia de letras, uma por linha, e, quando terminar, digita o ponto final. Você sinaliza para a professora com True e False, respectivamente, caso a criança acerte ou não a palavra.
Entrada: primeira linha: uma palavra simples  (sem espaços), linhas seguintes: uma letra por linha, última linha: um ponto final.'''

resposta = True

palavra = input()
palavra_final = ''

while True:
    letra = input()

    if letra == '.':
      break

    palavra_final += letra
  
    if palavra_final == palavra:
      resposta = True
    else:
      resposta = False
        
print(resposta)