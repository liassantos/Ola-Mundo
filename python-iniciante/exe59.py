#Exe 59 (Menu de Opções)

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
choice = 0
while choice != 5:
  print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] escolher novos números\n[ 5 ] sair do programa\n')
  choice = int(input('>>>>> Qual é a sua opção? '))
  if choice == 1:
    print(f'A soma de {n1} + {n2} é {n1+n2}')
    print('=-='*20)
  elif choice == 2:
    print(f'O produto de {n1} x {n2} é {n1*n2}')
    print('=-='*20)
  elif choice == 3:
    print(f'O maior entre {n1} e {n2} é {max(n1, n2)} ')
    print('=-='*20)
  elif choice == 4:
    n1 = int(input('Primeiro Valor: '))
    n2 = int(input('Segundo Valor: '))
  elif choice == 5:
    print('Finalizando...')
  else:
    print('Valor incorreto. Tente novamente')
print('Fim da Aplicação.')
print('=-='*20)
