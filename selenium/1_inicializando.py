from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Inicializando o webdriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Navegar até um site
driver.get('https://facebook.com')
input('Aperta uma tecla para fechar')
