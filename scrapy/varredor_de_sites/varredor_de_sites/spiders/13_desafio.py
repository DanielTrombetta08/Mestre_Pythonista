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


class IndeedSpider(scrapy.Spider):
    # identidade
    name = 'indeed'
    # Request

    def start_requests(self):
        # não esqueça de setar ROBOTSTXT_OBEY = False dentro do arquivo settings.py
        urls = ['https://br.indeed.com/jobs?q=python&l=&from=searchOnHP&vjk=467f2bd1131d76e0']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'proximo_url': url})
    # Response

    def parse(self, response):
        driver, wait = iniciar_driver()
        driver.get(response.meta['proximo_url'])
        sleep(10)
        response_webdriver = Selector(text=driver.page_source)

        for elemento in response.xpath("//div[@class='job_seen_beacon']"):
            yield {
                'cargo': elemento.xpath(".//span[@id='jobTitle-467f2bd1131d76e0']/text()").get(),
                'nome da empresa': elemento.xpath(".//span[@class='css-1x7z1ps eu4oa1w0']/text()").get(),
                'local': elemento.xpath(".//div[@class='css-t4u72d eu4oa1w0']/text()").get(),
                'link da vaga': elemento.xpath(".//a[@id='sj_467f2bd1131d76e0']").get()
            }
        driver.close()