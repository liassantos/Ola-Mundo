#Exe53 (PALÍNDROMOS)

frase = str(input('Digite uma frase: ')).strip()
name1 = ''.join(frase.upper().split())
qtd = len(name1)
name2 = name1[qtd::-1]

print(f'O inverso de {name1} é {name2}')
if name1 == name2:
  print('É um palíndromo!')
else:
  print('Não é um palíndromo!')