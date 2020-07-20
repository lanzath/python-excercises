#Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = int(input('Digite um número qualquer: '))
n2 = int(input('Digite outro número: '))
n3= int(input('Digite mais um número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

meio = n1
if n2 > n1 and n2 < n3:
    meio = n2
if n3 > n1 and n3 < n2:
    meio = n3

print('A sequência em ordem crescente é: {}, {}, {}'.format(menor, meio, maior))

    
