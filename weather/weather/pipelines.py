# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WeatherPipeline(object):
    def __init__(self):
        pass
    def process_item(self, item, spider):
        with open('wea.txt','w+') as file:
            city=item['city'][0].encode('utf-8')
            file.write('city:'+str(city))
            date=item['date']
            day_of_week=item['day_of_week']
            air_quality=item['air_quality']
            air_quality_score=item['air_quality_score']
            temperature=item['temperature']
            wind_power=item['wind_power']
            weaitem=zip(date,day_of_week,air_quality,air_quality_score,temperature,wind_power)
            for i in range(len(weaitem)):
                txt ='日期:{0}\t周几:{1}\n空气质量:{2}\t空气质量评分:{3}\n温度:{4}\t风力:{5}\n'.format(
                    weaitem[i][0].encode('utf-8'),
                    weaitem[i][1].encode('utf-8'),
                    weaitem[i][2].encode('utf-8'),
                    weaitem[i][3].encode('utf-8'),
                    weaitem[i][4].encode('utf-8'),
                    weaitem[i][5].encode('utf-8'),
                )
                file.write(txt)
        return item
