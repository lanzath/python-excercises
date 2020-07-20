#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
tc = float(input('Digite o valor de uma temperatura em °C:  '))
tf = (9/5) * tc + 32
print('{}°C ={}°F'.format(tc, tf))
