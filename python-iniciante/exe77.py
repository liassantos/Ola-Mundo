#Tuplas
#Exe77 (Contando Vogais)

#fazer a tupla
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS')

#listar as vogais de cada palavra
for item in palavras:
    print(f'\nNa palavra {item} temos', end=' ')
    #vou dividir a palavra em letras
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')