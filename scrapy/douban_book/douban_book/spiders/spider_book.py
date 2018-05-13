import scrapy
from douban_book.items import DoubanBookItem
"""
启动方法：E:\学习\python\爬虫\系统学习爬虫\项目\scrapy\douban_book> scrapy crawl cfwu_book -o book_list.csv
"""
class book_spider(scrapy.Spider):
	"""docstring for book_spider"""
	name = 'cfwu_book'
	allowed_domain = ['douban.com']#满足某些网站的域名允许爬取
	start_urls = ['https://book.douban.com/top250']

	def parse(self,response):#调用此函数是已经执行过一次爬取，内容放在response中 
		#框架会自动去重。首先请求第一页
		yield  scrapy.Request(response.url,callback=self.parse_next)#第一个参数是要执行的url,第二个是执行的函数不带括号
		#//*[@id="content"]/div/div[1]/div/div/a[1]
		for page in response.xpath('//div[@class="paginator"]/a'):
			link = page.xpath('@href').extract()[0]#返回字符串，取第一个
			yield  scrapy.Request(link,callback=self.parse_next)#给调度器返回链接
	def parse_next(self,response):
		#pass
		#//*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[2]/div[1]/a
		#//*[@id="content"]/div/div[1]/div/table[2]/tbody/tr/td[2]/div[1]/a
		#//*[@id="content"]/div/div[1]/div/table[1]
		for items in response.xpath('//tr[@class="item"]'):
			book = DoubanBookItem()
			#/tr/td[2]/div[1]/a
			book['name'] = items.xpath('td[2]/div[1]/a/@title').extract()[0]
			book['ratings'] = items.xpath('//span[@class="rating_nums"]/text()').extract()[0]
			#td[2]/p[1]
			book['info'] = items.xpath('td[2]/p[1]/text()').extract()[0]
			yield book #返回内容

	