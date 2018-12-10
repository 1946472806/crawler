import json
import threading
import time

import requests
import lxml
from lxml import etree

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

#信号量：允许的线程最大并发量5
sem = threading.Semaphore(5)


def getcityjob(url):
    response = requests.get(url, headers=headers)
    html = response.content.decode()
    # 创建etree对象
    myetree = lxml.etree.HTML(html)
    #获取总页数
    pages = myetree.xpath('/html/body/div[4]/div[1]/div[8]/div[2]/div/@page-data')[0]
    params = json.loads(str(pages))
    pages = params['totalPage']

    #多线程
    t_list = []
    for page in range(1,pages+1):
        t = threading.Thread(target=get_data,args=(page,))
        t.start()
        t_list.append(t)
        # t.join() #不这么写,要不然就是一个一个线程排队去执行了
    #等待所有子线程全部执行完毕
    for t in t_list:
        t.join()
def get_data(page):
    with sem:
        print('开始爬取第%d页房源数据' % page)
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
            # print(houestitle)
            # 房子名称
            houesname = houes.xpath(".//div[1]/div[2]/div/a/text()")[0].strip()
            # print(houesname)
            # 描述1
            description = houes.xpath(".//div[1]/div[2]/div/text()")[0].strip()
            # print(description)
            # 描述2
            description2 = houes.xpath(".//div[1]/div[3]/div/text()")[0].strip()
            # print(description2)
            # 地址
            address = houes.xpath(".//div[1]/div[3]/div/a/text()")[0].strip()
            # print(address)
            # 描述3
            description3 = houes.xpath(".//div[1]/div[4]/text()")[0].strip()
            # print(description3)
        print('爬取第%d页房源数据结束' % page)

if __name__ == "__main__":
    start = time.time()
    getcityjob('https://gz.lianjia.com/ershoufang/')
    end = time.time()
    print(end - start)