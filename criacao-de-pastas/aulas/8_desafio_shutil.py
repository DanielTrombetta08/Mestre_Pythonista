import shutil
import os

'''
 Crie 3 pastas diferentes no seu diretório atual(manualmente):
    * Arquivos 2010
    * Documentação
    * Backup
    Agora crie 3 arquivos fora destas pastas
    * nomes.txt
    * inscrições.pdf
    * relatórios.xlsx
'''
# 1) Copie o arquivo nomes.txt para a pasta 'Arquivos 2010'
shutil.copy(os.getcwd() + os.sep + 'nomes.txt',
            os.getcwd() + os.sep + 'Arquivos 2010')
# 2) Mova o arquivo inscrições.pdf para a pasta 'Documentação'
shutil.move(os.getcwd() + os.sep + 'inscrições.pdf',
            os.getcwd() + os.sep + 'Documentação')
# 2) Faça uma cópia da pasta 'Arquivos 2010' e tudo que estiver contido nela para a pasta uma nova pasta chamada 'Backup Arquivos 2010'
caminho_arquivos_2010 = os.getcwd() + os.sep + 'Arquivos 2010'
os.makedirs('Backup Arquivos 2010' + os.sep + 'Arquivos 2010')
caminho_backup = os.getcwd() + os.sep + 'Backup Arquivos 2010' + os.sep + 'Arquivos 2010'
shutil.copytree(caminho_arquivos_2010, caminho_backup, dirs_exist_ok=True)
# 3) Compacte todo o conteúdo da pasta 'Documentação' no formato zip
shutil.make_archive('Documentação', 'zip')
# 4) Mova o arquivo compactado para dentro da pasta 'Backup'
shutil.move(os.getcwd() + os.sep + 'Documentação.zip',os.getcwd() + os.sep + 'Backup')
# 4) Exclua o diretório 'Arquivos 2010' e 'Documentação' e seus conteúdos
shutil.rmtree(os.getcwd() + os.sep + 'Arquivos 2010')
shutil.rmtree(os.getcwd() + os.sep + 'Documentação')
# 5) Compacte o diretório inteiro, para um arquivo chamado 'Backup Arquivos Python.zip'
shutil.make_archive('Backup Arquivos', 'zip', os.getcwd())