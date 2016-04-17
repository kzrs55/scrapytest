# coding=utf-8
import scrapy
from weather.items import WeatherItem

__author__ = 'zjutK'


class WeatherSpider(scrapy.Spider):
    name = "SinaWeather"
    allowed_domains = ["sina.com.cn"]
    start_urls = ['http://weather.sina.com.cn/']

    def parse(self, response):
        item = WeatherItem()
        item['city'] = response.xpath('//*[@id="slider_ct_name"]/text()').extract()
        tenday=response.xpath('//*[@id="blk_fc_c0_scroll_w"]')
        item['date'] = tenday.css('p.wt_fc_c0_i_date::text').extract()
        item['day_of_week'] = tenday.css('p.wt_fc_c0_i_day::text').extract()
        item['temperature'] = tenday.css('p.wt_fc_c0_i_temp::text').extract()
        item['wind_power'] = tenday.css('p.wt_fc_c0_i_tip::text').extract()
        item['air_quality'] = tenday.css('ul > li.l::text').extract()
        item['air_quality_score'] = tenday.css('ul > li.r::text').extract()
        return item
