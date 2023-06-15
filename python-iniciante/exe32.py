#Exe32 (Ano Bissexto)
import datetime

#o programa lê o ano que o usuário escolher
year = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if year==0:
  today = datetime.datetime.now()
  date = today.date()
  year_actual = date.year
  if year_actual % 4 == 0 and year_actual % 100 != 0 or  year_actual % 400 == 0:
    print(f'O ano {year_actual} é BISSEXTO')
  else:
    print(f'O ano {year_actual} NÃO é BISSEXTO')

if year!=0:
  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'O ano {year} é BISSEXTO')
  else:
    print(f'O ano {year} NÃO é BISSEXTO')