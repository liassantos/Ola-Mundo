#Exe58 (Jogo da Advinhação 2.0)
from time import sleep
from random import randint
import pygame
from pygame.locals import *

musica_efeito_texto = pygame.mixer.music.load('depositphotos_424865256-track-computer-beep-sound-effect.mp3')

print('Sou seu computador...')
sleep(1.3)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(1.3)
print('Será que você consegue advinhar qual foi?')
sleep(1.3)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
pc = randint(0, 10)
user = int(input('Qual é o seu palpite? '))
count = 1
while user != pc:
  if user < pc:
    print('Mais... Tente mais uma vez.')
    user = int(input('Qual é o seu palpite? '))
  if user > pc:
    print('Menos... Tente mais uma vez.')
    user = int(input('Qual é o seu palpite? '))
  count = count + 1
print(f'Acertou com {count} tentativas. Parabéns!')