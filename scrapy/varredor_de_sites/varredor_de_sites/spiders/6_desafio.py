import scrapy
from scrapy.loader import ItemLoader
from varredor_de_sites.items import CitacaoItem


class GoodReadsSpider(scrapy.Spider):
    # Identidade
    name = 'quotebot1'
    # Request

    def start_requests(self):
        # Definir url(s) a varrer
        urls = ['https://www.goodreads.com/quotes?page=1']
        # 'https://www.goodreads.com/quotes?page=1
        # 'https://www.goodreads.com/quotes?page=2
        

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    # Response

    def parse(self, response):
        # aqui é onde você deve processar o que é retornado da response
        for elemento in response.xpath("//div[@class='quote']"):
            loader = ItemLoader(item=CitacaoItem(), selector=elemento, response=response)
            loader.add_xpath('frase', ".//div[@class='quoteText']/text()")
            loader.add_xpath('autor', ".//span[@class='authorOrTitle']/text()")
            loader.add_xpath('tags', ".//div[@class='greyText smallText left']/a/text()")
            yield loader.load_item()

        # Encontrar o link para a próxima página e extrair o número da próxima página
        numero_proxima_pagina = response.xpath("//a[@class='next_page']/@href").get().split('=')[1]
        print('#'*20)
        print(numero_proxima_pagina)
        print('#'*20)
        if numero_proxima_pagina is not None:
            link_proxima_pagina = f'https://www.goodreads.com/quotes?page={numero_proxima_pagina}'
            print('#'*20)
            print(link_proxima_pagina)
            print('#'*20)
            yield scrapy.Request(url=link_proxima_pagina,callback=self.parse)

        # Ver se ainda existe um próxima página
        # Navegar até aquela próxima página ou parar caso não haja mais páginas