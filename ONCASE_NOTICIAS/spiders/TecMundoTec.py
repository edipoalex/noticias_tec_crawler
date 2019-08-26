# -*- coding: utf-8 -*-
import scrapy

from ONCASE_NOTICIAS.items import OncaseNoticiasItem


class TecmundotecSpider(scrapy.Spider):
    name = 'TecMundoTec'
    allowed_domains = ['www.tecmundo.com.br']
    start_urls = ['https://www.tecmundo.com.br/novidades/']

    def parse(self, response):
    	self.log('ACESSANDO URL: %s' % response.url)
    	for article in response.css('article'):
    		link    = article.css('h3 a::attr(href)').extract_first()
    		yield response.follow(link, self.parse_article)

    def parse_article(self, response):
      link   = response.url
      title = response.css('title::text').extract_first()
      data = response.css('time strong ::text').extract_first()
      author = response.css('a.tec--author__info__link::text').extract_first()
      text = "".join(response.css("div.p402_premium p::text").extract())
      noticia = OncaseNoticiasItem(title=title, author=author, text=text, link=link, data=data)
      yield noticia
