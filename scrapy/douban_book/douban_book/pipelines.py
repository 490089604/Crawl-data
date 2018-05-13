# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanBookPipeline(object):
    def process_item(self, item, spider):
    	info = item['info'].split(' / ')#张嘉佳 / 湖南文艺出版社 / 2013-11-1 / CNY 39.80,从你的全世界路过
    	item['publisher'] = info[1]
    	item['edition_year'] = info[-2]
    	item['price'] = info[-1]
    	return item