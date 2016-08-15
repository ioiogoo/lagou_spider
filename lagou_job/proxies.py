from Proxies import Proxies
import time
import requests
import json

def get_proxie():
	a = Proxies(6)
	a.verify_proxies()
	proxies = a.proxies 
	with open('proxies.txt', 'a') as f:
		for proxy in proxies:
			if verify_lagou(proxy):
				f.write(proxy+'\n')

def verify_lagou(proxy):
	headers = {
	'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	'Accept-Encoding':'gzip, deflate',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
	}
	proxy = {'http': proxy}
	data = {'pn':'1', 'kd':'python'}
	url = 'http://www.lagou.com/jobs/positionAjax.json?px=default&city=%E4%B8%89%E4%BA%9A&needAddtionalResult=false'
	try:
		html = requests.post(url, data=data, headers=headers, proxies=proxy, timeout=5)
	# print html.content
	except:
		return False
	if html.status_code in [200]:
		try:
			json.loads(html.content)
		except ValueError:
			return False
		if html.url != url:
			return False
		print 'success %s' % proxy
		return True
	else:
		return False




if __name__ == '__main__':
	time.sleep(3600)
	while 1:
		proxies = []
		with open('proxies.txt', 'r') as f:
			for line in f:
				if verify_lagou(line.strip()):
					proxies.append(line.strip())
		with open('proxies.txt', 'w') as f:
			if len(proxies) != 0:
				for proxy in set(proxies):
					f.write(str(proxy)+'\n')


		# get_proxie()
		time.sleep(3600)

	# with open('proxies.txt', 'r') as f:
	# 	for line in f:
	# 		print verify_lagou(line.strip())