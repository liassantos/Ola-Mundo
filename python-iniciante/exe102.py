def fatorial(num, show=False):
    """
    Função para calcular o fatorial de um número
    :param num: o número a ser calculado o fatorial
    :param show: é opcional, mostra o processo do cálculo do fatorial
    :return: o cálculo do fatorial do valor num
    """
    fatorialResult = 1
    for counter in range(num, 0, -1):
        fatorialResult *= counter
        if show and counter > 1:
            print(f'{counter} x', end=' ')
        if show and counter == 1:
            print(f'{counter} =', end=' ')
    return fatorialResult


print(fatorial(7, 1))