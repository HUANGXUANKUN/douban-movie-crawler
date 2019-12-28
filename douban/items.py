# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name = scrapy.Field()
    serial_number = scrapy.Field()
    introduction = scrapy.Field()
    star = scrapy.Field()
    # 评论数
    evaluate = scrapy.Field()
    description = scrapy.Field()
