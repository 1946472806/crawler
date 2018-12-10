import requests
from bs4 import BeautifulSoup

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}


def download(url):
    res = requests.get(url,headers=headers)
    html = res.content.decode('gbk')

    # soup = BeautifulSoup(html,'lxml')
    soup = BeautifulSoup(html, "html5lib")
    #
    mytable = soup.select('#datalist')
    tr_list = mytable[0].find_all("tr")
    for tr in tr_list:
        code = tr.td.a.text
        name = tr.select('td')[1].a.text
        value = tr.select('td')[4].span.text
        print(code,name,value)

if __name__ == "__main__":
    download("http://quote.stockstar.com/fund/stock_3_1_2.html")