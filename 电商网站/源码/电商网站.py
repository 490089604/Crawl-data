#!/usr/bin/env python3
#coding=utf-8
# @Time    : 2018/5/9 16:57
# @Author  : Changfa Wu
# @Site    :
# @File    : DecisionTree.py
# @Software: PyCharm
#用selenium爬取电商网站图片
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os.path
import base64
import requests#更好的方案是使用requests
#selenium主要是用来做自动化测试，支持多种浏览器，爬虫中主要用来解决JavaScript渲染问题。
#模拟浏览器进行网页加载，当requests,urllib无法正常获取网页内容的时候
#解决1个问题
browser = webdriver.Chrome()#chrome的驱动器
browser.set_page_load_timeout(30)#等待超时不超过30秒
browser.maximize_window()  #将浏览器最大化
browser.get('http://www.17huo.com/newsearch/?k=%E5%A4%A7%E8%A1%A3')
#阴影对后续有影响所以去掉了
browser.find_element_by_css_selector('body > div.boot_mask > div').click()
page_info = browser.find_element_by_css_selector('body > div.wrap > div.search_container > div.pagem.product_list_pager > div')
#共多少页多少条
#print(page_info.text)
pages = int((page_info.text.split('，')[0]).split(' ')[1])
print ('商品共有%d页' %pages)
for page in range(pages):
    if page > 2:#获取前三页信息
        break
    #url = 'http://www.17huo.com/?mod=search&sq=2&keyword=%E7%BE%8A%E6%AF%9B&page=' + str(page + 1)
    url = 'http://www.17huo.com/newsearch/?k=%E5%A4%A7%E8%A1%A3&page=' +str(page+1)
    browser.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")#因为页面时滚动加载的，所以要模拟一个滚动的操作
    time.sleep(5)   # 不然会load不完整
    goods = browser.find_element_by_css_selector('body > div.wrap > div.search_container > div.book-item-list.clearfix').find_elements_by_class_name('book-item-list-box')
    print('%d页有%d件商品' % ((page + 1), len(goods)))
    count=0
    bool_jpg=1
    content=None
    for good in goods:
        print('第%d页第%d件商品' %(page+1,count))
        count=count+1
        try:
            title = good.find_element_by_css_selector('a > div.book-item-top.clearfix').text
            price = good.find_element_by_css_selector('a > div.book-item-mid.clearfix > div.book-item-price > span').text
            #body > div.wrap > div.search_container > div.book-item-list.clearfix > div:nth-child(1) > a > div.img_box > img
            this_download_url=good.find_element_by_css_selector('a > div.img_box > img').get_attribute('data-original')
            print('图片地址',this_download_url)
            #错误原因，base64'这里不用管它，这里获得的不全，导致图片无法写入
            if 'data:image/png' in this_download_url:
                #pass
                bool_jpg = 0
                #content = base64.b64decode(this_download_url[22:])
                content = this_download_url[22:]
                print('base64')
            else:
                r = requests.get(this_download_url.strip(), stream=True)
                content =r.content
            print(title, price+'元')
            #E:\学习\python\爬虫\系统学习爬虫\电商网站
            file_path = r'E:\学习\python\爬虫\系统学习爬虫\电商网站\信息.txt'
            if bool_jpg == 0 :
                picture_path = r'E:\学习\python\爬虫\系统学习爬虫\电商网站\图片\\'[:-1] + title + '.png'
            else:
                picture_path=r'E:\学习\python\爬虫\系统学习爬虫\电商网站\图片\\'[:-1]+title+'.jpg'
            # 下载文件
            #with open(file_path, 'a') as code:
                #code.write(title+' '+price+'元\n')
            if (os.path.isfile(picture_path)):
                print('exist')
            else:
                with open(picture_path, 'wb') as code:
                    code.write(content)
        except Exception as e:
            print(e,"商品信息",good.text)
        finally:
            with open(file_path, 'a') as code:
                code.write(title+' '+price+'元\n')
print('爬完啦')
#<img class="book-item-list-box-img lazy" data-original="http://img0.17huo.com/./01/2017-12-23/9d1e85f1fb449247176b5fafc2d62a60_250x250.jpg" src="http://img0.17huo.com/./01/2017-12-23/9d1e85f1fb449247176b5fafc2d62a60_250x250.jpg" style="display: inline;">
#<img class="book-item-list-box-img lazy" data-original="http://img0.17huo.com/./01/2018-01-02/dc207a46eefc2e79448e831b084ebbb4_250x250.jpg" src="http://img0.17huo.com/./01/2018-01-02/dc207a46eefc2e79448e831b084ebbb4_250x250.jpg" style="display: inline;">
'''
base64代码
import base64
转换后的代码特长
def convert(image):
    f = open(image)
    img_raw_data = f.read()
    f.close()
 
    img_b64_string = base64.b64encode(img_raw_data)
    convert_img_raw_data = base64.b64decode(img_b64_string)
 
    t = open("example.png", "w+")
    t.write(convert_img_raw_data)
    t.close()
 
if __name__ == "__main__":
    convert("test.png")
'''