#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
h = float(input('Qual é a sua altura? '))
print('A massa ideal para sua altura se você é homem é de {:.1f}kg'.format((72.7*h)-58))
print('A massa ideal para sua altura se você é mulher é de {:.1f}kg'.format((62.1*h)-44.7))
