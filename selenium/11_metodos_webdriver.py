from tkinter import Radiobutton
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


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
driver.get("https://cursoautomacao.netlify.com/")  # navegar até um site
driver.maximize_window()  # maximizar a janela
driver.refresh()  # recarrega página atual
driver.get(driver.current_url)  # recarrega página atual
driver.back()  # volta à página anterior
driver.forward()  # navega 1 vez para frente
print(driver.title)  # Obtem título da página
print(driver.current_url)  # Obtem URL(endereço) da página atual
print(driver.page_source)  # Obtem o código fonte da página atual
# obtem o texto dentro de um elemento
print(driver.find_element(By.XPATH, '//a[@class="navbar-brand"]').text)
print(driver.find_element(    By.XPATH, '//a[@class="navbar-brand"]').get_attribute("style"))

driver.close() # Fecha janela atual
input('')