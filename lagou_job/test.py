# *-* coding:utf-8 *-*
import requests
import json
import MySQLdb
from Proxies import Proxies


# headers = {
# 	'Accept': '*/*',
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
# 	'Referer': 'http://www.lagou.com/',
# 	'Accept-Encoding': 'gzip, deflate, sdch',
# 	'Accept-Language': 'zh-CN,zh;q=0.8'
# }

headers = {
	'Accept':'application/json, text/javascript, */*; q=0.01',
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'zh-CN,zh;q=0.8',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	'Content-Length':'55',
	'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	'Host':'www.lagou.com',
	'Origin':'http://www.lagou.com',
	'Referer':'http://www.lagou.com/jobs/list_%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86?px=default&city=%E5%8C%97%E4%BA%AC',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
	'X-Anit-Forge-Code':'0',
	'X-Anit-Forge-Token':'None',
	'X-Requested-With':'XMLHttpRequest'
}

def get_page_job_category(job_name, cityname):
	url = 'http://www.lagou.com/jobs/positionAjax.json?city=%s' % cityname
	page = 1
	while 1:
		data = {
		'pn':page,
		'kd':job_name
		}
		html = requests.post(url, data=data, headers=headers).content
		html = json.loads(html)
		if html.get('content').get('positionResult').get('resultSize') == 0:
			break
		print html.get('content').get('positionResult').get('resultSize'), page
		page += 1
	print page

def create_db():
	conn = MySQLdb.connect(host='localhost', user='root', passwd='qwer', charset='utf8', db='lagou')
	cur = conn.cursor()
	sql = 'create table job_info(id int(8) auto_increment primary key,companyLogo varchar(255),salary varchar(255),city varchar(255),financeStage varchar(255),industryField varchar(255),approve varchar(255),positionAdvantage varchar(255),positionId varchar(255),companyLabelList varchar(255),score varchar(255),companySize varchar(255),adWord varchar(255),createTime varchar(255),companyId varchar(255),positionName varchar(255),workYear varchar(255),education varchar(255),jobNature varchar(255),companyShortName varchar(255),district varchar(255),businessZones varchar(255),imState varchar(255),lastLogin varchar(255),publisherId varchar(255),explain varchar(255),plus varchar(255),pcShow varchar(255),appShow varchar(255),deliver varchar(255),gradeDescription varchar(255),companyFullName varchar(255),formatCreateTime varchar(255))'
	cur.execute(sql)
	conn.commit()
	conn.close()

if __name__ == '__main__':
	
	a = Proxies()
	a.verify_proxies()
	print a.proxies