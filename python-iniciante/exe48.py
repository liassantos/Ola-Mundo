#Exe48 (Soma de ímpares múltiplos de 3)
n = 0
for c in range (0, 500, 3):
  if c % 2 != 0:
    n += c
print(n)