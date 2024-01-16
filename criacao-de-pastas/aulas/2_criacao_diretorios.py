import os

# Como criar um diretório
os.mkdir('Música')
# Como criar um sub-diretório
os.makedirs('Música' + os.sep + 'rock')
# Verificar se a pasta(diretório) existe
try:
    if not os.path.isdir('Música' + os.sep + 'rock'):
        os.mkdir('Música' + os.sep + 'rock')
    else:
        print('Diretório já foi criado')
except OSError:
    print('Não foi possível criar este diretório, pois já existe')
    