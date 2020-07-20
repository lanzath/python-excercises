#ex. 15
l1 = int(input('Digite o comprimento do lado 1: '))
l2 = int(input('Digite o comprimento do lado 2: '))
l3 = int(input('Digite o comprimento do lado 3: '))
 
if l1+l2 < l3 or l1+l3 < l2 or l2+l3 < l1:
    print('Não é possível formar triângulo nessa porra!')
elif l1 == l2 and l1 == l3 and l2 == l3:
    print('Triângulo Equilátero!')
elif l1 == l2 or l2 == l3 or l1 == l3:
    print('Triângulo Isósceles!')
else:
    print('Triângulo Escaleno!')
