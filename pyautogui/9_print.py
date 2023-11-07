# Como tirar print da tela inteira ou parte dela
import pyautogui

# Print da tela inteira
pyautogui.screenshot('tela.jpg')

# Print de uma parte da tela
pyautogui.screenshot('calculadora.jpg', region=(851,75,327,550))
