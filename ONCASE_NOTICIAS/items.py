# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OncaseNoticiasItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titulo = scrapy.Field()
    autor = scrapy.Field()
    texto = scrapy.Field()
    link = scrapy.Field()
    data = scrapy.Field()
    tags = scrapy.Field()
    qtd_palavras = scrapy.Field()
    top_palavras = scrapy.Field()
    dt_aquisicao = scrapy.Field()
