def leiaInt(num):
    while True:
        msg = input(num)
        if msg.isnumeric() == False:
            print('\033[0;31mERRO! Digite um número válido.\033[m')
        else:
            break
    return msg

#Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
