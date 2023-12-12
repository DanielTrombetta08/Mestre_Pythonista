from scrapy_sem_terminal import QuotesToScrapeSpider, CrawlerProcess

resposta = input('Devo iniciar a automação? (s/n)')

if resposta == 's':
    bot = CrawlerProcess(
    settings={
        "FEEDS": {
            "livros.json": {"format":"csv"}
        }
    }
    )

    bot.crawl(QuotesToScrapeSpider)
    bot.start()
else:
    print('Não será iniciado a automação')