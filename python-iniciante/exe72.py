#Exe72 (Número por extenso)
n = int(input('Escolha um número de 0 a 20: '))
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while n < 0 or n > 20:
  n = int(input('Tente Novamente. Escolha um número de 0 a 20: '))
print(f'O número {n} por extenso é {tupla[n]}')