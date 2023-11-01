# Continue, ignorar/pular
""" for numero in range(10):
    if numero % 2 ==0:
        print(numero)
    else:
        continue

for numero in range(10):
    if numero % 2 ==0:
        print(numero)
    else:
        break """

frutas = ['Maça', 'Manga', 'Laranja', 'Morango']
for fruta in frutas:
    if fruta == 'Manga':
        continue
    print(f'{fruta} adicionada a dieta')

frutas = ['Maça', 'Manga', 'Laranja', 'Morango']
for fruta in frutas:
    if fruta == 'Manga':
        break
    print(f'{fruta} adicionada a dieta')