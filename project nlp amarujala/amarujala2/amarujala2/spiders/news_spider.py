import scrapy
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule
from nlp.items import nlpItem

class MySpider(BaseSpider):
    name = "Amarujala"
    allowed_domains = ["amarujala.com"]
    start_urls = ["http://www.amarujala.com/"]

    def parse(self,response):
        item=nlpItem()
        news_source=Selector(response).xpath('//div[@class="news-channels-logo-txt"]/text()').extract()
        news_summary=Selector(response).xpath('//div[@class="news-channel-caption"]/span/a/text()').extract()
        news_date=Selector(response).xpath('//div[@class="news-channel-caption"]/span/small/text()').extract() 
        news_image = Selector(response).xpath('//div[@class="caption-img"]/img/@data-src').extract()

        item['news_source']=news_source
        item['news_summary']=news_summary
        item['news_image']=news_image
        item['news_date']=news_date

        yield item


    
