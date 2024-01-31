from pikepdf import Pdf

# Exibir quantidade de páginas
with Pdf.open('historias.pdf') as pdf:
    print(len(pdf.pages))
    pdf.close()

# Excluir uma página
with Pdf.open('historias.pdf') as pdf:
    del pdf.pages[1:3]
    pdf.save('exclusão.pdf')