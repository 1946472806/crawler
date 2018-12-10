# -*- coding: utf-8 -*-
import scrapy


class ZhihuspiderSpider(scrapy.Spider):
    name = 'zhihuSpider'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/signup?next=%2F']

    def __init__(self):
        pass

    def parse(self, response):
        print('*' * 50)
        print(response.text)
        print('*' * 50)

