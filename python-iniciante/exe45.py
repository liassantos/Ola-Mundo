#GAME - Pedra, Papel, Tesoura

from random import randint
from time import sleep

print('Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
user = int(input('Qual é a sua jogada? '))
lista = ('PEDRA', 'PAPEL', 'TESOURA')
console = randint(0, 2)

if user == 0 or user == 1 or user == 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!')
    print('='*30)
    print(f'Você escolheu {lista[user]}')
    print(f'O computador escolheu {lista[console]}')
    if (user == 0 and console == 2) or (user == 1 and console == 0) or (user == 2 and console == 1):
        print('PARABÉNS! Você ganhou!')
    elif user == console:
        print('EMPATE!')
    else:
        print('Que pena... você perdeu.')
else:
    print('Opção não disponível. Tente novamente.')
print('='*30)