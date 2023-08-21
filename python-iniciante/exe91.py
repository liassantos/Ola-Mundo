#4 jogadores jogam um dado e tem resultados aleatórios
#resultados são guardados em um dicionário
#colocar o dicionário em ordem
#o vencedor tira o maior número do dado
from random import randint
from time import sleep

jogadores = dict()
print('VALORES SORTEADOS ')
for c in range(1, 5):
    jogadores[f'Jogador{c}'] = randint(1, 6)
    print(f'    Jogador{c} retirou o número {jogadores[f"Jogador{c}"]}')
    sleep(1)
print('='*50)
print(jogadores)
print('RANKING DE JOGADORES')
for key, value in enumerate(sorted(jogadores, key=jogadores.get, reverse=True)):
    print(f'    {key + 1}° lugar: {value} com {jogadores[value]}')
    sleep(1)
print('='*50)

# CTRL + / -> ADICIONA UM COMENTÁRIO