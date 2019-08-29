from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

settings = get_project_settings()
process = CrawlerProcess(settings)
excludes = ["xxx"] #Caso deseje excluir algum spider da execução

for spider_name in process.spider_loader.list():
    print ("Running spider %s" % (spider_name))
    if spider_name in excludes:
                continue
    spider_cls = process.spider_loader.load(spider_name)
    process.crawl(spider_cls)
process.start()
print ("End spider")
