def calcule(msg):
    lista = msg.upper().split()
    if 'V' in lista:
        d = int(lista[2])
        t = int(lista[4])
        v = d / t
        print(f'V = {v}')
    if 'D' in lista:
        v = int(lista[0])
        t = int(lista[4])
        d = v * t
        print(f'D = {d}')
    if 'T' in lista:
        v = int(lista[0])
        d = int(lista[2])
        t = d / v
        print(f'T = {t}')


choice = str(input('O que você quer que eu calcule? \nUtilize o formato [V = D / T] -> ' ))
calcule(choice)
