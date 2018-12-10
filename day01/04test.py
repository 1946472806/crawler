#抓取豆瓣Ajax(GET方式)
import json
import urllib
from urllib import request

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
url="https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"

#创建请求对象
req = urllib.request.Request(url,headers=headers)
#访问
response = urllib.request.urlopen(req)
content = response.read().decode() #json字符串

#json解析
context_dict = json.loads(content)
movie_list = context_dict.get('subjects')
for movie in movie_list:
    print(movie.get('title'))