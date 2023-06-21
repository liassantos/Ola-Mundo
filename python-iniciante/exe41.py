#Exe41 (Classificando atletas)
from datetime import date
birth = int(input('Ano de nascimento: '))
today = date.today().year
age = today - birth

print(f'O atleta tem {age} anos')
if age <= 9:
  print(f'Classificação: MIRIM')
elif 9 < age <= 14:
  print(f'Classificação: INFANTIL')
elif 14 < age <= 19:
  print(f'Classificação: JÚNIOR')
elif 19 < age <= 25:
  print(f'Classificação: SÊNIOR')
else:
  print(f'Classificação: MASTER')