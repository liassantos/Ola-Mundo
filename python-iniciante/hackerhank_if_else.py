n = int(input('Digite um número:'))

rest = n % 2

if rest != 0:
    print('Weird')
if rest == 0 and 2<=n<=5:
    print('Not Weird')
if rest == 0 and 6<=n<=20:
    print('Weird')
if rest == 0 and n>20:
    print('Not Weird')