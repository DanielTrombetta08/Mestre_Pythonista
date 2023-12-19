import scrapy


class IndeedSpider(scrapy.Spider):
    # identidade
    name = 'indeed'
    # Request

    def start_requests(self):
        # não esqueça de setar ROBOTSTXT_OBEY = False dentro do arquivo settings.py
        urls = ['https://br.indeed.com/jobs?q=python&l=&from=searchOnHP&vjk=467f2bd1131d76e0']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    # Response

    def parse(self, response):

        for elemento in response.xpath("//td[@class='resultContent']"):
            yield {
                'cargo': elemento.xpath(".//span[1]/text()").get(),
                'nome da empresa': elemento.xpath(".//span[@class='css-1x7z1ps eu4oa1w0']/text()").get(),
                'local': elemento.xpath(".//div[@class='css-t4u72d eu4oa1w0']/text()").get(),
                'link da vaga': 'https://br.indeed.com' + elemento.xpath(".//a/@href").get()
            }
        try:
            link_proxima_pagina = response.xpath("//a[data-testid='pagination-page-next']/@href").get()
            print('*'*10)
            print(link_proxima_pagina)
            print('*'*10)
            if link_proxima_pagina is not None:
                link_completo = 'https://br.indeed.com' + link_proxima_pagina
                print('*'*10)
                print(link_completo)
                print('*'*10)
                yield scrapy.Request(url=link_completo, callback=self.parse)
        except Exception as error:
            print(error)
            print('Chegamos na última página')
            

        