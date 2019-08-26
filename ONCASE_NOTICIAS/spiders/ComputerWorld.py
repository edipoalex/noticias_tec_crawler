# -*- coding: utf-8 -*-
import scrapy

from ONCASE_NOTICIAS.items import OncaseNoticiasItem


class ComputerworldSpider(scrapy.Spider):
    name = 'ComputerWorld'
    allowed_domains = ['computerworld.com.br']
    start_urls = ['http://computerworld.com.br/']

    def parse(self, response):
    	self.log('ACESSANDO URL: %s' % response.url)
    	for article in response.css('article'):
         	link    = article.css('a::attr(href)').extract_first()
         	yield response.follow(link, self.parse_article)


    def parse_article(self, response):
    	link   = response.url
    	title  = response.css('title ::text').extract_first()
    	author  = response.css('p.personalizado strong span::text').extract_first()
    	text   =  "".join(response.css('div.p-lr-15 p::text').extract())
    	data   = response.css('p.p-relative::text').extract_first().strip()
    	noticia = OncaseNoticiasItem(title=title, author=author, link=link, text=text, data=data)
    	yield noticia
        	
