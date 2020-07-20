#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato
#faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
vh = float(input('Quanto você ganha por horas trabalhadas R$ '))
ht = int(input('Total de horas trabalhadas no referido mês: '))
sb = vh*ht
sl = sb - (sb*0.24)
print('+  Salário bruto: R${:.2f}'.format(vh*ht))
print('-   IR (11%): R${:.2f}'.format(sb*0.11))
print('-   INSS (8%): R${:.2f}'.format(sb*0.08))
print('-   Sindicato (5%): R${:.2f}'.format(sb*0.05))
print('=   Salário Líquido: R${:.2f}'.format(sl))
input (' ')
