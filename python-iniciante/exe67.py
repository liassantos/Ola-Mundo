#Interrupção while
#Exe 67 (tabuada v3.0)

while True:
  n = int(input('Qual tabuada você quer ver? '))
  print('-' * 30)
  if n < 0:
    break
  for c in range (1, 11):
    print(f'{n} x {c} = {n*c}')
  print('-' * 30)
print('FIM DO PROGRAMA...')