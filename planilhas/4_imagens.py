import openpyxl
from openpyxl.drawing.image import Image

workbook = openpyxl.Workbook()
workbook.create_sheet('produtos')
sheet_produtos = workbook['produtos']
sheet_produtos.append(['item', 'imagem', 'preço'])
sheet_produtos['A2'].value = 'Celular'
sheet_produtos['C2'].value = '2500'

# Para adicionar uma imagem
img = Image('fone1.png')
sheet_produtos.add_image(img, 'B2')
# salvar
workbook.save('Produtos.xlsx')