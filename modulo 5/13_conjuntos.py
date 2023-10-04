# SET
numeros = [2, 2, 5, 8]
frutas = {'maça', 'uva', 'banana', 'maça', 'morango'}
# Convertendo
set_numeros = set(numeros)
set_frutas = set(frutas)

print(set_numeros)
print(set_frutas)

# Adicionando 
set_numeros.add(10)
print(set_numeros)

# Conjuntos
numeros1 = [2, 2, 5, 8]
numeros2 = [2, 2, 3, 9]
a = set(numeros1)
b = set(numeros2)
print(a.symmetric_difference(b))
print(a.intersection(b))
print(a.union(b))

