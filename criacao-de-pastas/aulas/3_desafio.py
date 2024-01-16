# DESAFIO - Criando diretório
import os
# Crie um novo diretório dentro do diretório atual, chamado 'Arquivos'
os.mkdir('Arquivos')
# Em um outro comando crie um novo diretório dentro do diretório 'Arquivos' chamado 'Arquivos pdf'
os.makedirs('Arquivos' + os.sep + 'Arquivos pdf')
# Em apenas uma linha crie o diretório 'Fotos' e dentro o sub-diretório 'Fotos verão'
os.makedirs('Fotos' + os.sep + 'Fotos verão')