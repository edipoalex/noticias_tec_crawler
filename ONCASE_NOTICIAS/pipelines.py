# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonItemExporter

from datetime import datetime
from elasticsearch import Elasticsearch, helpers
from six import string_types

import logging
import hashlib
import types
import pymongo

class OncaseNoticiasPipeline(object):
	collection_name = 'noticias_tec'
	def __init__(self, mongo_uri, mongo_db):
		self.mongo_uri = mongo_uri
		self.mongo_db = mongo_db
	 	# self.file = open("noticias.json", 'wb')
	 	# self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
	 	# self.exporter.start_exporting()

	@classmethod
	def from_crawler(cls, crawler):
		return cls(
			mongo_uri=crawler.settings.get('MONGO_URI'),
			mongo_db=crawler.settings.get('MONGO_DATABASE', 'ONCASE_NOTICIAS')
		)

	def open_spider(self, spider):
		self.client = pymongo.MongoClient(self.mongo_uri)
		self.db = self.client[self.mongo_db]

	def close_spider(self, spider):
	 	self.exporter.finish_exporting()
	 	self.file.close()

	def process_item(self, item, spider):
		self.db[self.collection_name].find_one_and_update(
			{"link": item["link"]},
			{"$set": dict(item)},
			upsert=True
		)
		return item
		# self.db[self.collection_name].insert_one(dict(item))
	 	# self.exporter.export_item(item)
	 	# line =  json.dumps(dict(item)) + '\n'
	 	# self.file.write(line)
	 	
