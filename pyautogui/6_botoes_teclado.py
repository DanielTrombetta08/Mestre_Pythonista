# Como usar botões e atalhoso do teclado
import pyautogui
from time import sleep

# Navegar e clicar no campo email
pyautogui.click(1411,265,duration=2)
sleep(1)
# Digitar o email
pyautogui.typewrite('daniel@hotmail')
sleep(1)
# Apertar tab
pyautogui.press('tab')
sleep(1)
# Digitar minha senha
pyautogui.typewrite('213456')
sleep(1)
# Apertar tab
pyautogui.press('tab')
sleep(1)
# Aperta espaço
pyautogui.press('space')

# Para ver todas as teclas possíveis
print(pyautogui.KEYBOARD_KEYS)

# Como usar combinações de teclas
pyautogui.click(797,98, duration=1)
# Simular segurar uma tecla
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1850,543, duration=1)
pyautogui.hotkey('ctrl', 'v')
