# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()           #名字
    price = scrapy.Field()          #价格
    edition_year = scrapy.Field()   #编辑年份
    publisher = scrapy.Field()      #出版社
    ratings = scrapy.Field()        #评分
    info = scrapy.Field()			#信息
class DoubanMovieCommentItem(scrapy.Item):
    useful_num = scrapy.Field()      # 多少人评论有用
    no_help_num = scrapy.Field()     # 多少人评论无用
    people = scrapy.Field()          # 评论者
    people_url = scrapy.Field()      # 评论者页面
    star = scrapy.Field()            # 评分
    comment = scrapy.Field()         # 评论
    title = scrapy.Field()           # 标题
    comment_page_url = scrapy.Field()# 当前页