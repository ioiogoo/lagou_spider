# Lagou_job
使用scrapy、mysql，实现对拉勾网招聘信息的爬虫，使用Proxies定时更新代理池并检测代理的可用性。
这个项目是为我之后对[拉勾网的招聘信息进行分析](https://github.com/ioiogoo/internet_job_analysis)的前置项目，获取数据保存到mysql。

* 更新代理池。通过[Proxies](https://github.com/ioiogoo/Proxies_)获取并保存到根目录下proxies.txt文件
* 数据存储在mysql数据库中，主要字段包括：
  * keyword `职业类型`
  * salary `工资`
  * companySize `公司规模`
  * city `所在城市`
  * positionName `职位名称`
  * workYear `工作年限`
  * education `教育水平`
  * jobNature `工作性质`
  * .........
* 避免爬虫被ban的策略
  * 调整设置里面的`DOWNLOAD_DELAY`
  * 设置更换代理的中间件`ProxyMiddleWare`
  * 设置Header
     * ```'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'```
* 信息存储
  * 通过pipeline里的`LagouJobInfoDbPipeline`插入到数据库
  
# 需要用到的第三方库
* requests
* BeautifulSoup
* MySQLdb
  
