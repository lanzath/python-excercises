#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = float(input('Digite um número real: '))
print('O produto do dobro de {} com a metade de {} vale: {}'.format(n1, n2, (n1*2)*(n2/2)))
print('A soma do triplo de {} com o {} vale: {:.2f}'.format(n1, n3, (n1*3)+n3))
print('({})³={}'.format(n3, pow(n3, 3)))
input ('Pressione <enter> para continuar')
