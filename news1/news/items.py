# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy 
from scrapy.item import Item, Field


class NewsItem(scrapy.Item):
	
	name = scrapy.Field()
	heading = scrapy.Field()
	path = scrapy.Field()
	sports = scrapy.Field()
	entertainment = scrapy.Field()
	alag = scrapy.Field()
	news = scrapy.Field()
	national = scrapy.Field()
	#pass
