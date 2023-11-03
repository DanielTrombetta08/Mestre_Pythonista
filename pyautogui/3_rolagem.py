# Como simular rolagem do mouse
import pyautogui
from time import sleep

# Página Brasil wikipédia - História
pyautogui.moveTo(853,464, duration=1)
pyautogui.scroll(-4500)