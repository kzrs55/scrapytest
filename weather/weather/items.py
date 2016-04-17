# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    date = scrapy.Field()
    day_of_week = scrapy.Field()
    temperature = scrapy.Field()
    wind_power = scrapy.Field()
    air_quality = scrapy.Field()
    air_quality_score=scrapy.Field()
    pass
