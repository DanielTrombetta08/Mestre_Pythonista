from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
# Navegar até o site
driver.get('https://cursoautomacao.netlify.app/')
driver.maximize_window()
sleep(1)
# Encontrar e clicar no link de desafios
botao_desafio = driver.find_element(By.LINK_TEXT, 'Desafios')
sleep(1)
botao_desafio.click()
sleep(1)
# Scroll
driver.execute_script("window.scrollTo(0, 300);")
sleep(1)
# Encontrar e clicar no campo nome
campo_nome = driver.find_element(By.ID, 'dadosusuario')
sleep(1)
# Digitar o nome
campo_nome.send_keys('Daniel Trombetta')
sleep(1)
# Encontrar botão Clique aqui
botao_enviar = driver.find_element(By.ID, 'desafio2')
sleep(1)
botao_enviar.click()
sleep(1)
# Encontrar campo que apareceu
campo_novo = driver.find_element(By.ID, 'escondido')
sleep(1)
# Digitar o nome
campo_novo.send_keys('Daniel Trombetta')
sleep(1)
# Clicar em Validar
botao_validar = driver.find_element(By.ID, 'validarDesafio2')
botao_validar.click()


input('')
driver.close()