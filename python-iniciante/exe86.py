#o programa cria uma matriz 3x3 e preenche com valores lidos pelo teclado
matriz = [[[ ], [ ], [ ]], [[ ], [ ], [ ]], [[ ], [ ], [ ]]]
valor = 0
c = 0
for c in range (0, 3):
    valor = int(input(f'Digite o valor da posição [0, {c}]: '))
    matriz[0][c].append(valor)
for c in range (0, 3):
    valor = int(input(f'Digite o valor da posição [1, {c}]: '))
    matriz[1][c].append(valor)
for c in range(0, 3):
    valor = int(input(f'Digite o valor da posição [2, {c}]: '))
    matriz[2][c].append(valor)

#Apresentação da matriz
print("="*30)
titulo = '\33[43mA MATRIZ GERADA\33[m'
print(titulo.center(40))
print(' '*9, matriz[0][0], matriz[0][1], matriz[0][2])
print(' '*9, matriz[1][0], matriz[1][1], matriz[1][2])
print(' '*9, matriz[2][0], matriz[2][1], matriz[2][2])
print("="*30)