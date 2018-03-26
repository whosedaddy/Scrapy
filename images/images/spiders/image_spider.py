#-*- coding:utf-8 -*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
from images.items import ImagesItem
import re
from scrapy.http import Request
from scrapy.selector import Selector


class ImagesSpider(CrawlSpider):

	name = 'images'
	allowed_domain = ['meizitu.com']
	start_urls = ['http://www.meizitu.com/']
	
	def parse(self, response):
		sel = Selector(response)
		for link in sel.xpath("//div[@class='tags']//a/@href").extract():
			request = Request(link, callback = self.parse_class)
			yield request
	
	def parse_class(self, response):
		sel = Selector(response)
		for link in sel.xpath("//div[@class='pic']//a/@href").extract():
			request = Request(link, callback = self.parse_detail)
			yield request
	#这里可以进行翻页	
		# pages = sel.xpath("//div[@class='navigation']/div[@id='wp_page_numbers']/ul/li/a/@href").extract()
		# print('pages:%s'%pages)
		# if len(pages) > 2:
			# page_link = page[-2]
			# page_link = page_link.replace('/a/', '')
			# request = Request('http://www.meizitu.com/a/%s' % page_link, callback=self.parse)
			# yield request
		
	def parse_detail(self, response):
		item = ImagesItem()
		item['image_urls'] = response.xpath("//div[@id='picture']/p/img/@src").extract()
		item['url'] = response.url
		yield item
			

# class ImagesSpider(CrawlSpider):
	# name = 'meizitu'
	# allowed_domain = ['t66y.com']
	# start_urls = ['http://t66y.com/thread0806.php?fid=16']
	
	# def parse(self, response):
		# detailpagelinks = response.xpath('//h3/a/@href')
		# for detailpagelink in detailpagelinks:
			# detailpagelink = detailpagelink.extract()
			# link = response.urljoin(detailpagelink)
			# yield scrapy.Request(link, callback = self.parse_detail)
			
		# next_page = response.xpath('//a[contains(text(),"下一頁")]/@href').extract_first()
		# if next_page:
			# next_pagelink = response.urljoin(next_page)
			# yield scrapy.Request(next_pagelink, callback = self.parse)
		
	# def parse_detail(self, response):
		# item = ImagesItem()
		# item['image_urls'] = response.xpath('//input/@src').extract()
		# yield item