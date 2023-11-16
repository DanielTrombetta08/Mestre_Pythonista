from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/desafios.html')

botao_1 = driver.find_element(By.ID, 'btn1')
botao_2 = driver.find_element(By.CLASS_NAME, 'btn2.btn.btn-dark')
botao_3 = driver.find_element(By.CLASS_NAME, 'btn2.btn.btn-warning')

if botao_1.is_enabled():
    print('botão 1 esta habilitado')
else:
    print('botão 1 está desabilitado')

if botao_2.is_enabled():
    print('botão 2 esta habilitado')
else:
    print('botão 2 está desabilitado')

if botao_3.is_enabled():
    print('botão 3 esta habilitado')
else:
    print('botão 3 está desabilitado')

    
input('')
driver.close()
    