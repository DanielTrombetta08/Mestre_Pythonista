import openpyxl

workbook = openpyxl.Workbook()
workbook.create_sheet('funcionários')
sheet_funcionarios = workbook['funcionários']
sheet_funcionarios.append(['nome', 'cargo', 'salário'])
continuar = 's'
while continuar == 's':
    nome = input('Nome: ')
    cargo = input('Cargo: ')
    salario = input('Salário: ')
    sheet_funcionarios.append([nome, cargo, salario])
    continuar = input('Adicionar mais um funcionário? (s/n)')

workbook.save('Funcionários.xlsx')