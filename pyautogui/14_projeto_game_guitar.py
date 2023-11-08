import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(2460,795,(0,152,0)):
        pyautogui.press('a')
    if pyautogui.pixelMatchesColor(2545,795,(255,0,0)):
        pyautogui.press('s')
    if pyautogui.pixelMatchesColor(2632,794,(244,244,2)):
        pyautogui.press('j')