import time

import gevent
from gevent import monkey

monkey.patch_all() #实现自动调度
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

#协程
def fn(url):
    print('协程：',url)

    #请求网络,会阻塞IO
    res = requests.get(url,headers=headers)
    html = res.text

    print('协程%s结束' % url,len(html))

if __name__ == '__main__':
    url_list = [
        'http://www.baidu.com',
        'http://www.qq.com',
        'http://www.taobao.com',
        'http://www.ifeng.com',
        'http://www.163.com',
    ]
    time.clock()
    #遍历5个url,创建5个协程
    g_list = []
    for url in url_list:
        # fn(url)
        #多协程
        g = gevent.spawn(fn,url)
        g_list.append(g)
    gevent.joinall(g_list)
    print(time.clock())