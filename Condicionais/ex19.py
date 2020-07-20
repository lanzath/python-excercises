#ex 19
n1 = int(input('Digite um número inteiro de 1 a 1000: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
print('{}, centena: {}, dezena: {}, unidade: {}'.format(n1, c, d, u))
