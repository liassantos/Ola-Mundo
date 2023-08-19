#lê o nome, média e situação (>= 7 aprovado) + guarda no dicionário
n = str(input('Digite o nome do aluno: '))
m = float(input(f'Digite a média de {n}: '))
if m >= 7:
    s = 'Aprovado'
else:
    s = 'Reprovado'
boletim = {'Nome': n, 'Média': m, 'Situação': s}
print('='*50)
print('SITUAÇÃO DO ALUNO')
for k, v in boletim.items():
    print(f'{k}: {v}')
print('='*50)


#mostra o conteúdo