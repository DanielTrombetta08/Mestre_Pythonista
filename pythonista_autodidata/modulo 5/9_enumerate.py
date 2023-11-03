# Enumerate
for indice, numero in enumerate(range(1, 11), 1):
    print(indice, numero)
    if indice == 5:
        print('Estamos na metade da lista')

nomes = ['nome1', 'nome2', 'nome3', 'nome4', 'nome5']

for indice, nome in enumerate(nomes, 1):
    print(indice, nome)
    if indice == 3:
        print('Já temos 3 pessoas cadastradas')

frutas = ['Maçã', 'Laranja', 'Morango', 'Limão']

for indice, fruta in enumerate(frutas, 0):
    if indice == 3:
        print(f'{indice} {fruta} em PROMOÇÃO')
    else:
        print(indice, fruta)

