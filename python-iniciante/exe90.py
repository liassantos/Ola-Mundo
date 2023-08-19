#lê o nome, média e situação (>= 7 aprovado) + guarda no dicionário
boletim = {}
boletim['Nome'] = str(input('Digite o nome do aluno: '))
boletim['Média'] = float(input(f'Digite a média de {boletim["Nome"]}: '))
boletim['Situação'] = 'Aprovado' if boletim['Média'] >= 7 else 'Reprovado' if boletim['Média'] <6 else 'Recuperação'
#mostra o conteúdo
print('='*50)
print('SITUAÇÃO DO ALUNO')
for k, v in boletim.items():
    print(f'{k}: {v}')
print('='*50)


