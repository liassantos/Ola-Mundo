#Exe 81 (Extraindo dados de uma lista)

#recebe vários números e coloca em uma lista
resposta = 'S'
valores = list()
while resposta in 'Ss':
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja continuar? \033[30;47m[S/N]\033[m '))
#break point
print('='*50)
#quantos numeros foram digitados
if len(valores) == 1:
    print(f'Foi digitado \033[43m{len(valores)} valor\033[m.')
else:
    print(f'Foram digitados \033[43m{len(valores)} valores\033[m.')
#lista de valores ordenada de forma decrescente
valores.sort(reverse=True)
print(f'A lista gerada em ordem decrescente foi: \033[43m{valores}\033[m')
#se o valor 5 foi digitado e está ou não na lista
if 5 in valores:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 \033[41mNÃO\033[m está na lista.')
#end point
print('='*50)
