#ex 17
ano = int(input('Digite um ano: '))

if ano >= 1582:
    if ano % 4 == 0 and ano % 100 != 0:
        print('Ano {} é bissexto'.format(ano))

    elif ano % 400 == 0 and ano % 100 !=0:
        print('Ano {} é bissexto'.format(ano))

    else:
        print('Ano {} não é bissexto'.format(ano))

else:
    print('Ano do calendário Juliano, o calendário Gregoriano passou a valer a partir de 1582')
    
