city = str(input('Em que cidade você nasceu?' ))

#o programa deve reconhecer maíusculas e minúsculas

nameup = city.upper()

#o programa deve reconhecer espaços 

nonspace = nameup.strip()

#o programa deve verificar a palavra SANTO

verify = 'SANTO' in nonspace 

print(verify)