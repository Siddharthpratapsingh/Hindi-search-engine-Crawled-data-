# -*- coding: utf-8 -*-
import scrapy
from scrapy import spider
from scrapy.selector import Selector
from sumansa.items import SumansaItem


class Spi2Spider(scrapy.Spider):
	name = "spi2"
	allowed_domains = ["sumansa.com"]
	start_urls = ('http://www.sumansa.com/',)

	def parse(self, response):
		item = SumansaItem()
		news = Selector(response).xpath('/html/body/div[6]/div/div[2]/div/div[1]/div/div[13]/h4/a/text()')
		item['news'] = news
		yield item

		
     
