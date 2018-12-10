import requests
from bs4 import BeautifulSoup


def download(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    response = requests.get(url, headers=headers)
    html = response.content.decode('gbk')

    soup = BeautifulSoup(html, "html5lib")
    # 获取岗位数量的多种查找方式
    # # 方式1： 使用find_all
    # jobnum = soup.find_all('div',class_='rt')
    # print(jobnum[0].text)
    # print(soup)
    # 方式2： 使用select
    jobnum = soup.select('.rt')[0].string
    print(jobnum.strip())  # 去掉首尾空格
download(url = "https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=")