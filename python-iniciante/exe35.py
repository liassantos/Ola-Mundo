#Exe35 (Analisador de Triângulos)
print('-='*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-='*20)
#o programa lê o cumprimento de três retas 
a = float(input('Cumprimento da primeira reta:'))
b = float(input('Cumprimento da segunda reta: '))
c = float(input('Cumprimento da terceira reta: '))

#o programa diz se elas formam ou não um triângulo
if abs(b-c) < a < (b + c) and abs(a-c) < b < (a + c) and abs(b-a) < c < (b + a):
    print('Os segmentos PODEM FORMAR um triângulo!')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo...')
