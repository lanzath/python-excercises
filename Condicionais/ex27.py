#ex 27
morango = int(input('Qual a quantidade de morangos? '))
maçã = int(input('Qual a quantidade de maçãs? '))
if maçã <= 5 and morango <= 5:
    valor_morango = morango * 2.5
    valor_maçã = maçã * 1.8
    total = valor_maçã + valor_morango
elif maçã > 5 and morango > 5:
    valor_morango = morango * 2.5
    valor_maçã = maçã * 1.8
    total = valor_maçã + valor_morango
if total >= 25:
    total = total - (total*0.1)
print('R$ {} de maçãs e R${} de morangos\nTotal a pagar: R$ {:.2f}'.format(valor_maçã, valor_morango, total))
