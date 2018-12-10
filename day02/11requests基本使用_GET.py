#GET
import requests

kw = {'wd':'DG'}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
response = requests.get("http://www.baidu.com/s?",params=kw,headers=headers)

# print(response.__dict__)
print(response.status_code)
# print(response.url)
# print(response.cookies)
# print(response.encoding)
print(response.text)
# print(response.content)