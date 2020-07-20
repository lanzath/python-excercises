#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
vh = float(input('Quanto você ganhar por hora trabalhada? R$'))
ht = int(input('Quantas horas você trabalhou neste mês? '))
print('Seu salário bruto no mês referido é de R${:.2f}'.format(vh*ht))
