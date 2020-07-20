#ex 26
litros = int(input('Qtd de litros a ser abastecido: '))
Combustível = str(input('Escolha E-Etanol ou G- Gasolina: \n')).upper()
if Combustível == 'E':
    if litros <= 20:
        desconto = (1.9 * litros * 0.03)
        valor = (1.9 * litros) - desconto
        print('Total em litros {}, Total a pagar: R$ {:.2f}\nDesconto: R$ {:.2f}'.format(litros, valor, desconto))
    elif litros > 20:
        desconto = (1.9 * litros * 0.05)
        valor = (1.9 * litros) - desconto
        print('Total em litros {}, Total a pagar: R$ {:.2f}\nDesconto: R$ {:.2f}'.format(litros, valor, desconto))
elif Combustível == 'G':
    if litros <= 20:
        desconto = (2.5 * litros * 0.04)
        valor = (1.9 * litros) - desconto
        print('Total em litros {}, Total a pagar: R$ {:.2f}\nDesconto: R$ {:.2f}'.format(litros, valor, desconto))
    elif litros > 20:
        desconto = (2.5 * litros * 0.06)
        valor = (2.5 * litros) - desconto
        print('Total em litros {}, Total a pagar: R$ {:.2f}\nDesconto: R$ {:.2f}'.format(litros, valor, desconto))
