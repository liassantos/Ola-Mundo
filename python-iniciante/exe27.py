#'Digite seu nome completo: '
nome = str(input('Digite seu nome completo: ')).strip().title()

#'Muito prazer em te conhecer!'
print('Muito prazer em te conhecer!')

#'Seu primeiro nome é {}'
print(f'Seu primeiro nome é {nome.split()[0]}')

#'Seu último nome é {}'
print(f'Seu último nome é {nome.split()[-1]}')