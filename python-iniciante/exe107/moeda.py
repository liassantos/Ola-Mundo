def moeda(x=0, cifra='R$'):
    return f'{cifra}{x:.2f}'.replace('.', ',')


def aumentar(price, n, format=False):
    price = price + (price * (n/100))
    if format:
        return moeda(price)
    else:
        return price

def diminuir(price, n, format=False):
    price = price - (price * (n/100))
    if format:
        return moeda(price)
    else:
        return price

def dobro(price,format=False):
    price *= 2
    if format:
        return moeda(price)
    else:
        return price

def metade(price,format=False):
    price /= 2
    if format:
        return moeda(price)
    else:
        return price


def resumo(price=0, aum=0, red=0):
    title = 'RESUMO DO VALOR'
    print('-'*50)
    print(title.center(50))
    print('-'*50)
    print(f'Preço analisado:      {moeda(price)}')
    print(f'Dobro do Preço:       {dobro(price, True)}')
    print(f'Metade do Preço:      {metade(price, True)}')
    print(f'{aum}% de aumento:       {aumentar(price, aum, True)}')
    print(f'{red}% de redução:       {diminuir(price, red, True)}')
    print('-' * 50)
