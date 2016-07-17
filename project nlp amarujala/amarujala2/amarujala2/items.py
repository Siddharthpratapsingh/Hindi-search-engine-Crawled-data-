import scrapy from scrapy.item
import Item,Field



class Amarujala2Item(scrapy.Item):
    news_source=scrapy.Field()
    news_summary=scrapy.Field()
    news_date=scrapy.Field()
    news_image=scrapy.Field()# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

