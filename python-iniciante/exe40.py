#Exe40 (Média de notas)
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
avg = (n1 + n2)/2

print(f'Tirando {n1} e {n2}, a média do aluno é {avg}')

if avg < 5:
  print('O aluno está REPROVADO')
elif 5 <= avg <= 6.9:
  print('O aluno está em RECUPERAÇÃO')
else:
  print('O aluno está APROVADO')