#Exe82 (Dividindo valores em várias listas)

#recebe vários números e coloca em uma lista
valores = []
resposta = 'S'
while resposta in 'Ss':
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja continuar? \033[30;47m[S/N]\033[m '))
#break point
print('='*50)
#lista que contém todos os valores
print(f'Os valores digitados foram: \033[43m{valores}\033[m')
#listas extras que contém só valores pares ou ímpares
par = []
ímpar = []
for c, v in enumerate(valores):
    if v % 2 == 0:
        par.append(v)
    else:
        ímpar.append(v)
if not par:
    print('Não foram digitados valores pares.')
else:
    print(f'Os valores pares digitados foram: \033[42m{par}\033[m')
if not ímpar:
    print('Não foram digitados valores ímpares.')
else:
    print(f'Os valores ímpares digitados foram: \033[41m{ímpar}\033[m')
#end point
print('='*50)