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
		name = Selector(response).xpath('//*[@id="body"]/div[8]/div/div[1]/section/div[1]/div[1]/ul[1]/li[1]/a')
		news = Selector(response).xpath('//*[@id="body"]/div[8]/div/div[1]/section/div[1]/div[1]/ul[1]/li[2]/a')
		heading = Selector(response).xpath('//*[@id="body"]/div[3]/div[1]/section/ul[1]')
		path = Selector(response).xpath('//*[@id="global-nav-exp"]/ul/li[10]/h3/a')
		sports = Selector(response).xpath('//*[@id="global-nav-exp"]/ul/li[11]/h3/a')
		entertainment = Selector(response).xpath('//*[@id="global-nav-exp"]/ul/li[12]/h3/a')
		alag = Selector(response).xpath('//*[@id="global-nav-exp"]/ul/li[15]/h3/a')
		item['news'] = news
		item['alag'] = alag
		item['entertainment'] = entertainment
		item['sports'] = sports
		item['path'] = path
		item['heading'] = heading
		item['name'] = name
		yield item
