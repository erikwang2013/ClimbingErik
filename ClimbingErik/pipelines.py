# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os,time

class ClimbingerikPipeline(object):
    def process_item(self, item, spider):
#        print("文章分类",item['category'])
#        print("文章名称",item['title'])
#        print("文章链接",item['title_url'])
        pathGet=os.getcwd()
        times=time.strftime("%Y%m%d", time.localtime())
        filePath=pathGet+'/data/'+times+'.txt'
        fileData=open(filePath,'a')
        getData=item['title']+":"+item['title_url']
        fileData.write("\n"+getData)
        fileData.flush()
        fileData.close()
        return item
