#João Papo-de-Pescador, homem de bem, comprou um microcomputador
#para controlar o rendimento diário de seu trabalho.
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca
#do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
pp = float(input('Quantos quilos de peixes foram pescados? '))
excesso =  pp-50
multa = excesso*4
print('A quantidade excedente é de {}kg e a multa de acordo com o regulamento é de R${:.2f}'.format(excesso, multa))

