#Exe36 (Empréstimo Bancário)

value_house = float(input('Valor da Casa: '))
salary = float(input('Salário do Comprador: '))
years_pay = int(input('Em quantos anos vai pagar: '))
monthly = value_house/(years_pay * 12)
print(f'Para pagar uma casa de R${value_house:.2f} em {years_pay} anos, a prestação será de R${monthly:.2f}')
if monthly <= salary * 0.3:
  print('O empréstimo pode ser CONCEDIDO!')
else:
  print('O empréstimo foi NEGADO!')