import openpyxl

workbook = openpyxl.load_workbook('hockey_players.xlsx')
sheet_player_data = workbook['PlayerData']
print(sheet_player_data['D3'].value)
sheet_player_data['D3'].value = 'AMANDA'
workbook.save('hocker_players_novo.xlsx')