#o programa lê nome e duas notas do aluno
aluno = []
geral = []
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    geral.append(aluno[:])
    aluno.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print(geral)
#boletim com média
print('='*50)
titulo = 'BOLETIM'
print(titulo.center(50))
print('Nº Nome  Média')
for c, p in enumerate(geral):
    media = (geral[c][1] + geral[c][2])/2
    print(f'{c}  {geral[c][0]} {media}')
print('='*50)
#mostrar notas individuais
while True:
    a = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if a == 999:
        break
    print(f'Notas de {geral[a][0]} são: {geral[a][1:3]}')
