import scrapy
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    LOGGER.setLevel(logging.WARNING)
    arguments = ['--lang=pt-BR', '--window-size=1920,1080', '--headless']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait


class F1RacesSpider(scrapy.Spider):
    # identidade
    name = 'formula1'
    # Request

    def start_requests(self):
        # não esqueça de setar ROBOTSTXT_OBEY = False dentro do arquivo settings.py
        urls = ['https://f1races.netlify.app/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'proximo_url': url})
    # Response

    def parse(self, response):
        driver, wait = iniciar_driver()
        driver.get(response.meta['proximo_url'])
        sleep(10)
        response_webdriver = Selector(text=driver.page_source)

        for corrida in response_webdriver.xpath("//div[@class='sc-bZQynM llbHfj']"):
            yield {
                'Grand Prix': corrida.xpath("./div[1]/text()").get(),
                'Local': corrida.xpath("./div[2]/text()").get(),
                'Piloto': corrida.xpath(".//a/text()").get(),
                'Tempo': corrida.xpath("./div[4]/text()").get()
            }
        driver.close()