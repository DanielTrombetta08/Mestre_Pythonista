from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select


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
driver.get('https://cursoautomacao.netlify.app/desafios')
driver.maximize_window()
sleep(2)
driver.execute_script("window.scrollTo(0, 2000);")
sleep(2)
paises = driver.find_element(By.XPATH, '//select[@id="paisesselect"]')
opcoes = Select(paises)

opcoes.select_by_index(2)
sleep(2)

opcoes.select_by_value('africa')
sleep(2)

opcoes.select_by_visible_text('Chille')
sleep(2)


input('')
driver.close()