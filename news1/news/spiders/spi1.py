# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from news.items import NewsItem


class Spi1Spider(scrapy.Spider):
	name = "spi1"
	allowed_domains = ["www.amarujala.com"]
	start_urls = ['http://www.amarujala.com/']

	def parse(self, response):
		item = NewsItem()
		name = Selector(response).xpath('//div[@class="lvdskLst"]/div/h3/a/@title').extract()
		news = Selector(response).xpath('//section[@class="pd10 auw-lazy-load"]/ul/li/a/text()').extract()
		heading = Selector(response).xpath('//*[@id="body"]/div/ul/h3/a/text()').extract()
		path = Selector(response).xpath('//*[@id="global-nav-exp"]/div/ul/li/h3/a/@title').extract()
		sports = Selector(response).xpath('//*[@id="global-nav-exp"]/div/h3/a/text()').extract()
		entertainment = Selector(response).xpath('//*[@id="global-nav-exp"]/ul/li/h3/a/@title').extract()
		alag = Selector(response).xpath('//div[@class="mostRdr left auw-story"]/section/h3/a/text()').extract()
		national = Selector(response).xpath('//div[@class="mostRdr left auw-story"]/section/h3/a/text()').extract()
		item['news'] = news
		item['alag'] = alag
		item['entertainment'] = entertainment
		item['sports'] = sports
		item['path'] = path
		item['heading'] = heading
		item['name'] = name
		item['national'] = national
		yield item
