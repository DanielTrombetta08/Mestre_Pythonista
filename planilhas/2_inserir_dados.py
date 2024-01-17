import openpyxl

workbook = openpyxl.Workbook()
del workbook['Sheet']
workbook.create_sheet('instrumentos')

# Como selecionar um sheet para trabalhar nele
sheet_instrumentos = workbook['instrumentos']

# Sempre colocar cabeçalho, se não existir ainda
sheet_instrumentos.append(['instrumento','marca','preço'])
workbook.save('Instrumentos.xlsx')

# Para adicionar dados em uma linha
sheet_instrumentos.append(['Instrumento 1','Marca 1','1500'])
sheet_instrumentos.append(['Instrumento 2','Marca 2','2500'])
sheet_instrumentos.append(['Instrumento 3','Marca 3','3500'])
sheet_instrumentos.append(['Instrumento 4','Marca 4','4500'])

# Como adicionar dados por endereço da célula
sheet_instrumentos['A6'].value = 'Instrumento 5'
sheet_instrumentos['B6'].value = 'Marca 5'
sheet_instrumentos['C6'].value = '5000'
workbook.save('Instrumentos.xlsx')