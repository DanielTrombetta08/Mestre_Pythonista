# Como digitar com PyAutogui
import pyautogui
import pyperclip

# Função para usar caracteres especiais
def escrecer_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')

# Mover mouse até o campo de digitar
pyautogui.moveTo(2114,932,duration=1)
# Clicar no campo de digitar
pyautogui.click()
# Digitar a mensagem
escrecer_frase('olá, bom dia')
# pyautogui.typewrite('Digitei aqui usando o PyAutoGUI, hehe')
# Clicar no botão de enviar
pyautogui.click(2843,1002, duration=1)
