#Tuplas
#Exe76 (Lista de Produtos)

# listagem de produto e preço
lista = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)

#cabeçalho
titulo = 'LISTAGEM DE PRODUTOS'
print('-' * 40)
print(titulo.center(40))
print('-' * 40)

#produtos em forma de lista
for pos in range(0, len(lista), 2):
    print(f'{lista[pos]:.<30}', end=" ")
    print(f'R$ {lista[pos+1]}')

#rodapé
print('-' * 40)