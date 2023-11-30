from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep

# Iniciar o webdriver


def iniciar_driver():
    chrome_options = Options()

    arguments = ['--lang=en-US', '--window-size=1920,1080',
                 '--incognito']

    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1

    })

    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait


driver, wait = iniciar_driver()
# Quais são os passos a fazer?

# 1 - Navegar até https://automatize.netlify.app/
driver.get('https://automatize.netlify.app')
sleep(2)
# Encontrar o elemento
campo_email = driver.find_element(By.ID, 'email')
sleep(2)
# 2 - Clicar no campo de e-mail
campo_email.click()
sleep(2)
# 3 - Digitar um e-mail
campo_email.send_keys('jhonatan@hotmail.com')
sleep(2)
# encontrar campo senha
campo_senha = driver.find_element(By.XPATH, "//input[@type='password']")
sleep(2)
# 4 - Clicar no campo de senha
campo_senha.click()
sleep(2)
# 5 - Digitar uma senha
campo_senha.send_keys('123456')
sleep(2)
# 6 - Clicar no botão iniciar
botao_iniciar = driver.find_element(
    By.XPATH, "//button[@class='btn btn-primary']")
sleep(2)
botao_iniciar.click()
input()