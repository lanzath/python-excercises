#ex. 21
saque = int(input('Informe o valor de Saque: R$ '))
print('Saque autorizado: R$ ', saque)
if saque in range (10, 600):
    nota_cem = saque // 100
    saque = saque % 100

    nota_cinq = saque // 50
    saque = saque % 50

    nota_dez = saque // 10
    saque = saque % 10

    nota_cinc = saque // 5
    saque = saque % 5

    nota_um = saque // 1
    saque = saque % 1
    
    if nota_cem > 0:
        print(nota_cem, 'Notas de R$100')
    if nota_cinq > 0:
        print(nota_cinq, 'Notas de R$50')
    if nota_dez > 0:
        print(nota_dez, 'Notas de R$10')
    if nota_cinc > 0:
        print(nota_cinc, 'Notas de R$5')
    if nota_um > 0:
        print(nota_um, 'Notas de R$1')
else:
    print('Valor indisponível')
