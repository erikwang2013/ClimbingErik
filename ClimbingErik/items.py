# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ClimbingerikItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #分类名称
    category=scrapy.Field();
    #文章名称
    title=scrapy.Field()
    #文章地址
    title_url=scrapy.Field()
    #文章作者
    author=scrapy.Field()
    pass
