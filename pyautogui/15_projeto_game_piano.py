import pyautogui
import keyboard
from time import sleep
import win32api
import win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
while keyboard.is_pressed('1') == False:
    pyautogui.pixelMatchesColor()