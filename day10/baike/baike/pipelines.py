# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class BaikePipeline(object):

    def open_spider(self, spider):
        self.db = pymysql.connect(
            host="127.0.0.1", port=3306,
            user="root", password='root',
            database='spiderdb', charset='utf8'
        )
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()

    def process_item(self, item, spider):

        title = item['title']
        sub_title = item['sub_title']
        content = item['content']

        sql = "insert into baike(title, sub_title, content) values(%r, %r, %r)" % \
              (title, sub_title, content)
        self.cursor.execute(sql)
        self.db.commit()

        return item
