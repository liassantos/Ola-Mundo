#Exe31 (Custo da Viagem)

#o programa pergunta a distância da viagem
distance = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a fazer uma viagem de {distance} Km.')


#o programa calcula o preço da viagem
#0,50 até 200 km e 0,45 para mais de 200 km

if distance <=200:
  print(f'E o preço da passagem será de R${distance*0.5:.2f}')
else:
  print(f'E o preço da passagem será de R${distance*0.45:.2f}')