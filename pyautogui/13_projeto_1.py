import webbrowser
import pyautogui
import pyperclip
from time import sleep

def logout():
    pyautogui.click(3445,866, duration=1)
    pyautogui.click(1428,978, duration=1)
    pyautogui.click(1450,906, duration=1)

while True:
    # 1 - Navegar até o site https://www.instagram.com
    webbrowser.open('https://www.instagram.com')
    sleep(4)
    # 2 - Entrar com meu usuário
    # 3 - Entrar com minha senha
    # 4 - Clicar em "log in"
    # 5 - Clicar em "not now"
    # 6 - Fechar janela de "salvar senha"
    pyautogui.click(2854,598, duration=3)
    sleep(4)
    # 7 - Pesquisar pela página
    pyautogui.click(1584,279, duration=3)
    sleep(3)
    pyautogui.typewrite('slash')
    sleep(3)
    # 8 - Entrar na página
    pyautogui.click()
    sleep(3)
    # 9 - Clicar na postagem mais recente
    pyautogui.click(2481,577, duration=3)
    # 10 - Verificar se já curti a postagem
    coracao = pyautogui.locateCenterOnScreen('coracao.png')
    sleep(1)
    # 11 - Se já curti, não fazer nada, e pausar o bot por 24 horas
    if coracao is not None:
        logout()
        sleep(86400)
    # 12 - Se não tiver curtido, curtir a foto e deixar um comentário
    elif coracao == None:
        pyautogui.click(2857,872, duration=1)
        sleep(1)
        pyautogui.click(2996,981, duration=1)
        sleep(1)
        pyautogui.typewrite('Showw')
        sleep(1)
        pyautogui.click(3279,980, duration=1)
        sleep(3)
        logout()
        sleep(86400)
    # 13 - Pausar por 24 horas
    # 14 - Após 24 horas rodar de novo