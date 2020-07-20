#Faça um Programa que leia três números e mostre o maior deles.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n1 > n2 and n1> n3:
    print('O maior número é ', n1)
else:
    if n2 > n1 and n2 > n3:
        print('O maior número é ', n2)
    else:
        print('O maior número é ', n3)
