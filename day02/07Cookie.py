from urllib import request
from http import cookiejar

#创建一个对象存储cookie
cookies = cookiejar.LWPCookieJar()

#cookie处理器,提取cookie
cookie_handler = request.HTTPCookieProcessor(cookies)

#创建打开器,处理cookie
opener = request.build_opener(cookie_handler)

#发起请求
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
req = request.Request("http://www.baidu.com",headers=headers)

response = opener.open(req)

#得到cookies
for cookie in cookies:
    print(cookie.name,":",cookie.value)