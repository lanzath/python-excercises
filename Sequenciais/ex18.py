Arquivo = float(input('Qual é o tamanho do arquivo (MB) ? '))
Link = float(input('Qual é a velocidade de sua internet (mbps) ? '))
tempo = Arquivo/Link
print('O tempo aproximado de download é de {:.2f} minutos '.format(tempo*60))
