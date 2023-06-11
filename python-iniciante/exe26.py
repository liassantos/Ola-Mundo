#transformar tudo em maiúsculo e remover espaços
frase = str(input('Digite uma frase: ')).strip().upper()

#contar
contar = frase.count('A')
print(f'A letra A aparece {contar} vezes na frase.')

#primeira vez que a string aparece
primeiro = frase.find('A')+1
print(f'A primeira letra A apareceu na posição {primeiro}')

#última vez que a string aparece
ultimo = frase.rfind('A')+1
print(f'A última letra A apareceu na posição {ultimo}')