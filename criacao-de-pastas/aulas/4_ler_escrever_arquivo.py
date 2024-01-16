'''
COMO CRIAR E MODIFICAR ARQUIVOS:
'r'  -> Usado somente para  ler algo
'w'  -> Usado somente para escever algo
'r+' -> Usado para ler e escrever algo
'a'  -> Usado para acrescentar algo
'''
import os

# Como  criar um arquivo
with open('nomes.txt', 'w', newline='', encoding='utf-8') as arquivo:
    arquivo.write('meu nome é Daniel' + os.linesep)

# Como adicionar novo conteúdo, sem apagar o anterior
with open('nomes.txt', 'a', newline='', encoding='utf-8') as arquivo:
    arquivo.write('sou uma nova linha' + os.linesep)

# Ler conteúdos de um arquivo de texto
with open('nomes.txt', 'r', newline='', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)

# Ler e acrescentar algo ao mesmo tempo
with open('nomes.txt', 'r+', newline='', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)
    arquivo.write('Dev Aprender'+os.linesep)