import json

import requests

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}


data = {
"i": "中国",
"from": "AUTO",
"to": "AUTO",
"smartresult": "dict",
"client": "fanyideskweb",
"salt": "1543306469484",
"sign": "e77b97de8542b783dd1d549bec566746",
"doctype": "json",
"version": "2.1",
"keyfrom": "fanyi.web",
"action": "FY_BY_REALTIME",
"typoResult": "false",
}
response = requests.post(url,data=data,headers=headers)
res = response.content
tgt = json.loads(res)
print(tgt['translateResult'][0][0]['tgt'])