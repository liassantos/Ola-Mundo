#Exe34 (Aumentos Múltiplos)

#o programa recebe o valor do salário do funcionário
salary = float(input('Qual é o salário do funcionário? R$'))

#acima de 1250, aumenta 10%
#abaixo ou igual a 1250, aumento de 15%

if salary > 1250:
  new_salary = salary + (salary*0.1)
else:
  new_salary = salary + (salary*0.15)

print(f'Quem ganhava R${salary:.2f} passa a ganhar R${new_salary:.2f} agora.')