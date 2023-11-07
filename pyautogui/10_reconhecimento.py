# Reconhecimento de imagem simples com pyautogui
import pyautogui

# Encontrar as coordenadas próximas de onde aquela imagem está
print(pyautogui.locateOnScreen('quatro.png'))
# Encontrar as coordenadas do centro da imagem
print(pyautogui.locateCenterOnScreen('quatro.png'))
# Como quebrar captcha
captcha = pyautogui.locateCenterOnScreen('captcha.png')
pyautogui.click(captcha[0], captcha[1], duration=2)
