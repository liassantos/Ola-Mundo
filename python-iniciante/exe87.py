#aprimorar o exe86 mostrando
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
col = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input('Digite um número: '))
        for c, num in enumerate(matriz[l]):
            if c == 2:
                col += num
    for num in matriz[l]:
        if num % 2 == 0:
            soma += num

#matriz
print("="*50)
print('\33[43mA MATRIZ GERADA\33[m')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end=' ')
    print()
print()
#a soma de todos os valores pares digitados
print(f'A soma dos pares foi: {soma}')
#a soma dos valores da terceira coluna
print(f'A soma dos valores da terceira coluna foi: {col}')
#o maior valor da segunda linha
maior = max(matriz[1])
print(f'O maior valor da segunda linha foi: {maior}')
print("="*50)