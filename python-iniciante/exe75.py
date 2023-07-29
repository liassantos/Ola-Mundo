#Tuplas
#Exe75 ----- faltam umas correções

# 4 valores digitados e armazena em uma tupla
valores = tuple(int(input(f'Digite o {c}º valor: '))for c in range(1, 5))

#tupla = (n1, n2, n3, n4)
print(f'Você digitou os valores {valores}')

# quantas vezes apareceu o 9
if 9 in valores:
    print(f'O valor 9 apareceu {valores.count(9)} vezes.')
else:
    print(f'O valor 9 não apareceu nenhuma vez')

# em que posição foi digitado o primeiro valor 3
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição.')
else:
    print(f'O valor 3 não apareceu nenhuma vez')

# quais foram os numeros pares
print('Os valores pares digitados foram:', end=" ")
for n in valores:
  if n % 2 == 0:
    print(n, end=" ")
