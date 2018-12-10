#爬取前程无忧的岗位数量
import re
import urllib
from urllib import request
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
url = "https://search.51job.com/list/040000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

#创建请求对象
req = urllib.request.Request(url,headers=headers)

#访问服务器
response = urllib.request.urlopen(req)

print(response)
html = response.read().decode('gbk') #注意，这个解码是utf-8还是gbk,应该到原网页查看元素的头部的charset值

pattern = re.compile('<div class="rt">(.*?)</div>',re.S)
result = pattern.findall(html)[0]
print(result.strip())
