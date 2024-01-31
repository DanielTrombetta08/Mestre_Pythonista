from pikepdf import Pdf

with Pdf.open('historias.pdf') as pdf:
    novo_pdf = Pdf.new()
    novo_pdf.pages.append(pdf.pages[0])
    novo_pdf.save('novo.pdf')