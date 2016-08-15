# *-* coding:utf-8 *-*
from scrapy import Spider
import scrapy
from bs4 import BeautifulSoup
import lxml
from ..items import LagouJobCategoryItem

class Lagou_job_category(Spider):
	"""docstring for Lagou_job_category"""
	name = 'lagou_job_categoty'
	allow_domains = ['lagou.com']
	headers = {
		'Accept': '*/*',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
		'Referer': 'http://www.lagou.com/',
		'Accept-Encoding': 'gzip, deflate, sdch',
		'Accept-Language': 'zh-CN,zh;q=0.8'
	}

	def start_requests(self):
		yield scrapy.Request(url='http://www.lagou.com/', headers=self.headers)


	def parse(self,response):
		soup = BeautifulSoup(response.body, 'lxml')
		item = LagouJobCategoryItem()
		menu_boxes= soup.find_all(class_='menu_box')
		for menu_main in menu_boxes:
			item['job_category_level1'] = menu_main.find(class_='menu_main job_hopping').h2.get_text().strip()
			for dl in menu_main.find(class_='menu_sub dn').find_all('dl'):
				item['job_category_level2'] = dl.dt.get_text().strip()
				for job_name in dl.dd.find_all('a'):
					item['job_name'] = job_name.get_text()
					item['job_url'] = job_name['href']
					yield item


