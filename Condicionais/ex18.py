#ex18
dd = int(input('Digite um dia: '))
mm = int(input('Digite um mês: '))
aa = int(input('Digite um ano: '))
if mm == 2:
    if dd in range (1, 29):
        print('Data digitada: {}/{}/{}'.format(dd,mm,aa))
    else:
        print('Data inválida')
elif mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
    if dd in range (1, 31):
        print('Data digitada: {}/{}/{}'.format(dd,mm,aa))
    else:
        print('Data inválida')
elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
    if dd in range (1, 30):
        print('Data digitada: {}/{}/{}'.format(dd,mm,aa))
    else:
        print('Data inválida')
