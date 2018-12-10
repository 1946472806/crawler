import random
from urllib import request

# ip代理池
iplist = [
    "http://183.159.84.198:18118",
    "http://183.159.92.206:18118",
    "http://119.179.209.43:61234",
    "http://183.159.82.181:18118"
]

# ua池（user-agent池 ）
UserAngentList=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36"
]

url = 'https://blog.csdn.net/linangfs/article/details/78331419?locationNum=9&fps=1'

headers = {"User-Agent":random.choice(UserAngentList)}
# proxy = {"http":random.choice(iplist)}
#使用西刺代理
proxy = {"http": "http://user1:123456@10.20.154.23:808"}
proxy_handler = request.ProxyHandler(proxy)

opener = request.build_opener(proxy_handler)

#发起请求
req = request.Request(url,headers=headers)

response = opener.open(req)

print(response.read().decode())