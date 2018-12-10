#递归方式
import re

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

hrefre = "<a.*href=\"(https?://.*?)\".*>"


def getPage(url):
    html = requests.get(url,headers=headers)
    return html.text


def getUrl(url):
    html = getPage(url)
    urllist = re.findall(hrefre,html)
    return urllist


def deepSpider(url,depth):
    print('\t'*deepDict[url],"爬取了第%d级页面:%s" % (deepDict[url],url))

    if deepDict[url] > depth:
        return
    sonlist = getUrl(url)
    for sonurl in sonlist:
        if sonurl not in deepDict:
            deepDict[sonurl] = deepDict[url] + 1
            deepSpider(sonurl,depth)

if __name__ == "__main__":
    deepDict = {}
    startUrl = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=岛国邮箱"
    deepDict[startUrl] = 1

    deepSpider(startUrl,4)
