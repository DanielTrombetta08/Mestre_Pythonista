import webbrowser
import pyautogui
from time import sleep

telefones = []

with open('fones.txt', 'r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
    print(telefones)

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(1512,208,duration=1)
    sleep(10)
    pyautogui.typewrite('Opa, ignora essa mensagem. To testando uma automação de um robô! hehe')
    sleep(5)
    pyautogui.press('enter')
    sleep(300)