print('='*40)
print('10 TERMOS DE UMA PA'.center(40))
print('='*40)
a1 = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
c = 0
for c in range(0, 10):
    c = c + 1
    a2 = a1 + (r * c)
    print(a2, end=' -> ')
print('ACABOU')