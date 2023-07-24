#Interrupção while
#Exe 66 (vários números com flag)
c = 0
s = 0
n = 0
while True:
  n = int(input('Digite um número: '))
  c += 1
  if n == 999:
    break
  s += n
print(f'Você digitou {c} números. E a soma entre ele é {s}.')
