import requests

response = requests.get("http://www.baidu.com/")

cookiejar = response.cookies

#cookiejar转成字典
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

print(cookiedict)