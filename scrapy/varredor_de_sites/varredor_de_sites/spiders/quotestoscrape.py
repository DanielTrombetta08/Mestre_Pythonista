from typing import Any, Iterable
import scrapy
from scrapy.http import Request, Response

# CamelCase
class QuotesToScrapeSpider(scrapy.Spider):
    # Identidade
    name = 'frasebot1'
    # Request
    def start_requests(self):
        # Definir url(s) a varrer
        urls = ['https://quotes.toscrape.com']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response
    def parse(self, response):
        # Aqui é onde você deve processar o que é retornado da response
        with open('pagina.html', 'wb') as arquivo:
            arquivo.write(response.body)