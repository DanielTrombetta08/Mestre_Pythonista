import pyautogui

email = pyautogui.prompt(text='Digite seu email', title='Dados de Login')
senha = pyautogui.password(text='Digite sua senha', title='Dados de Login', mask='*')

pyautogui.click(776,98, duration=1)
pyautogui.typewrite(email)
pyautogui.press('enter')
pyautogui.typewrite(senha)