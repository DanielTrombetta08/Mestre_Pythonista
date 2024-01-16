import os

frutas = ['Fruta1', 'Fruta2', 'Fruta3', 'Fruta4', 'Fruta5', ]
cores = ['Cor1', 'Cor2', 'Cor3', 'Cor4', 'Cor5']
linguagens = ['Python', 'C#', 'Javascript', 'Java', 'PHP']

# Desafio 1
# Crie um novo arquivo chamado frutas.txt e insira dentro dele todos as 5 frutas que estão na lista de frutas
with open('frutas.txt', 'w', newline='', encoding='utf-8') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + os.linesep)

# Desafio 2
# Imprima na tela todas as linhas que estao dentro do arquivo frutas.txt
with open('frutas.txt', 'r', newline='', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)

# Desafio 3
# Sem apagar os dados que já estão dentro de frutas.txt, adicione todas as cores que estão dentro da sua lista de cores ao arquivos frutas.txt
with open('frutas.txt', 'a', newline='', encoding='utf-8') as arquivo:
    for cor in cores:
        arquivo.write(cor + os.linesep)

# Desafio 4
# Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o arquivo, de forma com que cada linguagem ocupe apenas uma linha.
with open('Top 5 Linguagens.txt', 'w', newline='', encoding='utf-8') as arquivo:
    for linguagem in linguagens:
        arquivo.write(linguagem + os.linesep)