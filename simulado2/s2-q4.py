# 4 - Sempre na luta pelo meio ambiente
'''Com o aumento da rede de monitoramento, a quantidade de observações também cresce a cada dia. Considerando o valor da pior estimativa e um conjunto de valores informados pelas agências de monitoramento, seu programa deve verificar a quantidade total de observações e quantas delas foram inferiores à pior estimativa. Para isso, seu programa deve ler um número qualquer de observações, sendo que o final das observações será indicado por um valor negativo.'''

pior_estimativa = float(input())
total_observacoes = 0
contador_inferiores = 0

while True:
  taxas = float(input())

  if taxas < 0:
    break
  
  if taxas < pior_estimativa:
    contador_inferiores += 1
    
  total_observacoes += 1

print('{} {}'.format(total_observacoes, contador_inferiores))