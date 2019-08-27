# -*- coding: utf-8 -*-
import scrapy

from ONCASE_NOTICIAS.items import OncaseNoticiasItem


class G1tecSpider(scrapy.Spider):
    name = 'G1Tec'
    allowed_domains = ['g1.globo.com']
    start_urls = ['https://g1.globo.com/economia/tecnologia']

    def parse(self, response):
        self.log('ACESSANDO URL: %s' % response.url)
        for article in response.css('.bastian-page .bastian-feed-item'):
          link    = article.css('a::attr(href)').extract_first()
          yield response.follow(link, self.parse_article)

    def parse_article(self, response):
      link   = response.url
      titulo = response.css('div.title h1::text').extract_first().strip()
      data = response.css('time::text').extract_first().strip()
      autor = response.css('.content-publication-data__from ::text').extract_first().strip()
      texto = "".join(response.css('.mc-article-body p::text').extract()).strip()
      tags  = ", ".join(response.css('.entities .entities__list-item a::text').extract()).strip()

      noticia = OncaseNoticiasItem(titulo=titulo, autor=autor, texto=texto, link=link, data=data, tags=tags)
      yield noticia
