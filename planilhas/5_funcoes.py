import openpyxl

workbook = openpyxl.Workbook()
workbook.create_sheet('demo funções')
sheet_funcoes = workbook['demo funções']
sheet_funcoes['A1'].value = '=SUM(5,5)'
sheet_funcoes['A2'].value = '=SUM(10,5)'
sheet_funcoes['A3'].value = '=SUM(5,10)'
sheet_funcoes['A4'].value = '=AVERAGE(2,4)'
sheet_funcoes['A5'].value = '=MIN(A1:A3)'
sheet_funcoes['A6'].value = '=MAX(A1:A3)'
workbook.save('Demo funções.xlsx')