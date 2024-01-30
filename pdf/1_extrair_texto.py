from fpdf import FPDF
# orientation - 'P'(vertical) 'L'(horizontal)
# unit - 'mm', 'cm', 'in'
# format - 'A3','A4','A5','Letter','Legal',(100,150)
pdf = FPDF(orientation='p', unit='cm', format='a4')
# adicionar uma página(isso é obrigatório)
pdf.add_page()
# fontes - 'times','courier','helvetica','symbol','zpfdingbats'
# formatação - 'b'(negrito), 'u'(sublinhado), 'i'(itálico), 'BI'(combinação)
pdf.set_font("times", "BUI", 16)
# A4 - 21cm x 29.7cm
# Align - 'L'(esquerda),'R'(direita),'C'(centralizado), 'J'(justificado)
pdf.cell(w=0, h=0.8, txt="Hello World!",
         align='c', new_x='LMARGIN', new_y='NEXT')
pdf.set_font(family='times', size=12)
longtext = f'''Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.'''
pdf.ln(0.5)
pdf.multi_cell(w=0, h=0.7, txt=longtext, align='j',
               new_x='LMARGIN', new_y='NEXT')
pdf.output("tuto1.pdf")