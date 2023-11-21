from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from random import randint


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

def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(randint(1, 5)/30)


driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/')
driver.maximize_window()
paragrafo = driver.find_element(By.XPATH, '//textarea[@placeholder="digite seu texto aqui"]')
texto = """Aqui recomendo que você sempre tenha essa história pronta para contar de uma forma que saliente o seu 
interesse por a área. Isso porque caso você realmente esteja interessado na vaga, desta maneira você irá mostrar 
a quem estiver te analisando que você tem uma grande probabilidade de ser um profissional mais engajado com as 
tarefas da empresa. Capriche nessa história.Muitos aqui iram dizer coisas como: porque vocês são uma ótima 
empresa, porque todos falam bem de você. Mas alerto: seja autêntico na sua resposta  as empresas querem aqui 
saber se você pesquisou sobre a empresa e como o seu skillset (seu conhecimento) pode agregar para a empresa, 
então use essa oportunidade para falar como a EMPRESA vai ganhar contratando você. Não diga coisas como: sempre
foi meu sonho trabalhar aqui! As empresas não ganham nada com seu sonho de querer trabalhar lá (triste, mas é a 
realidade), então mostre o que você tem de melhor para ajudar a empresa crescer. No meu caso a resposta que dei 
foi a seguinte: “Amo aprender e ensinar e estou constantemente me atualizando, além de gostar muito de ensinar 
e aprender com os outros integrantes da equipe, percebi que vocês em uma cultura internacional e isso me chamou 
muita atenção, seria ótimo poder trabalhar com vocês!”. """

digitar_naturalmente(texto, paragrafo)
input('')
driver.close()