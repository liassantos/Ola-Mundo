#Exe30 (Par ou Ímpar)

#o programa lê um número inteiro
number = int(input('Digite um número: '))

#informa se é par ou impar
resto = number % 2
if resto == 0:
  print('É par!')
else:
  print('É ímpar!')