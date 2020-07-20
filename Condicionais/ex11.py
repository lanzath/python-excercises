def calculo():
    rem = float(input('\nDigite o valor de seu salário: R$'))

    print('\nValor atual R${:.2f}'.format(rem))

    if rem <= 280:
        print('Percentual de aumento: 20%')
        print('Valor do aumento: R${:.2f}'.format(rem*0.2))
        rem = rem + rem * 0.2
        print('Valor atualizado: R${:.2f}'.format(rem))

    elif rem > 280 and rem < 700:
        print('Percentual de aumento: 15%')
        print('Valor do aumento: R${:.2f}'.format(rem*0.15))
        rem = rem + rem * 0.15
        print('Valor atualizado: R${:.2f}'.format(rem))

    elif rem < 1500 and rem >= 700:
        print('Percentual de aumento: 10%')
        print('Valor do aumento: R${:.2f}'.format(rem*0.1))
        rem = rem + rem * 0.1
        print('Valor atualizado: R${:.2f}'.format(rem))

    elif rem >= 1500:
        print('Percentual de aumento: 5%')
        print('Valor do aumento: R${:.2f}'.format(rem*0.05))
        rem = rem + rem * 0.05
        print('Valor atualizado: R${:.2f}'.format(rem))
    again()

def again():
    denovo = input('\nQuer calcular de novo ? S/N ').upper()
    if denovo == 'S':
        calculo()
    elif denovo == 'N':
        print('Fim de cálculo')
    else:
        again()
calculo()
    
