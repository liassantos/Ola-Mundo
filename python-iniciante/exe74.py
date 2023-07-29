#Tuplas
#Exe74

# gera 5 valores aleatórios

from random import randint

x1 = randint(1, 10)
x2 = randint(1, 10)
x3 = randint(1, 10)
x4 = randint(1, 10)
x5 = randint(1, 10)

# coloca em tupla

tupla = (x1, x2, x3, x4, x5)

# printa os valores

print(f'Os valores gerados foram: {tupla}')

# indica o maior valor

print(f'O maior valor é {max(tupla)}')

# indica o menor valor

print(f'O menor valor é {min(tupla)}')