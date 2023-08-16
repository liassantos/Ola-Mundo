#programa lê nome e peso de várias pessoas e guarda em uma lista
dados = []
geral = []
peso = []
pesado = []
leve = []
qtd = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso (Kg): ')))
    qtd += 1
    geral.append(dados[:])
    dados.clear()
    resp = input('Deseja adicionar mais? \033[30;47m[S/N]\33[m ')
    if resp in 'Nn':
        break
#para saber o maior e menor peso
for p in geral:
    peso.append(p[1])
menor = min(peso)
maior = max(peso)
#para saber o nome da pessoa correspondente ao maior e menor peso
for p in geral:
    if p[1] == maior:
        pesado.append(p[0])
    if p[1] == menor:
        leve.append(p[0])
#mostra os dados coletados
print('='*50)
print(f'\033[30;43mDados Coletados:\33[m\n{geral}')
print('='*50)
#mostra quantas pessoas cadastradas
print(f'\033[30;43mTotal de Pessoas:\33[m {qtd}')
print('='*50)
#lista das pessoas mais pesadas e peso
print(f'\033[30;43mPessoas mais Pesadas:\33[m {pesado}\n\033[30;42mPeso:\33[m {maior} Kg')
print('='*50)
#lista das pessoas mais leves e peso
print(f'\033[30;43mPessoas mais Leves:\33[m {leve}\n\033[30;42mPeso:\33[m {menor} Kg')
print('='*50)