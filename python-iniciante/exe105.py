def notas(*grade, sit=False):
    countGrade = len(grade)
    highGrade = max(grade)
    lowGrade = min(grade)
    avgGrade = sum(grade)/countGrade
    if sit:
        if avgGrade <= 5:
            sit = 'RUIM'
        elif avgGrade >= 7:
            sit = 'ÓTIMO'
        else:
            sit = 'REGULAR'
        info = {'Total de Notas': countGrade, 'Maior Nota': highGrade,
            'Menor Nota': lowGrade, 'Média': avgGrade, 'Situação': sit}
    else:
        info = {'Total de Notas': countGrade, 'Maior Nota': highGrade,
                'Menor Nota': lowGrade, 'Média': avgGrade}
    return info
#Programa Principal
resposta = notas(10, 5.5, 10, 10, sit=True)
print(resposta)