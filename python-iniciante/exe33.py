#Exe33 (Maior e menor valor) - MINHA RESOLUÇÃO

#o programa lê três númmeros escolhidos pelo usuário
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
n3 = int(input('Terceiro Valor: '))

#o programa retorna o menor e o maior valor digitado

list = n1, n2, n3

print(f'O menor valor digitado foi {min(list)}')
print(f'O maior valor digitado foi {max(list)}')