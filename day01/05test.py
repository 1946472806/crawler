#爬取网易云音乐(POST方式)
import json
import urllib
from urllib import request,parse

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

# post接口
url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_547976490?csrf_token="

# post提交参数
data = {
    "params": "3u5ErBfSCxBGdgjpJpTQyZVZgmPAv+aisCYZJ9pxk26DoOaS5on9xBjsE65yaS57u9XyxvCJIa78DXJathMsyiClN4LXqhonGNQrAtI2ajxsdW8FosN4kv8psGrRyCBsWrxSJQyfy5pfoeZwxLjB7jHtQkt9hglgZaAfj7ieRWq/XvX3DZtSgLcLrvH/SZOM",
    "encSecKey": "872312d7d8b04d2d5dab69d29c9bde5438337f0b3982887e3557468fe7b397de59e85ab349c07f32ef5902c40d57d023a454c3e1ed66205051264a723f20e61105752f16948e0369da48008acfd3617699f36192a75c3b26b0f9450b5663a69a7d003ffc4996e3551b74e22168b0c4edce08f9757dfbd83179148aed2a344826"}

#post参数转换成二进制
data = urllib.parse.urlencode(data) #url编码
data = data.encode() #转换成二进制
#创建请求对象
req = urllib.request.Request(url,headers=headers,data=data) #加上data后就表示post请求了
#发起请求
response = urllib.request.urlopen(req)

context = response.read().decode() #json

#json解析
content_dict = json.loads(context)
hotComments = content_dict.get('hotComments')
#热评
for c in hotComments:
    userid = c['user']['userId']
    nickname = c['user']['nickname']
    content = c['content']
    print(userid, nickname, content)
