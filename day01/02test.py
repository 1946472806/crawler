#模拟百度搜索
import urllib.request
import urllib.parse

def baiduAPI(params):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    }
    url = "https://www.baidu.com/s?"+params

    #创建请求对象
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    return response.read().decode('utf-8')

if __name__ == "__main__":
    kw = input("请输入你要查找的内容:")
    wd = {'ie':'utf-8',"wd":kw}
    params = urllib.parse.urlencode(wd)
    response = baiduAPI(params)
    print(response)