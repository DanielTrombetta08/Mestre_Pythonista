# Pegar e arrastar algo para outro lugar
import pyautogui

# Mover para a coord
pyautogui.moveTo(1358,257, duration=1)
# Clicar e arrastar até um ponto e soltar
pyautogui.dragTo(1360,790,button='left', duration=1)
 