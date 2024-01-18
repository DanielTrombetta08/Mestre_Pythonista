import openpyxl

workbook = openpyxl.Workbook()
workbook.create_sheet('vagas')
del workbook['Sheet']
sheet_vagas = workbook['vagas']
sheet_vagas.append(['empresa','vaga','data aplicação','retorno'])
continuar = 's'
while continuar == 's':
    empresa = input('Empresa: ')
    vaga = input('Vaga: ')
    data_aplicacao = input('Data da Aplicação: ')
    retorno = input('Retorno: ')
    sheet_vagas.append([empresa,vaga,data_aplicacao,retorno])
    continuar = input('Adicionar mais uma vaga? (s/n)')
workbook.save('Acompanhamento de Vagas.xlsx')
