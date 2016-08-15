# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouJobCategoryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    job_url = scrapy.Field()
    job_category_level1 = scrapy.Field()
    job_category_level2 = scrapy.Field()



class LagouJobInfo(scrapy.Item):
	"""docstring for LagouJobInfo"""
	keyword = scrapy.Field()
	companyLogo = scrapy.Field()
	salary = scrapy.Field()
	city = scrapy.Field()
	financeStage = scrapy.Field()
	industryField = scrapy.Field()
	approve = scrapy.Field()
	positionAdvantage = scrapy.Field()
	positionId = scrapy.Field()
	companyLabelList = scrapy.Field()
	score = scrapy.Field()
	companySize = scrapy.Field()
	adWord = scrapy.Field()
	createTime = scrapy.Field()
	companyId = scrapy.Field()
	positionName = scrapy.Field()
	workYear = scrapy.Field()
	education = scrapy.Field()
	jobNature = scrapy.Field()
	companyShortName = scrapy.Field()
	district = scrapy.Field()
	businessZones = scrapy.Field()
	imState = scrapy.Field()
	lastLogin = scrapy.Field()
	publisherId = scrapy.Field()
	# explain = scrapy.Field()
	plus = scrapy.Field()
	pcShow = scrapy.Field()
	appShow = scrapy.Field()
	deliver = scrapy.Field()
	gradeDescription = scrapy.Field()
	companyFullName = scrapy.Field()
	formatCreateTime = scrapy.Field()