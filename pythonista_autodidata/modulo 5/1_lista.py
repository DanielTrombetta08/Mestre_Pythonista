""" # Listas
precos = [10,20,30,40,50,60,100]
print(precos[0])
print(precos[precos.index(100)])
# Litas no python são dinâmicas(aceitam qualquer valor)
itens = [1,2,3,'Ola', 'Café', True, 10.6]
print(itens[4])
# Maneiras diferentes de gerar uma lista
# Multiplicação de valores(repetição)
lista_de_noves = [9] * 10
lista_de_testes = ['teste'] * 10
print(lista_de_noves)
print(lista_de_testes)
# Usando gerador Range(Sequência)
# 1 a 29
faixa_de_numeros = list(range(30))
print(faixa_de_numeros)
# Gerar a partir de strings
print(list('Bem-vindo ao treinamento'))
# Lista de lista
matriz_de_nomes = [['Carol', 30], ['Marcos', 50]]
print(matriz_de_nomes[0])
print(matriz_de_nomes[0][0]) """

# Desafio 1
objetos = ['computador', 'mouse', 'monitor']
print(objetos)
# Desafio 2
lista_numeros = list(range(10,131))
print(lista_numeros)
# Desafio 3
print(objetos + lista_numeros)
# Desafio 4
lista_objetos = [['computador', 3000], ['mouse', 100], ['monitor', 1000]]
print(lista_objetos)
print(lista_objetos[0])