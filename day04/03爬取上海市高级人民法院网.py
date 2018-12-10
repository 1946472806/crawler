import requests
from lxml import etree

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

url = "http://www.hshfy.sh.cn/shfy/gweb2017/ktgg_search_content.jsp"

data = {
"yzm": "ivKg",
"ft":"",
"ktrqks": "2018-11-29",
"ktrqjs": "2018-12-29",
"spc":"",
"yg":"",
"bg":"",
"ah":"",
"pagesnum": "1"
}

html = requests.post(url,headers=headers,data=data)

html = etree.HTML(html.text)
tr_list = html.xpath('//table[@id="report"]//tr')[1:]

for tr in tr_list:
    #法院
    fy = tr.xpath('./td[1]/font/text()')[0]
    print(fy)
