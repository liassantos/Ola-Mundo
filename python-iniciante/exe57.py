#Exe 57 (Validação de Dados)
sex = str(input('Informe seu sexo: [M/F]')).upper().strip()[0]
while sex not in 'MF':
  sex = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper().strip()[0]
print(f'Sexo {sex} registrado com sucesso')