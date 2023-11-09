import pyautogui
import keyboard
from time import sleep
import win32api
import win32con

pyautogui.click(2582,518,duration=1)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(2445,413,(0,0,0)):
        click(2445,413)
    if pyautogui.pixelMatchesColor(2531,419,(0,0,0)):
        click(2531,419)
    if pyautogui.pixelMatchesColor(2620,421,(0,0,0)):
        click(2620,421)
    if pyautogui.pixelMatchesColor(2715,424,(0,0,0)):
        click(2715,424)
