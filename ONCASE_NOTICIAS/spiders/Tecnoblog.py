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
      title  = response.css('title ::text').extract_first()
      author = response.css('span.author ::text').extract_first()
      text   =  "".join(response.css('div.entry ::text').extract())
      data   = None # response.css("meta[property=article:published_time] ::attr(content)").extract()

      noticia = OncaseNoticiasItem(title=title, author=author, text=text, link=link, data=data)
      yield noticia

    '''def parse(self, response):
        for article in response.css("article"):
        	link    = article.css("div.texts h2 a::attr(href)").extract_first()
        	title   = article.css("div.texts h2 a::text").extract_first()
        	author  = article.css("div.texts div.info a::text").extract_first()
        	texto   = article.css("div.texts div.entry p::text").extract_first()

        	noticia = OncaseNoticiasItem(title=title, author=author, link=link, texto=texto)

        	yield noticia
        	# {'link': link, 'title': title, 'author': author, 'texto': texto}'''
