# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonItemExporter

from datetime import date
from datetime import datetime
from elasticsearch import Elasticsearch, helpers
from six import string_types

import logging
import hashlib
import types
import pymongo
import regex
import collections

class OncaseNoticiasPipeline(object):
	collection_name = 'NOTICIAS'
	def __init__(self, mongo_uri, mongo_db):
		self.mongo_uri = mongo_uri
		self.mongo_db = mongo_db


	@classmethod
	def from_crawler(cls, crawler):
		return cls(
			mongo_uri=crawler.settings.get('MONGO_URI'),
			mongo_db=crawler.settings.get('MONGO_DATABASE', 'ONCASE_NOTICIAS')
		)

			
	def proc_words(self, text):
		words = text.split()
		qtd=0
		for word in words:
			qtd=qtd+1
		
		return qtd

	
	
	def top_words(self, text):
		words=[]
		words_exc = ["de","da","do","a","para","se","por","o","e","que","em","ao", "no","na","os","—", "as", "dos","das","nos","nas", "com","ou","é","uma","um","uns","umas","sua","seu","suas","seus","são","como","ele","ela","tem","mas","à"]
		for word in text.split():
			if not word.lower() in words_exc:
				words.append(word)
			# Contador para as ocorrencias de cada palavra
			c = collections.Counter(words)
		palavras=''
		for item in c.most_common(10):
			palavras=palavras + str(item)
		return palavras
		

	def open_spider(self, spider):
		self.client = pymongo.MongoClient(self.mongo_uri)
		self.db = self.client[self.mongo_db]

	def close_spider(self, spider):
	 	self.client.close()

	def process_item(self, item, spider):
		if item["autor"] is None:
			item["autor"]="Não Informado"

		#item["qtd_palavras"] = self.proc_words(regex.sub(r'["-,”“.:@#?!&$]', ' ', item["texto"]))
		#item["top_palavras"] = self.top_words(regex.sub(r'["-,”“.:@#?!&$]', ' ', item["texto"]))
		item["qtd_palavras"] = self.proc_words(item["texto"])
		item["top_palavras"] = self.top_words(item["texto"])
		item["dt_captura"] = str(date.today())
		item["data"] = str(datetime.strptime(item["data"][0:10], '%d/%m/%Y').date())
		

		self.db[self.collection_name].find_one_and_update(
			{"link": item["link"]},
			{"$set": dict(item)},
			upsert=True
		)
		return item





