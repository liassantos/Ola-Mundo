def ficha(name='<desconhecido>', gol=0):
    """
    :param nome: string
    :param gol: intenger
    :return: função retorna a ficha do jogador
    """
    print(f'O jogador {name} fez {gol} gol(s) no campeonato.')


playerName = str(input('Nome do jogador: '))
playerGols = str(input('Quantos gols o jogador fez? '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if playerName.strip() == '':
    ficha(gol=playerGols)
else:
    ficha(playerName, playerGols)
