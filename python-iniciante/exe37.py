#Exe37 (Conversor de bases numéricas)

n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] Converter para BINÁRIO \n[ 2 ] Converter para OCTAL \n[ 3 ] Converter para HEXADECIMAL')
option = int(input('Sua opção: '))
if option == 1:
  print(bin(n)[2:])
elif option == 2:
  print(oct(n)[2:])
elif option ==3:
  print(hex(n)[2:])
else:
  print('Opção inválida. Tente novamente.')