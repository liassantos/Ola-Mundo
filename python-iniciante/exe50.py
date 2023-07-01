#Exe50 (Soma de números pares)
soma = 0
cont = 0
for n in range (0, 6):
  n = int(input('Digite um número: '))
  if n % 2 == 0:
    soma = n + soma
    cont = cont + 1
print(f'A soma dos {cont} números inteiros pares é {soma}')