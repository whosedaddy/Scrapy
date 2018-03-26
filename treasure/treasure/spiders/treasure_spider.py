#-*- coding:utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
from treasure.items import TreasureItem
import re
from scrapy.http import Request
from scrapy.selector import Selector


class TreasureSpider(CrawlSpider):
	name = "treasure"
	allowed_domains = ["moko.cc"]
	start_urls = ["http://www.moko.cc/post/aaronsky/list/html"]
	img_urls = []
	rules = (Rule(LinkExtractor(allow=('/post/\d*\.html')), callback = 'parse_img', follow = True),)
	
	def parse_img(self, response):
		item = TreasureItem()
		sel = Selector(response)
		for divs in sel.xpath('//div[@class="pic dBd"]'):
			img_url = divs.xpath('.//img/@src2').extract()[0]
			img_url = img_url.split('?')[0]
			self.img_urls.append(img_url)
		item['image_urls'] = self.img_urls
		yield item
