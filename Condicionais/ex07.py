#Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

maior = n1
if maior < n2:
    maior = n2
if maior < n2:
    maior = n3
print ('O maior número é: ', maior)

menor = n1
if menor > n2:
    menor = n2
if menor > n3:
    menor = n3
print ('O menor número é: ', menor)

