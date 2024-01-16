#19	- Joaninha: tromba mas não cai
'''Quando a Joaninha é ligada, o programa captura da bateria um valor inteiro entre 0 e 100, correspondente à porcentagem de carga disponível. Ademais, a Joaninha só funciona com carga mínima maior que 5%. Antes de cada movimento, o programa obtém informações de dois sensores. O primeiro sensor informa B de bateu ou L se a área livre à frente. O segundo sensor informa A se tem um Abismo, ou P se há Piso para avançar.
Para controlar a Joaninha, seu programa emite os comandos virar, em caso de necessidade, ou avançar, sempre que possível. Quando não há bateria disponível para trabalhar, seu programa avisa que é hora de recarregar.  Junto com cada comando, seu sempre programa informa o quanto de bateria resta na Joaninha.
Entrada: primeira linha: um valor inteiro entre 0 e 100, a seguir, um número indeterminado de pares de linhas com uma letra cada: o primeiro valor do par contém B ou L e o segundo valor do par contém A ou P'''

carga_bateria = int(input())

while carga_bateria > 5:
  primeiro_sensor = input()
  segundo_sensor = input()

  if primeiro_sensor == 'B' or segundo_sensor == 'A':
    carga_bateria -= 5
    print('virar:', carga_bateria)

  elif primeiro_sensor == 'L' or segundo_sensor == 'P':
      carga_bateria -= 1
      print('avançar:', carga_bateria)

print('recarregar:', carga_bateria)