import pyautogui

# Para importar no cmd
# python
# from mouseinfo import mouseInfo
# mouseInfo()
# pra interromper jogar o cursor do mouse para o topo superior esquerdo bem rápido

# Posição de algo - use o mouseInfo
# Fazer algo com essa posição
pyautogui.moveTo(1270,50, duration=2)
pyautogui.move(0,-50,duration=2)
for i in range(100):
    pyautogui.click()