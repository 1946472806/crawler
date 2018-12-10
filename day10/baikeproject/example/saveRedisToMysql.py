#把redis中的数据迁移到mysql

#连接redis
import json
import time

import pymysql
import redis

redis_con = redis.Redis(host='localhost', port=6379, db=0)
# print(redis_con)
#连接mysql
mysqlcli = pymysql.connect(host='127.0.0.1', user='root', password='200417', db='xpc_1809', port=3306, charset='utf8')
mysql_cursor = mysqlcli.cursor()
# print(mysqlcli)
while True:
    key,val = redis_con.blpop(['mycrawler_redis:items'])
    item = json.loads(val)

    #存入数据库
    sql = 'insert into baikeredis(title, sub_title, content) values (%r,%r,%r)' % (
        item['title'],item['sub_title'],item['content']
    )

    mysql_cursor.execute(sql)
    mysqlcli.commit()

    time.sleep(1)
mysql_cursor.close()
mysqlcli.close()
