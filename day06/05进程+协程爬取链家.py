import json
import threading
import time

import gevent
from gevent import monkey
monkey.patch_all() #实现自动调度
import requests
import lxml
from lxml import etree
import multiprocessing

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}


def getcityhoues():
    #区域
    qu_list = [
        "luohuqu",
        "futianqu",
        "nanshanqu",
        "yantianqu",
        "baoanqu",
        "longgangqu",
        "longhuaqu",
        "guangmingxinqu",
        "pingshanqu",
        "dapengxinqu",
    ]

    p_list = []
    for i in qu_list:
        #区循环改成多进程
        p = multiprocessing.Process(target=get_request,args=(i,))
        p.start()
        p_list.append(p)
    for p in p_list:
        p.join()


def get_request(qu):
    url = 'https://sz.lianjia.com/ershoufang/' + qu
    response = requests.get(url, headers=headers)
    html = response.content.decode()
    # 创建etree对象
    myetree = lxml.etree.HTML(html)
    # 获取总页数
    pages = myetree.xpath('/html/body/div[4]/div[1]/div[8]/div[2]/div/@page-data')[0]
    params = json.loads(str(pages))
    pages = params['totalPage']
    get_pages(pages,qu)

def get_pages(pages,qu):
    # 多协程
    g_list = []
    for page in range(1, pages + 1):
        g = gevent.spawn(get_data, qu,page)
        g_list.append(g)
    gevent.joinall(g_list)

def get_data(qu,page):
    print('%s 开始爬取第%d页房源数据' % (qu,page))
    newurl = 'https://gz.lianjia.com/ershoufang/' + 'pg' + str(page)
    # 获取这一页的全部房源
    response = requests.get(newurl, headers=headers)
    html = response.content.decode()
    # 创建etree对象
    myetree = lxml.etree.HTML(html)

    houess = myetree.xpath('/html/body/div[4]/div[1]/ul/li[@class="clear LOGCLICKDATA"]')
    for houes in houess:
        # 房子标题
        houestitle = houes.xpath('.//div[1]/div[1]/a/text()')[0].strip()
        # 房子总价
        allmoney = houes.xpath('.//div[1]/div[6]/div[1]/span/text()')[0].strip() + '万'
        #单价
        avgmoney = houes.xpath('.//div[1]/div[6]/div[2]/span/text()')[0].strip()
        text = qu + ' '+ '第'+ str(page) + '页 '+ houestitle+ ' ' +allmoney+ ' ' +avgmoney
        print(text)
        # with lock:
        #     with open("链家深圳二手房.txt",'a',encoding="utf-8") as fp:
        #         fp.write(text+'\n')

    print('%s 爬取第%d页房源数据结束' % (qu,page))

if __name__ == "__main__":
    start = time.time()
    getcityhoues()
    end = time.time()
    print(end - start)
