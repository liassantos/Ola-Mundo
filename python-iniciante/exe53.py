#Exe 53 (Grupo da Maioridade)
from datetime import date
atual = date.today().year
adult = 0
young = 0
for cont_people in range (1, 8):
    person = int(input(f'Em que ano a {cont_people}º pessoa nasceu? '))
    if atual - person >= 18:
       adult += 1
    else:
       young += 1
print(f'Tem {adult} adultos')
print(f'Tem {young} pessoas menores de idade')

