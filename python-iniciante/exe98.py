from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    if i <= f:
        for c in range(i, f+1, p):
            print(c, end=" ")
            sleep(0.5)
        print("FIM!")
    if i > f:
        for c in range(i, f-1, -p):
            print(c, end=" ")
            sleep(0.5)
        print("FIM!")


def linha():
    print('='*50)

linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)
