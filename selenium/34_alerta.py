from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
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
driver.get('https://cursoautomacao.netlify.app/')

# Situação 1 - Fechar alerta
# descer a página até elementos estarem visíveis
sleep(2)
driver.execute_script('window.scrollTo(0,500)')
sleep(2)
# digitar meu nome
campo_nome = driver.find_element(By.ID, "nome")
sleep(1)
campo_nome.send_keys('Daniel')
sleep(1)
botao_alerta = driver.find_element(By.ID, "buttonalerta")
sleep(2)
# clicar em alerta
botao_alerta.click()
sleep(2)
# clicar em ok para fechar alerta
alerta1 = driver.switch_to.alert
sleep(2)
alerta1.accept()
sleep(5)


# Situação 2 - Confirmar ou cancelar alerta
# encontrar o campo confirmar
sleep(2)
botao_confirmar = driver.find_element(By.ID, "buttonconfirmar")
# clicar no campo de confirmar
botao_confirmar.click()
sleep(2)
# Clicar em ok ou cancelar
alerta2 = driver.switch_to.alert
sleep(2)
# confirmar
alerta2.accept()
# cancelar
# alerta2.dismiss()

# Situação 3 - Inserir dados em  alerta e depois confirmar ou cancelar esses dados, além de fechar a alerta posterior
# encontrar o campo fazer pergunta
sleep(1)
botao_pergunta = driver.find_element(By.ID, "botaoPrompt")
sleep(1)
botao_pergunta.click()
# digitar algo dentro da alerta
alerta3 = driver.switch_to.alert
sleep(1)
alerta3.send_keys('Segunda')
sleep(2)
# clicar em confirmar (ou cancelar)
alerta3.accept()
sleep(2)
# fechar a janela posterior
alerta3.dismiss()
input('')
driver.close()