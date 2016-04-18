# coding=utf-8
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from scrapy.contrib.linkextractors import LinkExtractor

from neituijob.items import NeituijobItem

__author__ = 'zjutK'

add=0
class neituijobSpider(CrawlSpider):
    name = 'neituijob'
    allowed_domains = 'neitui.me'
    start_urls = [
        'http://www.neitui.me/',
    ]
    rules = (
        Rule(LxmlLinkExtractor(allow=("\?name\=job&handle\=detail&id\=\d{6}&from\=index")), callback="parse_item"),
        Rule(LxmlLinkExtractor(allow=('neitui\/page\=\d{,3}\.html'))),

    )
    def parse_item(self, response):
        global add
        print add
        add=add+1
        items = []
        item = NeituijobItem()
        item['name'] = response.xpath('//*[@id="detail"]/div/ul/li/div[2]/div[2]/strong').extract()
        item['company'] = response.xpath('//*[@id="detail"]/div/ul/li/div[2]/div[3]/span[1]').extract()
        item['work_location'] = response.xpath('//*[@id="detail"]/div/ul/li/div[2]/div[3]/span[2]').extract()
        item['recruit_require'] = response.xpath('//*[@id="detail"]/div/ul/li/div[2]/div[2]/span[2]').extract()
        item['company_tag'] = response.xpath('//*[@id="detail"]/div/ul/li/div[2]/div[4]/ul').extract()
        item['publish_time'] = response.xpath('//*[@id="detail"]/div/ul/li/div[2]/div[1]').extract()
        item['data'] = response.xpath('//*[@id="detail"]/div/ul/li/div[2]/div[7]').extract()
        items.append(item)
        return items
