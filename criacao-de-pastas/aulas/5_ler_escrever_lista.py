'''
COMO CRIAR E MODIFICAR ARQUIVOS:
'r'  -> Usado somente para  ler algo
'w'  -> Usado somente para escever algo
'r+' -> Usado para ler e escrever algo
'a'  -> Usado para acrescentar algo
'''
import os
valores_celulares = [850, 2230, 1500, 3500, 5000]
# Como  criar um arquivo
with open('celulares.txt', 'w', newline='', encoding='utf-8') as arquivo:
    for valor in valores_celulares:
        arquivo.write(str(valor)+os.linesep)

# Como ler uma lista de dados
with open('celulares.txt', 'r', newline='', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)
# Para adicionar algo novo(sem apagar o anterior)
with open('celulares.txt', 'a', newline='', encoding='utf-8') as arquivo:
    arquivo.write('10000'+os.linesep)

# Para ler e escrever
with open('celulares.txt', 'r+', newline='', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)
    arquivo.write('15000'+os.linesep)