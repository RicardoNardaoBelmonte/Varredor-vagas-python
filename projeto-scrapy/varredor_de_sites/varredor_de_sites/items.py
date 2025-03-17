# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Join


def tirar_espaço(valor):
    return valor.strip()

def transformar_maiscula(valor):
    return valor.upper()

def remover_aspas(valor):
    return valor.replace(u"\u2019", '')

class Citacoes(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    frase = scrapy.Field(
        input_processor= MapCompose(remover_aspas, tirar_espaço),
        output_processor= TakeFirst()
    )

    author = scrapy.Field(
        input_processor= MapCompose(tirar_espaço, transformar_maiscula),
        output_processor= TakeFirst()
    )

    tags = scrapy.Field(
            output_processor= Join(';')
        )