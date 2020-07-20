#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
tf = float(input('Digite uma temperatura em °F: '))
tc = (5*(tf-32))/9
print('{}°F = {:.1f}°C'.format(tf, tc))
