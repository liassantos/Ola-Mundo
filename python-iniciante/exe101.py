#exe101
#função voto
#parâmetro = ano de nascimento
#retorna valor literal se a pessoa tem voto 'NEGADO', 'OPCIONAL', 'OBRIGATÓRIO'
def voto(year):
    from datetime import date
    currentYear = date.today().year
    ageOfPerson = currentYear - year
    if ageOfPerson < 16:
        return '\33[0;30;41mVOTO NEGADO\033[m'
    elif 16 <= ageOfPerson < 18 or ageOfPerson > 70:
        return '\33[7;49;96mVOTO FACULTATIVO\033[m'
    else:
        return '\33[7;49;92mVOTO OBRIGATÓRIO\033[m'

print('='*50)
title = 'Verifique sua situação eleitoral'
print(title.center(50))
print('='*50)
birthYear = int(input('Digite seu ano de nascimento: '))
print('='*50)
print(f'Sua situação eleitoral: {voto(birthYear)}')
print('='*50)
