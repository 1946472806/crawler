# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..items import BaikeItem

class MybaikeSpider(CrawlSpider):
    name = 'mybaike'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/Python/407313']

    rules = [
        Rule(
            LinkExtractor(
                allow=('/item/.*',),
            ),
            callback='parse_item',
            follow=True
        )
    ]

    def parse_item(self, response):
        title = response.xpath('//dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()').get()
        title = title if title else "主标题"
        sub_title = response.xpath('//dd[@class="lemmaWgt-lemmaTitle-title"]/h2/text()').get()
        sub_title = sub_title if sub_title else "副标题"
        content = response.xpath('//div[@class="lemma-summary"]/div/text()').get()
        content = content if content else "没有内容"

        # print()
        # print(title)
        # print(sub_title)
        # print(content)
        # print()

        print(title)


        item = BaikeItem()
        item['title'] = title
        item['sub_title'] = sub_title
        item['content'] = content
        yield item