from pickle import NEWFALSE
from watchfiles import watch
import os

# qual diretório quero monitor
diretorio = os.getcwd()

NEW_FILE = 1
MODIFIED = 2
DELETED = 3

for mudanca in watch(diretorio):
    for operacao in mudanca:
        tipo_operacao = operacao[0]
        arquivo = operacao[1]

        if tipo_operacao == NEW_FILE:
            print(f'Arquivo criado {arquivo}')
        if tipo_operacao == MODIFIED:
            print(f'Arquivo modificado {arquivo}')
        if tipo_operacao == DELETED:
            print(f'Arquivo excluído {arquivo}')