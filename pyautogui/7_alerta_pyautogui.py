# Alertar e pedir informação no PyAutoGUI
import pyautogui

# pyautogui.alert(text='Iniciando sua Automação', title='Automação de Login', button='Ok')

# Pedir informação

#email = pyautogui.prompt(text='Digite seu email', title='Informações Obrigatórias')
#print(f'Você digitou {email}')

# Confirmar se algo deve ou não acontecer

""" resposta = pyautogui.confirm(text='Continuar rodando nossa automação?', title='Confirmação', buttons=['Sim', 'Não', 'Cancelar'])
if resposta == 'Sim':
    print('continuando automação')
elif resposta == 'Não':
    print('encerrando automação')
else:
    print('operação cancelada') """

senha = pyautogui.password(text='Digite sua senha:', title='Dados de Login', mask='*')
print(senha)
