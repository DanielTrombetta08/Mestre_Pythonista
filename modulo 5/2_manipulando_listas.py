valores = [1,2,3,4,5,6,7,8,9]
anos = [2020,2030,2040,2050,2060]
# Adicionar ao final da lista
valores.append(10)
print(valores)
# Unir listas
valores.extend(anos)
print(valores)
# Adiciona lista
nova_lista = valores + anos
print(nova_lista)
# Inserir
print(anos[1])
anos.insert(2,2031)
print(anos)
# Extrair com base no índice
anos_2020 = anos.pop(0)
print(anos_2020)
# Remover item da lista
anos.remove(2050)
del anos[1]
print(anos)

del valores[1:7]
print(valores)
# Contando a ocorrência de um valor
print(valores.count(10))
# Resetar
valores.clear()
print(valores)
