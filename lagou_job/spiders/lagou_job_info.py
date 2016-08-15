# *-* coding:utf-8 *-*
from scrapy import Spider
import scrapy
import requests
import json
import MySQLdb
import itertools
import json
import urllib
from ..items import LagouJobInfo
from scrapy import log

class Lagou_job_info(Spider):
	"""docstring for Lagou_job_info"""
	name = 'lagou_job_info'

	def __init__(self):
		super(Lagou_job_info, self).__init__()
		# 得到城市名
		self.citynames = self.get_citynames()
		# 职业类型
		self.job_names = self.get_job_names()
		# 两两组合城市名和职业类型
		self.url_params = [x for x in itertools.product(self.citynames, self.job_names)]
		self.url = 'http://www.lagou.com/jobs/positionAjax.json?px=default&city=%s&needAddtionalResult=false'
		self.headers = {
			'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
			'Accept-Encoding':'gzip, deflate',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
		}
		


	def get_citynames(self):
		'''从数据库查询得到城市名'''
		conn = MySQLdb.connect(host='localhost', user='root', passwd='qwer', charset='utf8', db='lagou')
		cur = conn.cursor()
		sql = 'select cityname from city where id>0 order by id'
		cur.execute(sql)
		results = cur.fetchall()
		cur.close()
		conn.close()
		return [str(x[0].encode('utf-8')) for x in results]

	def get_job_names(self):
		'''从数据库查询得到职业类型'''
		conn = MySQLdb.connect(host='localhost', user='root', passwd='qwer', charset='utf8', db='lagou')
		cur = conn.cursor()
		sql = 'select job_name from job_category where id <=105'
		cur.execute(sql)
		results = cur.fetchall()
		cur.close()
		conn.close()
		return [str(x[0].encode('utf-8')) for x in results]


	def start_requests(self):
		'''从self.parms开始组合url并且生成request对象'''
		for url_param in self.url_params:
			url = self.url % urllib.quote(url_param[0])
			yield scrapy.FormRequest(url=url, formdata={'pn':'1', 'kd':url_param[1]}, method='POST', headers=self.headers, meta={'page':1, 'kd':url_param[1]}, dont_filter=True)
			# return [scrapy.Request('http://www.baidu.com')]
			# return []

	def parse(self, response):
		'''进一步处理生成的request对象'''
		try:
			html = json.loads(response.body)
		# 可能会出现安全狗的拦截，返回的并不是json数据
		except ValueError:
			log.msg(response.body, level=log.ERROR)
			log.msg(response.status, level=log.ERROR)
			# 需要重新生成当前的request对象
			yield scrapy.FormRequest(response.url, formdata={'pn':str(response.meta.get('page')), 'kd':response.meta.get('kd')}, headers=self.headers, meta={'page':response.meta.get('page'), 'kd':response.meta.get('kd')}, dont_filter=True) 
		# 判断当前页是否有内容
		if html.get('content').get('positionResult').get('resultSize') != 0:
			results = html.get('content').get('positionResult').get('result')
			for result in results:
				item = LagouJobInfo()
				item['keyword'] = response.meta.get('kd')
				item['companyLogo'] = result.get('companyLogo')
				item['salary'] = result.get('salary')
				item['city'] = result.get('city')
				item['financeStage'] = result.get('financeStage')
				item['industryField'] = result.get('industryField')
				item['approve'] = result.get('approve')
				item['positionAdvantage'] = result.get('positionAdvantage')
				item['positionId'] = result.get('positionId')
				if isinstance(result.get('companyLabelList'), list):
					item['companyLabelList'] = ','.join(result.get('companyLabelList'))
				else:
					item['companyLabelList'] = ''
				item['score'] = result.get('score')
				item['companySize'] = result.get('companySize')
				item['adWord'] = result.get('adWord')
				item['createTime'] = result.get('createTime')
				item['companyId'] = result.get('companyId')
				item['positionName'] = result.get('positionName')
				item['workYear'] = result.get('workYear')
				item['education'] = result.get('education')
				item['jobNature'] = result.get('jobNature')
				item['companyShortName'] = result.get('companyShortName')
				item['district'] = result.get('district')
				item['businessZones'] = result.get('businessZones')
				item['imState'] = result.get('imState')
				item['lastLogin'] = result.get('lastLogin')
				item['publisherId'] = result.get('publisherId')
				# item['explain'] = result.get('explain')
				item['plus'] = result.get('plus')
				item['pcShow'] = result.get('pcShow')
				item['appShow'] = result.get('appShow')
				item['deliver'] = result.get('deliver')
				item['gradeDescription'] = result.get('gradeDescription')
				item['companyFullName'] = result.get('companyFullName')
				item['formatCreateTime'] = result.get('formatCreateTime')
				yield item
			# 当前页处理完成后生成下一页的request对象
			page = int(response.meta.get('page')) + 1
			kd = response.meta.get('kd')
			yield scrapy.FormRequest(response.url, formdata={'pn':str(page), 'kd':kd}, headers=self.headers, meta={'page':page, 'kd':kd}, dont_filter=True)


		