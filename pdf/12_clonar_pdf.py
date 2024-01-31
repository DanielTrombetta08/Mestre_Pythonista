from pikepdf import Pdf

novo_pdf = Pdf.new()
with Pdf.open('historias.pdf') as pdf:
    pdf.save('historias_backup.pdf')