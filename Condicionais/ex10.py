#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!" conforme o caso.
turno = str(input('Qual é o turno em que você estuda ? Digite M para Matutino, V para Vespertino ou N para Noturno: ')).upper()
if turno == 'M':
    print('Bom dia!')
else:
    if turno == 'V':
        print('Boa tarde!')
    else:
        if turno == 'N':
            print('Boa noite!')
        else:
            print('VALOR INVÁLIDO!')

    
