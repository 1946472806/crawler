#爬取百度
import urllib
from urllib import request

url = "http://www.baidu.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

req = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(req)

# print(response.info()) #响应信息
# print(response.read())#二进制
print(response.read().decode('utf-8')) #字符串