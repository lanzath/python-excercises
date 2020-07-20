#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
l = int(input('Digite a medida de um dos lados do quadrado: '))
print('A área deste quadrado vale {} e o dobro deste valor é {}'.format(l**2, pow(l, 2)*2))
