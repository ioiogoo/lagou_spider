import random
import scrapy
from scrapy import log


# logger = logging.getLogger()

class ProxyMiddleWare(object):
	"""docstring for ProxyMiddleWare"""
	def process_request(self,request, spider):
		'''对request对象加上proxy'''
		proxy = self.get_random_proxy()
		request.meta['proxy'] = 'http://%s' % proxy 
		# print 'use proxy'
		log.msg('-'*10, level=log.DEBUG)
		log.msg(request.body.encode('utf-8'), level=log.DEBUG)
		log.msg(proxy, level=log.DEBUG)
		log.msg('-'*10, level=log.DEBUG)
		# print request.headers
		


	def process_response(self, request, response, spider):
		'''对返回的response处理'''
		# 如果返回的response状态不是200，重新生成当前request对象
		if response.status != 200:
			log.msg('-'*10, level=log.ERROR)
			log.msg(response.url, level=log.ERROR)
			log.msg(request.body.encode('utf-8'), level=log.ERROR)
			log.msg(response.status, level=log.ERROR)
			log.msg(request.meta['proxy'], level=log.ERROR)
			log.msg('proxy block!', level=log.ERROR)
			log.msg('-'*10, level=log.ERROR)
			proxy = self.get_random_proxy()
			# 对当前reque加上代理
			request.meta['proxy'] = 'http://%s' % proxy 
			return request
		return response

	def get_random_proxy(self):
		'''随机从文件中读取proxy'''
		while 1:
			with open('proxies.txt', 'r') as f:
				proxies = f.readlines()
			if proxies:
				break
			else:
				time.sleep(1)
		proxy = random.choice(proxies).strip()
		return proxy