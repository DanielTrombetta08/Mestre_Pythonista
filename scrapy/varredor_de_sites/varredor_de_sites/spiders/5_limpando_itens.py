import scrapy
from scrapy.loader import ItemLoader
from varredor_de_sites.items import CitacaoItem


class QuotesToReadSpider(scrapy.Spider):
    # identidade
    name = 'citacao'

    # Request
    def start_requests(self):
        urls = ['https://quotes.toscrape.com/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response
    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            loader = ItemLoader(item=CitacaoItem(), selector=quote, response=response)
            loader.add_xpath('frase', './/span[@class="text"]/text()')
            loader.add_xpath('autor', './/small[@class="author"]/text()')
            loader.add_xpath('tags', './/div[@class="tags"]/a/text()')
            yield loader.load_item()
     
        try:
            link_proxima_pagina = response.xpath(
                "//li[@class='next']/a/@href").get()
            if link_proxima_pagina is not None:
                proxima_pagina_url_completo = response.urljoin(
                    link_proxima_pagina)
                yield scrapy.Request(
                    url=proxima_pagina_url_completo, callback=self.parse)
        except:
            print('Chegamos na última página')