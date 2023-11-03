# Como usar a função click
import pyautogui

# Click personalizado
pyautogui.click(x=1000, y=500, clicks=2, interval=1, button='left', duration=1)
# Click simples(botão esquerdo)
pyautogui.click()
pyautogui.click(button='left')
pyautogui.click(button='right')
pyautogui.click(button='midle')
# Clicar x vezes
pyautogui.click(clicks=10)
# Funções prontas click
pyautogui.doubleClick()
pyautogui.tripleClick()
pyautogui.leftClick()
pyautogui.rightClick()
pyautogui.middleClick()
