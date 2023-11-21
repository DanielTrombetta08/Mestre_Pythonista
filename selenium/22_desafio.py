from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,1000', '--incognito']
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
# navegar até o site
driver.get('https://cursoautomacao.netlify.app/desafios')
driver.maximize_window()
sleep(2)
driver.execute_script("window.scrollTo(0, 1600);")
sleep(2)
checkboxes = driver.find_elements(By.XPATH, "//input[@name='carros']")

checkboxes[1].click()
checkboxes[3].click()
checkboxes[4].click()
sleep(2)

checkboxes_motos = driver.find_elements(By.XPATH, "//input[@name='motos']")
for moto in checkboxes_motos:
    moto.click()


input('')
driver.close()