#Faça um programa para uma loja de tintas.
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
#e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
from math import ceil
area = int(input('Qual é a área da parede a ser pintada? '))
qtdl = area/3
lata = qtdl/18
print('Você vai precisar de {} litros de tinta para pintar {}m²'.format(qtdl, area))
print('Será(ão) necessária(s) {} latas de tintas e custará R${:.2f}'.format(ceil(lata), lata*80))
input (' ')
