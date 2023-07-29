#Tuplas
#Exe73 (Times de Futebol)

times = ('Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Athletico-PR', 'São Paulo', 'Fluminense',
        'Bragantino', 'Fortaleza', 'Internacional', 'Cruzeiro', 'Cuiabá', 'Atlético-MG', 'Santos',
        'Corinthians', 'Goiás', 'Bahia', 'Coritiba', 'América-MG', 'Vasco')

print(f'A) Os cinco primeiros colocados são: {times[0:5]}')
print(f'B) Os quatro últimos colocados são: {times[-4:]}')
print(f'C) Os times em ordem alfabética são: {sorted(times)}')
print(f'D) O Fortaleza está na {times.index("Fortaleza")+1}ª posição da tabela.')