# Exiba todos os arquivos que estão naquela pasta
import os
print(os.listdir())
# Monte e exiba o caminho(path) absoluto dos 3 arquivos da pasta atual
datas_aniversario = os.getcwd() + os.sep + 'datas de aniversario.xlsx'
precos = os.getcwd() + os.sep + 'preços.txt'
relatorio = os.getcwd() + os.sep + 'relatorio.pdf'
print(datas_aniversario)
print(precos)
print(relatorio)
# Monte e exiba o caminho(path) que estão dentro das sub-pastas
texto_1 = os.getcwd() + os.sep + 'desafios texto' + \
    os.sep + 'desafio texto1.txt'
texto_2 = os.getcwd() + os.sep + 'desafios texto' + \
    os.sep + 'desafio texto2.txt'
texto_3 = os.getcwd() + os.sep + 'desafios texto' + \
    os.sep + 'desafio texto3.txt'
print(texto_1)
print(texto_2)
print(texto_3)
# Navegue para as 3 seguintes pastas, usando o os.chdir()
# Navegue até a pasta desafios texto
os.chdir(os.getcwd() + os.sep + 'desafios texto')
# Navegue de volta para a pasta desafio arquivos
os.chdir(os.pardir)
# Navegue para o diretório pai da pasta desafio arquivos
os.chdir(os.pardir)

