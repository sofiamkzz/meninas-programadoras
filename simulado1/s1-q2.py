# 2 - Desigualdade maior quando a qualificação é maior
'''Dados os dados de uma mulher, concluinte de graduação ou pós-graduação, cujo salário se sabe ser desigual em relação aos seus pares do gênero masculino na proporção reportada acima, calcule quanto deveria ser salário se ela ganhasse igual a um homem que exerce a mesma função. Seu programa lê duas linhas: a primeira informa se a profissional possui graduação (G) ou pós-graduação (PG); a segunda informa seu salario atual com um valor inteiro. Como saída, o programa imprime o salário que a mulher deveria receber se não houvesse a desigualdade identificada acima. Lembrete: para imprimir o valor de xis com duas casas decimais, podemos utilizar print('%.2f' % xis)'''

conclusao = input()
salario_atual = int(input())

if conclusao == 'G':
  salario_g = (salario_atual * 0.38) + salario_atual
  print('%.2f' % salario_g)
elif conclusao == 'PG':
  salario_pg = (salario_atual * 0.43) + salario_atual
  print('%.2f' % salario_pg)