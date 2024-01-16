# 4	- Memória utilizada
'''Para colocar os nomes das alunas em uma string, o programa precisa de memória  ao eliminar nomes, o programa libera memória. Assim, conforme um programa executa, a quantidade de memória que ele utiliza aumenta ou diminiu conforme o programa requisita ou libera memória. Sua tarefa é identificar o *valor máximo* de memória que um programa utilizou ao mesmo tempo ao longo sua execução, por exemplo quando rodou no beecrowd!'''

maximo = 0
minimo = 0

while True:
  valor = int(input())
  if valor == 0:
    break
    
  if valor >= maximo or ((valor <= maximo) and valor > 0):
    maximo += valor

  else:
    minimo = valor

print(maximo + minimo)