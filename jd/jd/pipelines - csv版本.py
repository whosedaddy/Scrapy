# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from jd.items import JdItem
import csv

class JdPipeline(object):
	
	def __init__(self):
		self.csvwriter = csv.writer(open('test.csv','wb'))
		name = ['ID','name','shop_name','link','comment_num','price']
		self.csvwriter.writerow(name)
		
	def process_item(self, item, spider):
		self.jd.writerow([item['ID'][0].encode('gbk'),item['name'][0].encode('gbk').strip(),item['shop_name'][0].encode('gbk'),"http:"+item['link'][0].encode('gbk'),str(item['comment_num']).encode('gbk'),str(item['price']).encode('gbks')])
		return item
		
	def close_spider(self, spider):
		return item