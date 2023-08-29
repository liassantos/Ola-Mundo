from time import sleep
def pyhelptitle():
    print('~'*50)
    print('SISTEMA DE AJUDA PYHELP')
    print('~'*50)

def pyhelpend():
    print('~'*50)
    print(f'Acessando o manual do comando "{nameFunction}"')
    print('~'*50)
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)


while True:
    pyhelptitle()
    nameFunction = input('Função ou Biblioteca > ')
    if nameFunction.upper() in 'FIM':
        print('Sistema Finalizado. ATÉ LOGO!')
        break
    else:
        pyhelpend()
        help(nameFunction)
