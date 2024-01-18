import openpyxl

workbook = openpyxl.load_workbook('hockey_players.xlsx')
sheet_player_data = workbook['PlayerData']

for linha in sheet_player_data.iter_rows(min_row=2):
    if linha[2].value == 'Canada':
        linha[2].value = 'CANADA'
    if linha[5].value >= 150:
        linha[5].value = 'Divisão A'

workbook.save('hockey_players_novo.xlsx')