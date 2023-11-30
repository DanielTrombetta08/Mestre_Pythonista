from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def iniciar_driver():
    chrome_options = Options()

    arguments = ['--lang=en-US', '--window-size=1920,1080',
                 '--incognito', '--disable-gpu', '--no-sandbox', '--headless', '--disable-dev-shm-usage']

    for argument in arguments:
        chrome_options.add_argument(argument)
    chrome_options.headless = True
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

driver.get('https://cursoautomacao.netlify.app/listagem1')
while True:
    sleep(2)

    # Encontrar título dos produtos
    produtos = wait.until(CondicaoExperada.visibility_of_all_elements_located(
        (By.XPATH, "//h5//a")))

    # Encontrar preços dos produtos
    precos = wait.until(CondicaoExperada.visibility_of_all_elements_located(
        (By.XPATH, "//p[@class='price-container']/span")))
    sleep(2)

    # Imprimir valores na tela
    for produto, preco in zip(produtos, precos):
        print(produto.text, preco.text)

    # Buscar próxima página
    try:
        botao_proxima_pagina = wait.until(
            CondicaoExperada.element_to_be_clickable((By.ID, "proxima_pagina")))
        botao_proxima_pagina.click()
        sleep(2)
        print('clicked next page')
    except:
        print('Chegamos a última página')
        sleep(60)
        driver.get('https://cursoautomacao.netlify.app/listagem1')
