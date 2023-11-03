import pyautogui
import pyperclip

def escrecer_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')

pyautogui.moveTo(856,107, duration=1)
pyautogui.click()
escrecer_frase('Automação é Incrível')
