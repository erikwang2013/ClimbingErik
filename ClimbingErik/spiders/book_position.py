# -*- coding: utf-8 -*-
import scrapy
from ClimbingErik.items import ClimbingerikItem
class BookPositionSpider(scrapy.Spider):
    name = 'book_position'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://xbiquge.la/xiaoshuodaquan/']

    def parse(self, response):
        for clim_primary in response.xpath('//div[@class="novellist"]'):
            for getData in clim_primary.xpath('//ul'):
                for getliData in getData.xpath('//li'):
                    item=ClimbingerikItem()
                    item['title']=getliData.xpath('./a/text()').extract_first()
                    item['title_url']=getliData.xpath('./a/@href').extract_first()
                    yield item
        pass
