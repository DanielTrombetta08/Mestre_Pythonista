from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as condicao_esperada


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

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
            TimeoutException
        ]
    )

    return driver, wait


driver, wait = iniciar_driver()
# Entrar no Instagram
driver.get('https://www.instagram.com/')
driver.maximize_window()
# Clicar e digitar usuário
campo_usuario = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//input[@name="username"]')))
campo_usuario.send_keys('danieltrombetta9')
# Clicar e digitar senha
campo_senha = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//input[@name="password"]')))
campo_senha.send_keys('123456')
# Clicar campo entrar
campo_entrar = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//div[text()="Entrar"]')))
campo_entrar.click()
while True:
    # Navegar até a pagina alvo
    driver.get('https://www.instagram.com/dev_aprender')
    # Clicar na última postagem
    postagens = wait.until(condicao_esperada.visibility_of_any_elements_located((By.XPATH, '//div[@class="_aagu"]')))
    postagens[0].click
    # Verificar se a postagem foi curtida
    elementos_postagem = wait.until(condicao_esperada.visibility_of_any_elements_located((By.XPATH, '//div[@class="_abm0"]')))

    if len(elementos_postagem) == 6:
        elementos_postagem[0].click()
        sleep(86400)
    else:
        print('postagem curtida')
        sleep(86400)

