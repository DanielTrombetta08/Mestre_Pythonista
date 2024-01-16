from watchfiles import watch
import os

# qual diretório quero monitor
diretorio = os.getcwd()

NEW_FILE = 1
MODIFIED = 2
DELETED = 3


def get_extension(arquivo):
    return arquivo[arquivo.rindex('.'):]


def is_text_file(arquivo):
    if get_extension(arquivo) == '.txt':
        return True


def is_pdf_file(arquivo):
    if get_extension(arquivo) == '.pdf':
        return True


for mudanca in watch(diretorio):
    for operacao in mudanca:
        tipo_operacao = operacao[0]
        arquivo = operacao[1]

        if tipo_operacao == NEW_FILE:
            if is_text_file(arquivo) == True:
                print('Foi criado um arquivo de texto')
            elif is_pdf_file(arquivo) == True:
                print('Foi criado um arquivo de pdf')
        if tipo_operacao == MODIFIED:
            print(f'Arquivo modificado {arquivo}')
        if tipo_operacao == DELETED:
            print(f'Arquivo excluído {arquivo}')