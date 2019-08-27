# -*- coding: utf-8 -*-
import scrapy

from ONCASE_NOTICIAS.items import OncaseNoticiasItem


class TecnoblogSpider(scrapy.Spider):
    name = 'Tecnoblog'
    allowed_domains = ['tecnoblog.net']
    start_urls = ['http://tecnoblog.net/']

    def parse(self, response):
    	self.log('ACESSANDO URL: %s' % response.url)
    	for article in response.css('article'):
    		link    = article.css('div.texts h2 a::attr(href)').extract_first()
    		yield response.follow(link, self.parse_article)


    def parse_article(self, response):
      link   = response.url
      titulo  = response.css('title ::text').extract_first().strip()
      autor = response.css('span.author ::text').extract_first().strip()
      texto   =  "".join(response.css('div.entry ::text').extract()).strip()
      data   = response.css('.by span::text')[1].extract().strip()
      tags   =  ", ".join(response.css('.tags a::text').extract()).strip()

      noticia = OncaseNoticiasItem(titulo=titulo, autor=autor, texto=texto, link=link, data=data, tags=tags)
      yield noticia
