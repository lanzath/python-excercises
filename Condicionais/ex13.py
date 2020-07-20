#ex 13
def semana():
    dia = int(input('Digite um número de 1 a 7: '))
    if dia == 1:
        print('O dia da semana correspondente é Domingo')
    elif dia == 2:
        print('O dia da semana correspondente é Segunda-feira')
    elif dia == 3:
        print('O dia da semana correspondente é Terça-feira')
    elif dia == 4:
        print('O dia da semana correspondente é Quarta-feira')
    elif dia == 5:
        print('O dia da semana correspondente é Quinta-feira')
    elif dia == 6:
        print('O dia da semana correspondente é Sexta-feira')
    elif dia == 7:
        print('O dia da semana correspondente é Sábado')
    else:
        print('Erro! Valor inválido')
        semana()
semana()
