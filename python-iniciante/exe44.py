#Simulador de Pagamentos de Loja
print(' LOJAS GUANABARA '.center(50, '='))
price = float(input('Preço das Compras: R$ '))
print('FORMA DE PAGAMENTO \n'
      '[ 1 ] à vista dinheiro/cheque \n'
      '[ 2 ] à vista cartão \n'
      '[ 3 ] 2x no cartão \n'
      '[ 4 ] 3x ou mais no cartão')
choice = int(input('Qual é a opção? '))

if choice == 1:
    print('Você escolheu à vista dinheiro/cheque.')
    print(f'Você recebeu 10% de desconto e suas compras vão ficar por R${price*0.9:.2f}')
elif choice == 2:
    print('Você escolheu à vista cartão.')
    print(f'Você recebeu 5% de desconto e suas compras vão ficar por R${price * 0.95:.2f}')
elif choice == 3:
    parcela = price/2
    print('Você escolheu à vista 2x no cartão.')
    print(f'Suas compras vão ficar por R${price:.2f}, parceladas em 2x de R$ {parcela:.2f}')
elif choice == 4:
    parcela = int(input('Quantas parcelas? '))
    juros = price * 1.2
    print(f'Você escolheu à vista {parcela}x no cartão.')
    print(f'Com os 20% de JUROS, suas compras vão ficar por R${juros:.2f}, parceladas em {parcela}x de R${juros / parcela:.2f}')
else:
    print('Opção inválida de pagamento.\nTente novamente.')