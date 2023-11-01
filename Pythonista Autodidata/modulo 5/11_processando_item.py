# Como podemos criar listas
# Criar listas usando Loops e Range()
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)
# Map
nomes = ['Larissa', 'Rafael', 'Marcos', 'John']

def aprovar_pessoa(nome):
    # Lógica mais complexa
    return nome + ' Aprovado'

print(list(map(aprovar_pessoa, nomes)))
