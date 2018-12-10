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
    urlre = "<a.*href=\"(https?://.*?)\".*>"
    urllist = re.findall(urlre,html)
    return urllist

def vastSpider(param):
    while len(stack) > 0:
        url = stack.pop()
        print('\t'*deptDict[url],"爬取了第%d级页面:%s" % (deptDict[url],url))

        if deptDict[url] < param:
            sonList = getUrl(url)
            for sonurl in sonList:
                if sonurl not in deptDict:
                    deptDict[sonurl] = deptDict[url] + 1
                    stack.append(sonurl)



if __name__ == "__main__":
    stack = []
    deptDict = {}
    startUrl = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=岛国邮箱"
    deptDict[startUrl] = 1
    stack.append(startUrl)
    vastSpider(3)