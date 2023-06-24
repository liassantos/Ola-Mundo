r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

#é um triangulo?
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  if (r1 == r2 and r2 != r3) or (r1 == r3 and r2 != r3) or (r2 == r3 and r1 != r3):
    print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES')
  elif r1 != r2 and r2 != r3 and r1 != r3:
    print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO')
  elif r1 == r2 and r1 == r3 and r2 == r3:
    print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO')
else:
  print('Os segmentos acima NÃO PODEM FORMAR um triângulo')