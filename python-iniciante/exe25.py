name = str(input('Qual é o seu nome completo?' )).strip()

#Verificar se contém o nome 'SILVA'
verify = 'SILVA' in name.upper()

print(f'Seu nome tem Silva? {verify}')