#ex 14
n1 = float(input('Digite a Nota 1: '))
n2 = float(input('Digite a nota 2: '))
media = (n1 + n2)/2
print('Média', 'Conceito', sep='   ')
if media > 9 and media <= 10:
    print('{:.1f}'.format(media), 'A', sep='      ')
elif media > 7.5 and media <= 9:
    print('{:.1f}'.format(media), 'B', sep='      ')
elif media > 6 and media <= 7.5:
    print('{:.1f}'.format(media), 'C', sep='      ')
elif media > 4 and media <= 6:
    print('{:.1f}'.format(media), 'D', sep='      ')
elif media > 0 and media <= 4:
    print('{:.1f}'.format(media), 'E', sep='      ')
