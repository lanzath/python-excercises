#ex 23
num = float(input('Digite um número qualquer: '))
if num == round(num):
    print('Número inteiro')
else:
    print('Número decimal')
    print("Arredondado pra baixo: ", round(num-0.5) )
    print("Arredondado pra cima : ", round(num+0.5) )
    
