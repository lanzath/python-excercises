#ex25
cont = 0
tel = input('Telefonou para a vítima? ')
local = input('Esteve no local do crime? ')
perto = input('Mora perto da vítima? ')
devia = input('Devia para a vítima? ')
trabalho = input('Já trabalhou com a vítima ')
if tel == 'sim':
    cont = cont + 1
if local == 'sim':
    cont = cont + 1
if perto == 'sim':
    cont = cont + 1
if devia == 'sim':
    cont = cont + 1
if trabalho == 'sim':
    cont = cont + 1
if cont == 2:
    print('Suspeita')
elif cont in range(3, 4):
    print('Cúmplice')
elif cont == 5:
    print('Assassino')
else:
    print('Inocente')
