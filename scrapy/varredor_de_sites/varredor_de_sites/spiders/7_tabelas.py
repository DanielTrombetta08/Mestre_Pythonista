import scrapy

class ProxyScraperSpider(scrapy.Spider):
    # identidade
    name = 'proxyscraper'
    # Request
    def start_requests(self):
        urls = ['https://www.us-proxy.org/']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    # Response
    def parse(self, response):
        # Montar um xpath que retorna a linha
        for linha in response.xpath("//table[@class='table table-striped table-bordered']//tr"):
            yield {
                # Montar individualmente um xpath que retorna cada item daquela  linha
                'ip_adress': linha.xpath('./td[1]/text()').get(),
                'port': linha.xpath('./td[2]/text()').get(),
                'code': linha.xpath('./td[3]/text()').get(),
                'country': linha.xpath('./td[4]/text()').get(),
                'anonymity': linha.xpath('./td[5]/text()').get(),
                'google': linha.xpath('./td[6]/text()').get(),
                'https': linha.xpath('./td[7]/text()').get(),
                'last_checked': linha.xpath('./td[8]/text()').get()
            }