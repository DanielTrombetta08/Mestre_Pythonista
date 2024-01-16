import shutil
import os

# Copiar de um lugar para o outro
relatorio = os.getcwd() + os.sep + 'relatorio.pdf'
fotos = os.getcwd() + os.sep + 'fotos'
shutil.copy(relatorio, fotos)

# Copiar conteúdos de um diretório para outro
caminho_pasta_musica = os.getcwd() + os.sep + 'musica'
shutil.copytree(caminho_pasta_musica, fotos, dirs_exist_ok=True)

# Copiar pasta e seus conteúdos para uma nova pasta
os.makedirs('fotos' + os.sep + 'musica')
pasta_musica_em_pasta_fotos = os.getcwd() + os.sep + 'fotos' + os.sep + 'musica'
shutil.copytree(caminho_pasta_musica,pasta_musica_em_pasta_fotos,dirs_exist_ok=True)

# Mover arquivo individual para outro diretório
relatorio = os.getcwd() + os.sep + 'relatorio.pdf'
pasta_musica = os.getcwd() + os.sep + 'musica'
shutil.move(relatorio,pasta_musica)

# Remove um diretório inteiro
pasta_musica = os.getcwd() + os.sep + 'musica'
shutil.rmtree(pasta_musica)
fotos = os.getcwd() + os.sep + 'fotos'
shutil.make_archive('zip_tudo','zip',os.getcwd())
shutil.unpack_archive(os.getcwd()+ os.sep + 'zip_codigo.zip','codigo')