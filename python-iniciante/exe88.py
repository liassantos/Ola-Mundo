from random import randint
#pergunta quantos jogos serão criados
qtd = int(input('Quantos jogos você quer? '))
geral = []
jogo = []
#sorteia 6 numeros entre 1 e 60
#cadastra cada jogo em uma lista composta
for c in range(0, qtd):
    for n in range(0, 6):
        num = randint(1,60)
        jogo.append(num)
    geral.append(jogo[:])
    jogo.clear()
    geral[c].sort()
    print(f'O {c+1}º jogo: {geral[c]}')






