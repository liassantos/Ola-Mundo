#Exe29 (Radar Eletrônico)

#o programa lê a velocidade do carro
speed = int(input('Digite a velocidade do carro: '))


#limite de velocidade 80km/h
#multa de R$7,00 por km acima do limite
if speed<=80:
  print('Você está dentro do limite de velocidade.')
else:
  print(f'Você foi multado. O valor da multa é R${(speed-80)*7}.')