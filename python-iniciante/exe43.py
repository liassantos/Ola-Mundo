peso = float(input('Qual é o seu peso? (Kg) '))
alt = float(input('Qual é a sua altura? (m) '))
imc = peso / (alt ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print ('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
