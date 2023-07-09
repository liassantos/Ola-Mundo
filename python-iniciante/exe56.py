#Exe 56 (Analisador Completo)
mulheres = 0
soma = 0
maior = 0
hvelho = ''
for c in range (1, 5):
    print('=' * 10 + ' ' + f'{c}ª PESSOA' + ' ' + '=' * 10)
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    soma = age + soma
    media = soma / c
    sex = str(input('Sexo [M/F]: '))
    if sex == 'F':
        if age < 20:
            mulheres = mulheres + 1
    if sex == 'M' and c == 1:
        maior = age
        hvelho = name
    if sex == 'M' and age > maior:
        maior = age
        hvelho = name
print(f'A média de idade do grupo é de {media} anos')
print(f'Ao todo são {mulheres} mulheres com menos de 20 anos.')
print(f'O homem mais velho tem {maior} anos e se chama {hvelho}.')
