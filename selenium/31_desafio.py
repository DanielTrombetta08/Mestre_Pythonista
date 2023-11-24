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
driver.get('https://cursoautomacao.netlify.app/desafios')
driver.maximize_window()
# 1) Salvar nossa janela atual
janela_inicial = driver.current_window_handle
print(f'primeira janela: {janela_inicial}')
sleep(2)
# 2) Abrir um nova janela
driver.execute_script('window.scrollTo(0,2500);')
sleep(2)
botao_nova_janela = driver.find_element(By.XPATH, "//button[text()='Abrir nova janela']")
sleep(1)
driver.execute_script('arguments[0].click()', botao_nova_janela)
sleep(1)
# 3) quais janelas estão abertas
janelas = driver.window_handles
for janela in janelas:
    if janela not in janela_inicial:
        driver.switch_to.window(janela)
        driver.maximize_window()
        sleep(2)
        campo_opiniao = driver.find_element(By.ID, 'opiniao_sobre_curso')
        sleep(1)
        campo_opiniao.click()
        sleep(2)
        campo_opiniao.send_keys('Muito bom!')
        sleep(2)
        botao_pesquisar = driver.find_element(By.ID, 'fazer_pesquisa')
        sleep(2)
        botao_pesquisar.click()
        sleep(2)
        driver.close()
driver.switch_to.window(janela_inicial)
# 4) Encontrar o campo para digitar na janela inicial
campo_desafio = driver.find_element(By.ID, 'campo_desafio7')
sleep(1)
campo_desafio.click()
sleep(1)
campo_desafio.send_keys('ola')







input('')
driver.close()