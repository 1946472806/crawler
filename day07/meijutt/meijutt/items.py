# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#item,有点类似Django的Model
class MeijuttItem(scrapy.Item):
    # define the fields for your item here like:
    #定义字段
    filename = scrapy.Field()
    score = scrapy.Field()
    director = scrapy.Field()
    editor = scrapy.Field()
