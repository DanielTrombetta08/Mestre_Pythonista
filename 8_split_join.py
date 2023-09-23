""" frase = 'Olá, bem-vindo a este treiamento!'
print(frase.split())
print(frase.split(','))
print(frase.split('-'))
nomes = 'jonatan, rafael, carol, amanda,jeferson'
print(nomes.split())
print(nomes.split(','))
hash = 'music #guitar #gamer #coder #python'
print(hash.split())
print(hash.split('#'))
print(hash.split('#', 3))
# Como concatenar(combinar) Strings
hash_separadas_espaco = hash.split(' ')
print(hash_separadas_espaco)
print(','.join(hash_separadas_espaco))
print('.'.join(hash_separadas_espaco))
print(' '.join(hash_separadas_espaco)) """

# Desafio

frase1 = 'Desafio manipulação de strings'
frase2 = 'jonatan,rafael,carol,camilla'
palavras1 = frase1.split()
palavras2 = frase2.split(',')
print(','.join(palavras1))
print(' & '.join(palavras2))

