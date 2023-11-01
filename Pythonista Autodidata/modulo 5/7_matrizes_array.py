# Arrays
from array import array
# Inteiros, números decimais e caracteres
numeros = array('i', [1,2,3,4,5,6])
print(numeros)
numeros.append(10) #(valor)
print(numeros)
numeros.insert(5, 200) #(índice, valor)
print(numeros)
numeros.pop(1) #(índice)
print(numeros)
numeros.remove(5) #(valor)
print(numeros)
del numeros[1:3] # (índice ou faixa de índices)
print(numeros)