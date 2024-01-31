from pikepdf import Pdf

# Como combinar 2(ou mais) PDFs em um
pdf = Pdf.new()
fonte1 = Pdf.open('demo.pdf')
fonte2 = Pdf.open('historias.pdf')

pdf.pages.extend(fonte1.pages)
pdf.pages.extend(fonte2.pages)

pdf.save('combinado.pdf')

fonte1.close()
fonte2.close()
pdf.close()