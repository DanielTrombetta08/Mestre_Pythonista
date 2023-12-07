# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# site que converte caracteres especiais "https://r12a.github.io/app-conversion/"

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join


def tirar_espaco_em_branco(valor):
    return valor.strip()

def processar_caracteres_especiais(valor):
    return valor.replace(u"\u2019", '')

def converter_maiusculo(valor):
    return valor.upper()


class CitacaoItem(scrapy.Item):
    frase = scrapy.Field(
        input_processor=MapCompose(tirar_espaco_em_branco, processar_caracteres_especiais),
        output_processor=TakeFirst()
    )
    autor = scrapy.Field(
        input_processor=MapCompose(tirar_espaco_em_branco,converter_maiusculo),
        output_processor=TakeFirst()
    )
    tags = scrapy.Field(
        output_processor=Join(';')
    )
