import os
# Obter nome do Sistema Operacional(nt para windows e posix para linux/mac)
print(os.name)
# Listar todos arquivos no diretório atual
print(os.listdir())
# retorna o separador nativo do Sistema Operacional
print(os.sep)
# Ex: como montar caminhos de arquivos de forma dinâmica
print(os.path.join(os.getcwd() + os.sep + 'relatorio.pdf'))
# Armazena o caminho completo de um arquivo
caminho = os.path.join(os.getcwd() + os.sep + 'relatorio.pdf')
# Retorna apenas o diretório daquele caminho(path)
print(os.path.dirname(caminho))
# Retorna apenas a parte final daquele caminho(normalmente é o nome do arquivo)
print(os.path.basename(caminho))
# Retorna as partes de um caminho(path)
print(os.path.split(caminho))
# Acessa o item no índice 0
print(os.path.split(caminho)[0])
# Acessa o item no índice 1
print(os.path.split(caminho)[1])
# Como navegar até o diretório pai(nível acima)
caminho_atual = os.getcwd() + os.sep
print(os.path.abspath(os.path.join(caminho_atual, os.pardir)))
# Verificar se um diretório existe
print(os.path.exists('musica'))
# Mudar de diretório
os.chdir('imagens')
# Subir um nível
os.chdir(os.pardir)
