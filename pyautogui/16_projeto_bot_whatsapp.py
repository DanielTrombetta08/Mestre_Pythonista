import webbrowser
import pyautogui
from time import sleep

telefones = [5548999454534]

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
"""     sleep(10)
    pyautogui.click(1512,208,duration=1)
    sleep(10)
    pyautogui.typewrite('Opa, ignora essa mensagem. To testando uma automação de um robô! hehe')
    sleep(5)
    pyautogui.press('enter')
    sleep(300) """