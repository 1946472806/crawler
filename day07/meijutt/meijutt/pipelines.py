# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

#一般用于处理爬取到的数据，数据持久化
class MeijuttPipeline(object):

    #初始化属性
    def __init__(self):
        pass

    #打开爬虫的时候自动调用
    def open_spider(self,spider):
        # self.fp = open('news.txt','a',encoding='utf-8')
        # 连接数据库
        self.db = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="200417", database='crawler',charset='utf8')
        # 游标
        self.cursor = self.db.cursor()

    #处理每一个item
    #item:每一个传递过来的item对象
    #spider:爬虫对象(MeijuttSpider对象)
    #会被自动调用
    def process_item(self, item, spider):
        # print('process item',item)

        # strname = str((item['name'],item['newstime'])) + '\n'
        # with open('movie.txt','a',encoding='utf-8') as fp:
        #     strname = str((item['name'])) + '\n'
        #     fp.write(strname)
        #     fp.flush()

        # self.fp.write(strname)
        # self.fp.flush()

        sql = 'insert into filetable(filename, score,director,editor) VALUES(%r,%r,%r,%r) ' % (item['filename'], item['score'], item['director'], item['editor'])
        self.cursor.execute(sql)
        self.db.commit()

        return item

    #关闭爬虫时被调用
    def close_spider(self,spider):
        # self.fp.close()
        self.cursor.close()
        self.db.close()

