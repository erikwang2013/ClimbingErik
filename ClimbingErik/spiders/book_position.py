# -*- coding: utf-8 -*-
import scrapy,time
from ClimbingErik.items import ClimbingerikItem
from selenium import webdriver
class BookPositionSpider(scrapy.Spider):
    browser=webdriver.Firefox(executable_path="browser/geckodriver")
    time.sleep(3)
    browser.get("http://xbiquge.la/xiaoshuodaquan/")
    time.sleep(5)
    name = 'book_position'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://xbiquge.la/xiaoshuodaquan/']

    def parse(self, response):
        for clim_primary in response.xpath('//div[@class="novellist"]'):
            for getData in clim_primary.xpath('//div[@class="novellist"]/ul'):
                for getliData in getData.xpath('//div[@class="novellist"]/ul/li'):
                    item=ClimbingerikItem()
                    item['title']=getliData.xpath('./a/text()').extract_first()
                    item['title_url']=getliData.xpath('./a/@href').extract_first()
                    yield item
