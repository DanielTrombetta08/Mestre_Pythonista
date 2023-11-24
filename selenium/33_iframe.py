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
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
sleep(1)
# Encontrar a iframe
iframe = driver.find_element(
    By.XPATH, "//iframe[@src='https://cursoautomacao.netlify.app/desafios.html']")

# Mudar para dentro da iframe
driver.switch_to.frame(iframe)
sleep(2)
# Interagir com ela
campo_nome = driver.find_element(By.ID, 'dadosusuario')
sleep(2)
campo_nome.send_keys('Daniel')
# Sair do iframe
driver.switch_to.default_content()
input('')
driver.close()