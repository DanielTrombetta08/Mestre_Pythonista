import openpyxl

workbook = openpyxl.Workbook()
del workbook['Sheet']
workbook.create_sheet('instrumentos')
sheet_instrumentos = workbook['instrumentos']
sheet_instrumentos.append(['instrumento', 'marca', 'ano'])
sheet_instrumentos.append(['Instrumento 1', 'marca 1', '2019'])
sheet_instrumentos.append(['Instrumento 2', 'marca 2', '2020'])
sheet_instrumentos.append(['Instrumento 3', 'marca 3', '2021'])
sheet_instrumentos.append(['Instrumento 4', 'marca 4', '2022'])
sheet_instrumentos.append(['Instrumento 5', 'marca 5', '2022'])
workbook.save('Instrumentos.xlsx')

# Excluir linha
sheet_instrumentos.delete_rows(5)
sheet_instrumentos.delete_rows(4,5)
workbook.save('Instrumentos.xlsx')
# Excluir colunas
sheet_instrumentos.delete_cols(3)
sheet_instrumentos.delete_cols(1,2)
workbook.save('Instrumentos.xlsx')

# Para excluir com base no endereço da célula
del workbook['instrumentos']['B5']
workbook.save('Instrumentos.xlsx')