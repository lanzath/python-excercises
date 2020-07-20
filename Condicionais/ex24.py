#ex 24
def analise():
    num1 = float(input('Digite um Número: '))
    num2 = float(input('Digite outro número: '))
    op = input('Escolha uma das operações abaixo: \na. par ou ímpar;\nb. positivo ou negativo\nc. inteiro ou decimal\n').lower()
    if op == 'a':
        if num1 % 2 == 0 and num2 % 2 == 0:
            print(num1,'e', num2, 'São pares')
        elif num1 % 2 == 0 and num2 % 2 != 0:
            print(num1, 'é par e', num2, 'é ímpar')
        elif num1 % 2 != 0 and num2 % 2 == 0:
            print(num1, 'é ímpar e', num2, 'é par')
        else:
            print(num1,'e', num2, 'São ímpares')
    elif op == 'b':
        if num1 >= 0 and num2 >= 0:
            print(num1, num2, 'São positivos')
        elif num1 >= 0 and num2 < 0:
            print(num1, 'é positivo e', num2, 'é negativo')
        elif num1 < 0 and num2 >= 0:
            print(num1, 'é negativo e', num2, 'é positivo')
        else:
            print(num1, 'e', num2, 'são Negativos')
    elif op == 'c':
        if num1 == round(num1) and num2 == round(num2):
            print(num1, 'e', num2, 'São inteiros')
        elif num1 != round(num1) and num2 == round(num2):
            print(num1, 'é decimal e', num2, 'é inteiro')
        elif num1 == round(num1) and num2 != round(num2):
            print(num1, 'é inteiro e', num2, 'é decimal')
        else:
            print(num1, 'e', num2, 'são decimais')
    else:
        print('Operação inválida')
    outro()   
def outro():
    novo = input('Fazer nova análise? S/N \n').lower()
    if novo == 's':
        analise()
    elif novo == 'n':
        print('Fim de execução')
    else:
        outro()
analise()
