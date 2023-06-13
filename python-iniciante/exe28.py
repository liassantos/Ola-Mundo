#Exe28 (Jogo da Advinhação)

#computador escolhe um número inteiro entre 1 e 5
import random
number_rand = random.randint(1,5)

#usuário tenta advinhar
number_user = int(input('Advinhe o número: '))

#o programa indica se o usuário acertou ou errou
if number_user == number_rand:
  print('Você acertou! Parabéns!')
else:
  print('Que pena, você errou... Tente outra vez.')