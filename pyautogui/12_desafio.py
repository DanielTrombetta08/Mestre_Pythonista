import webbrowser
import pyautogui
import pyperclip
from time import sleep

# Função para usar caracteres especiais
def escrecer_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')


# 1 Navegue até o site https://cursoautomacao.netlify.app
webbrowser.open('https://cursoautomacao.netlify.app')
# 2 Encontre e clique no campo "Digite seu nome" dentro de "Exemplos Alertas" e digitar seu nome
pyautogui.moveTo(2367,503, duration=4)
pyautogui.scroll(-300)
pyautogui.click(3378,881, duration=1)
#campo_digite = pyautogui.locateCenterOnScreen('digite.png')
#pyautogui.click(campo_digite[0],campo_digite[1])
#escrecer_frase('Daniel Trombetta')
pyautogui.typewrite('Daniel Trombetta')
# 3 Clicar em alerta, para gerar o alerta
#clicar_alerta = pyautogui.locateCenterOnScreen('alerta.png')
#pyautogui.click(clicar_alerta[0], clicar_alerta[1])
pyautogui.click(3317,912, duration=1)
# 4 Feche o alerta
pyautogui.moveTo(2825,165, duration=2)
sleep(1)
pyautogui.click(clicks=2)
# 5 Suba a página totalmente para cima
pyautogui.scroll(500)
sleep(1)
# 6 Desça apenas o suficiente para conseguir chegar na sessão que contém os arquivos para o qual você irá fazer p dowload deles e clicar
# e movimentar o mouse da maneira que for necessária para baixar os arquivos de excel e pdf
pyautogui.scroll(-1500)
pyautogui.click(2159,750, duration=2)
pyautogui.click(2356,753, duration=2)
# 7 Criar um alerta que diz "VOCÊ TERMINOU!"
pyautogui.alert(text='VOCÊ TERMINOU!', button='Ok')