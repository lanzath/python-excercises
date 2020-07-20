#ex 12.
def folha():

    ht = int(input('\nQuantidade de horas trabalhadas: '))
    vh = float(input('Valor da hora trabalhada: R$ '))

    sb = vh * ht
    
    print('\nSalário Bruto ({} x {})    :R$ {:.2f}'.format(ht, vh, sb))
    print('FGTS (11%)                   :R$ {:.2f}'.format(sb*0.11))
    print('(-) INSS (10%)               :R$ {:.2f}'.format(sb*0.1))
    
    if sb <= 900:
        print('(-) IR (ISENTO)              :R$ 0.00')
        print('Total de descontos           :R$ {:.2f}'.format(sb*0.1))
        print('Salário líquido              :R$ {:.2f}'.format(sb-(0.21*sb)))
    elif sb > 900 and sb <= 1500:
        print('(-) IR (5%)                  :R$ {:.2f}'.format(sb*0.05))
        print('Total de descontos           :R$ {:.2f}'.format(sb*0.15))
        print('Salário líquido              :R$ {:.2f}'.format(sb-(0.15*sb)))
    elif sb > 1500 and sb <= 2500:
        print('(-) IR (10%)                 :R$ {:.2f}'.format(sb*0.1))
        print('Total de descontos           :R$ {:.2f}'.format(sb*0.2))
        print('Salário líquido              :R$ {:.2f}'.format(sb-(0.2*sb)))
    elif sb > 2500:
        print('(-) IR (20%)                 :R$ {:.2f}'.format(sb*0.2))
        print('Total de descontos           :R$ {:.2f}'.format(sb*0.3))
        print('Salário líquido              :R$ {:.2f}'.format(sb-(0.3*sb)))

    outro()

def outro():
    repete = input('\nFazer um novo cálculo? S/N  ').upper()
    if repete == 'S':
        folha()
    elif repete == 'N':
        print('FIM DO CÁLCULO')
    else:
        outro()
folha()
