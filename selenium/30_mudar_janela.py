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
driver.maximize_window()
# 1) Salvar nossa janela atual
janela_inicial = driver.current_window_handle
print(f'primeira janela: {janela_inicial}')
# 2) Abrir um nova janela
driver.execute_script('window.scrollTo(0,500);')
sleep(3)
botao_abrir_janela = driver.find_element(
    By.XPATH, "//button[text()='Abrir Janela']")
sleep(1)
driver.execute_script('arguments[0].click()', botao_abrir_janela)
sleep(1)
# 3) quais janelas estão abertas
janelas = driver.window_handles
for janela in janelas:
    print(janela)
    if janela not in janela_inicial:
        # alterar para essa nova janela
        driver.switch_to.window(janela)
        sleep(2)
        campo_pesquisa = driver.find_element(By.ID, "campo_pesquisa")
        sleep(2)
        campo_pesquisa.send_keys('computador')
        sleep(2)
        botao_pesquisar = driver.find_element(By.ID, "fazer_pesquisa")
        sleep(2)
        botao_pesquisar.click()
        driver.close()
driver.switch_to.window(janela_inicial)

input('')
driver.close()