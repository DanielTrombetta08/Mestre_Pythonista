import scrapy


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
            yield {
                'frase': quote.xpath('.//span[@class="text"]/text()').get(),
                'autor': quote.xpath('.//small[@class="author"]/text()').get(),
                'tags': quote.xpath('.//div[@class="tags"]/a/text()').getall()
            }
     
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