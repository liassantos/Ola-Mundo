#nome, ano de nascimento, ctps, idade
from datetime import date
cadastro = {}
cadastro['Nome'] = str(input('Nome do Funcionário: '))
cadastro['Ano'] = int(input('Ano de Nascimento: '))
cadastro['Idade'] = date.today().year - cadastro['Ano']
cadastro['CTPS'] = int(input('Número da CTPS (0 se não possui): '))
#se a CTPS for diferente de ZERO, o dicionário receberá também
# o ano de contratação e o salário. Calcule e acrescente,
# além da idade, com quantos anos a pessoa vai se aposentar.
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = float(input('Salário: R$ '))
    cadastro['Aposentadoria'] = ((cadastro['Contratação'] + 35) - cadastro['Ano'])
print('='*50)
print('DADOS DO FUNCIONÁRIO')
for key, value in cadastro.items():
    if key == 'Salário':
        print(f'{key}: R$ {value:.2f}')
    elif key == 'Idade' or key == 'Aposentadoria':
        print(f'{key}: {value} anos')
    else:
        print(f'{key}: {value}')
print('='*50)
