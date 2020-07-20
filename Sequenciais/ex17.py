#Faça um Programa para uma loja de tintas.
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
#a tinta é vendida em latas de 18 litros, que custam R$ 80,00
#ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

from math import ceil
area = float(input('Digite a área a ser pintada: '))
qtdtinta = area/6 #cada 1 litro de tinta pinta 6m²
latas = qtdtinta/18 #numero de latas necessarias
galão = qtdtinta/3.6 #numero de galões necessários
print('Pra pintar {}m² você vai precisar de {} litros de tinta '.format(area, qtdtinta))
print('Você pode comprar {} galões por R${:.2f} ou {} latas por R${:.2f}'.format(ceil(galão), galão*25, ceil(latas), latas*80))
latas = qtdtinta // 18
galão = (qtdtinta % 18)/3.6
print('Você pode comprar {} latas e {} galões por R${:.2f}'.format(latas, round(galão + 0.5), (round(galão+0.5)*25) + (latas*80)))

      
