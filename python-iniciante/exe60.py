#Exe 60 (Cálculo do Fatorial)
from math import factorial

n = int(input('Choose a number to calculate its factorial: '))
count = n
fact = 1
print(f'Calculating {n}! =', end = ' ')
while count > 0 :
  count = count - 1
  fact = fact * count
  print(f'x {count}', end = ' ')
print (f'= {fact}')