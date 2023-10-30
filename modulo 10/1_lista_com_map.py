numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)

# Map
nomes = ['Larissa', 'Rafael', 'Marcos', 'João']

def aprovar_pessoa(nome):
    # Lógica mais complexa
    return nome + ' Aprovado'

print(list(map(aprovar_pessoa, nomes)))
