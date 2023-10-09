import os

frutas = ['laranja', 'banana', 'melao', 'abacate', 'maca']
cores = ['vermelho', 'amarelo', 'verde', 'azul', 'preto']
linguagens = ['python', 'javascript', 'sql', 'java', 'php']

# Desafio 1
""" with open('frutas.txt', 'a', newline='') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + os.linesep) """
# Desafio 2
""" with open('frutas.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha) """
# Desafio 3
""" with open('frutas.txt', 'a', newline='') as arquivo:
    for cor in cores:
        arquivo.write(os.linesep + cor) 
# Desafio 4
with open('Top 5 Linguagens.txt', 'a', newline='') as arquivo:
    for linguagem in linguagens:
        arquivo.write(linguagem + os.linesep) """

# BONUS - 
arquivos = ['musica.mp3', 'foto.jpg', 'senhas.txt', 'relatorio.pdf']
for arquivo in arquivos:
    with open(arquivo, 'w') as arquivo:
        pass