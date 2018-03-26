# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from jd.items import JdItem
from openpyxl import Workbook

class JdPipeline(object):
	
	def __init__(self):
		self.jd1 = Workbook()
		self.jd = self.jd1.active
		name = ['ID','name','shop_name','link','comment_num','price']
		self.jd.append(name)
		
	def process_item(self, item, spider):
		self.jd.append([item['ID'][0].encode('utf-8'),item['name'][0].encode('utf-8').strip(),item['shop_name'][0].encode('utf-8'),"http:"+item['link'][0].encode('utf-8'),str(item['comment_num']).encode('utf-8'),str(item['price']).encode('utf-8')])
		self.jd1.save('text.xlsx')
		return item
		
	def close_spider(self, spider):
		pass