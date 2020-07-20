#ex. 20
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
media = (n1 + n2 + n3) / 3
if media == 10:
    print('Aprovado com distinção!\nMedia final: {:.2f}'.format(media))
elif media >= 7:
    print('Aprovado \nMedia final: {:.2f}'.format(media))
else:
    print('Reprovado \nMedia final: {:.2f}'.format(media))
