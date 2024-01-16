# 1 - Remuneração salarial desigual
'''Dados os dados de uma mulher, cujo salário se sabe ser desigual em relação aos seus pares do gênero masculino na proporção reportada acima, calcule quanto deveria ser salário se ela ganhasse igual a um homem que exerce a mesma função. Seu programa lê uma linha que informa o salario atual (valor decimal). Como saída, o programa imprime o salário que a mulher deveria receber se não houvesse a desigualdade identificada acima (com duas casas decimais).'''

salario = float(input())
salario_desigual = (salario * 0.205) + salario
print('%.2f' % salario_desigual)
