import urllib
from urllib import request

# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求
handler = urllib.request.HTTPHandler()  # http

# 构建一个HTTPHandler 处理器对象，支持处理HTTPS请求
# handlers = urllib.request.HTTPSHandler()  # 处理https的处理器

# 调用urllib2.build_opener()方法，创建支持处理HTTP请求的opener对象
opener = urllib.request.build_opener(handler)

# 构建 Request请求
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
req = urllib.request.Request("http://www.baidu.com",headers=headers)

# 调用自定义opener对象的open()方法，发送request请求
response = opener.open(req)

# 获取服务器响应内容
print(response.read().decode())