# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NeituijobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 职位名称
    company = scrapy.Field()  # 公司名称
    work_location = scrapy.Field()  # 工作地点
    recruit_number = scrapy.Field()  # 招聘人数
    detail_link = scrapy.Field()  # 职位详情页链接
    publish_time = scrapy.Field()  # 发布时间
    data = scrapy.Field()  # 职位详情
    pass
