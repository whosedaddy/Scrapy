# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	ID = scrapy.Field()
	name = scrapy.Field()
	shop_name = scrapy.Field()
	link = scrapy.Field()
	comment_num = scrapy.Field()
	price = scrapy.Field()
	commentVersion = scrapy.Field()
	commentVersion = scrapy.Field()
	score1count = scrapy.Field()
	score2count = scrapy.Field()
	score3count = scrapy.Field()
	score4count = scrapy.Field()
	score5count = scrapy.Field()