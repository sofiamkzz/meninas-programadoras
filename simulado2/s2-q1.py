# 1 - Desmatamento na Amazônia
'''Em 2022, a Amazonia perdeu 10267 km² com desmatamento. Esse resultado representa um aumento de 11,3% na área com alertas de desmatamento, na comparação com 2021. É a pior marca desde o início do monitoramento, em 2015. Com base nessas informações, podemos utilizar uma regra de três simples para estimar a área desmatada na Amazônia em 2021. O seu programa deverá receber como entrada a quantidade de área desmatada na Amazônia em determinado ano (em km²) e a taxa de desmatamento em relação ao ano anterior (em porcentagem). Com base nesses dados, o programa deverá calcular e exibir qual foi a área desmatada no ano anterior (use uma casa decimal).'''

area_desmatada = int(input())
taxa_desmatamento = float(input())
calculo_area = area_desmatada / (1 + taxa_desmatamento / 100)
print('%.1f' % calculo_area)
