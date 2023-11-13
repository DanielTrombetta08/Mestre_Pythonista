from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Fonte de opções de switches https://chromium.googlesource.com/chromium/src/+/master/chrome/common/chrome_switches.cc e  https://peter.sh/experiments/chromium-command-line-switches/
chrome_options = Options()
'''
--start-maximized # Inicia maximizado
--lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
--incognito # Usar o modo anônimo
--window-size=800,800 # Define a resolução da janela em largura e altura
--headless # Roda em segundo plano(com a janela fechada)
--disable-notifications # Desabilita notificações
--disable-gpu # Desabilita renderização com GPU
'''
arguments = ['--lang=pt-BR', '--window-size=500,500', '--incognito']
for argument in arguments:
    chrome_options.add_argument(argument)
# Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
# Uso de configurações experimentais
chrome_options.add_experimental_option('prefs', {
    # Alterar o local padrão de download de arquivos
    'download.default_directory': 'D:\\Storage\\Desktop\\projetos selenium\\downloads',
    # notificar o google chrome sobre essa alteração
    'download.directory_upgrade': True,
    # Desabilitar a confirmação de download
    'download.prompt_for_download': False,
    # Desabilitar notificações
    'profile.default_content_setting_values.notifications': 2,
    # Permitir multiplos downloads
    'profile.default_content_setting_values.automatic_downloads': 1,

})
# inicializando o webdriver
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=chrome_options)
# Navegar até um site
driver.get('https://pt.wikipedia.org/wiki/Brasil')

input('aperta uma tecla para fechar')