#Faça um Programa que peça dois números e imprima o maior deles.

#Atribuição das strings para as variáveis
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

#Mostra o maior número
print('O maior número é ', n1 if n1>n2 else n2)
