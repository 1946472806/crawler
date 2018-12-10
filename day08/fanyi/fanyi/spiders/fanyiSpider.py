# -*- coding: utf-8 -*-
import json

import scrapy


class FanyispiderSpider(scrapy.Spider):
    name = 'fanyiSpider'
    allowed_domains = ['fanyi.baidu.com']
    # start_urls = ['http://fanyi.baidu.com/']

    #重写了start_requests方法
    def start_requests(self):
        print('开始请求')
        url = "http://fanyi.baidu.com/sug"
        params = {'kw':'wolf'}

        # POST请求
        yield scrapy.FormRequest(
            url=url,
            formdata=params,
            callback=self.parse
        )

    def parse(self, response):
        print('获得数据:',json.loads(response.text))
