# -*- coding: utf-8 -*-
import scrapy
# from lxml import etree

#scrapy.Spider:scrapy爬虫父类
#爬虫类
from ..items import MeijuttItem
from scrapy.spiders import CrawlSpider,Rule #导入爬虫类，规则
from scrapy.linkextractors import LinkExtractor #导入链接类

# #日志
# import logging
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"  # 设置输出格式
# DATE_FORMAT = "%Y/%m/%d %H:%M:%S"  # 设置时间格式
# logging.basicConfig(filename='meijutt.log', filemode='a+', format=LOG_FORMAT, datefmt=DATE_FORMAT)


# class MymeijuttSpider(scrapy.Spider):
class MymeijuttSpider(CrawlSpider):

    # logging.info('已经爬取到数据...')
    #爬虫名，唯一
    name = 'mymeijutt'
    allowed_domains = ['55xia.com']
    start_urls = ['https://www.55xia.com/movie/?page=1']

    rules = (
        Rule(
            LinkExtractor(allow=('/movie/\?page=\d',), ),
            # 符合正则的链接,restrict_xpaths使用xpath表达式，和allow共同作用过滤链接
            callback='parse_item',  # 回调函数
            follow=True,  # 是否跟随
        ),
    )


    def parse_item(self, response):
        div_list = response.xpath('/html/body/div[1]/div[1]/div[2]/div[@class="col-xs-1-5 col-sm-4 col-xs-6 movie-item"]')
        for div in div_list:
            #电影名称
            filename = div.xpath('./div/div/h1/a/text()').extract_first()
            #评分
            score = div.xpath('./div/div/h1/em/text()').extract_first()
            #详情链接
            detail_url = 'https:' + div.xpath('./div/a[1]/@href').extract_first()

            #需要使用item
            item = MeijuttItem()
            item['filename'] = filename
            item['score'] = score

            # yield item

            # 根据页面中的链接继续爬取详情页面
            yield scrapy.Request(url=detail_url,callback=self.get_detail,meta={'item':item})

    def get_detail(self,response):
        item = response.meta['item']
        #导演
        director = response.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[2]/a/text()').extract_first()
        #编剧
        editors =  response.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[2]/a/text()')
        editorlist = []
        for e in editors:
            editorlist.append(e.extract())
        editor = '|'.join(editorlist)

        item['director'] = director
        item['editor'] = editor

        yield item