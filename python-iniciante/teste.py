'''palavras = ('[capinha]', '[carregador]', '[pelicula]', '[fone]', '[assistencia]',
    '[vendas]', '[cabo]', '[iphone]', '[sansung]', '[portatil]', '[pulseira]',
    '[suporte]', '[fonte]')
for p in palavras:
    print(f'\n na palavra \033[33m{p}\033[m tem as vogais:',end=' ')
    for letras in p:
        if letras in 'aeiou':
            print(f'\033[34m{letras.lower()}\033[m',end=' ') '''


''' from unidecode import unidecode
lista = ('Gabriel', 'Valentin', 'Francieli', 'Marisa', 'Cezar')
for pos in lista:
    print(f'\n{pos} tem as seguintes vogais: ', end='')
    for letra in pos:
        if (unidecode(letra.lower())) in 'aeiou':
            print(f'{letra}', end=' ') '''

i = 0
for i in range(0, 3):
    print('Meow')
