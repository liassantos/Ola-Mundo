#Exe39 (Alistamento Militar)
from datetime import date

#o programa lê o ano de nascimento
birth = int(input('Ano de nascimento: '))
today = date.today().year
age = today - birth

print(f'Quem nasceu em {birth} tem {age} anos em 2023.')

#o programa avisa quando tempo falta para se alistar
if age < 18:
  print(f'Ainda faltam {18 - age} anos para o alistamento.')
  print(f'Seu alistamento será em {birth + 18}.')

#o programa avisa que é hora de se alistar
elif age == 18:
  print('Você deve se alistar IMEDIATAMENTE!')

#o programa avisa que já passou o tempo de se alistar
else:
  print(f'Você já deveria ter se alistado há {age - 18} anos.')
  print(f'Seu alistamento foi em {birth + 18}.')