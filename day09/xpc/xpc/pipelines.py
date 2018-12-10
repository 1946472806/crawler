# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class XpcPipeline(object):
    # 打开爬虫的时候自动调用
    def open_spider(self, spider):
        # self.fp = open('news.txt','a',encoding='utf-8')
        # 连接数据库
        self.db = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="200417", database='xpc_1809',
                                  charset='utf8mb4')
        # 游标
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        # # print(item) #item是一个字典型数据
        keys,values = zip(*item.items())
        sql = 'insert into `{}`({}) values({}) on duplicate key update {}'.format(
            item.table_name, #表名
            ','.join(['`%s`' % key for key in keys]), #字段
            ','.join(['%s'] * len(values)),
            ','.join(['`{}`=%s'.format(key) for key in keys])
        )
        self.cursor.execute(sql,values*2)
        self.db.commit()


        return item

    #关闭爬虫时被调用
    def close_spider(self,spider):
        # self.fp.close()
        self.cursor.close()
        self.db.close()
