import scrapy

# CamelCase
class QuotesToScrapeSpider(scrapy.Spider):
    # Identidade
    name = 'frasebot'
    # Request
    def start_requests(self):
        # Definir url(s) a varrer
        urls = ['https://quotes.toscrape.com/']

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)    
    # Response
    def parse(self, response):
        # aqui é onde você deve processar o que é retornado da response
        for elemento in response.xpath("//div[@class='quote']"):
            yield {
                'frase': elemento.xpath(".//span[@class='text']/text()").get(),
                'autor': elemento.xpath(".//small[@class='author']/text()").get(),
                'tags': elemento.xpath(".//a[@class='tag']/text()").getall()
            }