#ex. 16
def bhaskara():
    a = int(input('Digite o coeficiente a de uma equação quadrática: '))

    if a == 0:
        print('Se a = 0 então não temos uma eq. quadrática.')

    else:
        b = int(input('Digite o coeficiente b de uma equação quadrática: '))
        c = int(input('Digite o coeficiente c de uma equação quadrática: '))

        delta = (b**2)-(4*a*c)
        x1 = (-b + pow(delta, 0.5)) / (2 * a)
        x2 = (-b - pow(delta, 0.5)) / (2 * a)
        
        if a != 0 and delta < 0:
            print('Não há solução real para a equação.')
        elif a != 0 and delta == 0:
            print('A equação possui apenas uma raíz real x = {:.2f}'.format(-b/(2*a)))
        elif a != 0 and delta > 0:
            print('A equação possui duas raízes: x1 = {:.2f} e x2 = {:.2f}'.format(x1, x2))

        outro()
def outro():
    again = input('Quer calcular de novo?  S/N \n').upper()
    if again == 'S':
        bhaskara()
    elif again == 'N':
        print('Fim do programa.')
    else:
        outro()
bhaskara()
