#!/usr/bin/env python3
#coding=utf-8
# @Time    : 2018/5/9 16:57
# @Author  : Changfa Wu
# @Site    :
# @File    : DecisionTree.py
# @Software: PyCharm
#爬取豆瓣电影top250
import requests
from lxml import etree

s = requests.Session()
#E:\学习\python\爬虫\系统学习爬虫\项目\豆瓣电影爬取
file_path = r'E:\学习\python\爬虫\系统学习爬虫\项目\豆瓣电影爬取\信息.txt'
for id in range(0, 251, 25):
    #https://movie.douban.com/top250?start=
    url = 'https://movie.douban.com/top250?start=' + str(id)
    r = s.get(url)
    r.encoding = 'utf-8'
    root = etree.HTML(r.content)
    items = root.xpath('//ol/li/div[@class="item"]')
    # print(len(items))
    for item in items:
        title = item.xpath('./div[@class="info"]//a/span[@class="title"]/text()')#取内容
        #title = item.xpath('./div[@class="info"]//p/text()')  # 取内容,xpath用法。
        name = title[0].encode('gb2312','ignore').decode('gb2312')#只取第一个中文名字。
        # rank = item.xpath('./div[@class="pic"]/em/text()')[0]
        rating = item.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]
        saying = item.xpath('.//div[@class="bd"]//span[@class="inq"]/text()')

        if not saying :#取反操作
            print(name, rating)
            with open(file_path, 'a',encoding='utf-8') as code:
                code.write(name + ' ' + rating + '\n')
        else:
            print(name, rating,saying[0])
            with open(file_path, 'a',encoding='utf-8') as code:#写入时定义写入文本的操作
                code.write(name+' '+rating+'   '+saying[0]+'\n')

