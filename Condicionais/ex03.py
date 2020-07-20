#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

#Atribuição e transformação para Maiúscula
letra = str(input('Digite o gênero do cliente: ')).upper()

#Condicional para teste
if letra == 'F':
    print('Feminino')

else:
  if letra == 'M':
      print('Masculino')
  else:
      print('Sexo inválido')
