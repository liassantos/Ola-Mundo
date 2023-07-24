x = int(input('Digite um número: '))

for c in range(1, x + 1):
    print(c, end=' ')
    if x % c != 0:
        print(f'{x} é um número primo.')
    else:
        print(f'{x} não é um número primo.')
