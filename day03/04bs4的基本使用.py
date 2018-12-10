from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

#创建soup对象
soup = BeautifulSoup(html, 'lxml')
#获取标签
# print(soup.title)
#获取标签的属性
# print(soup.a.attrs)

#获取标签文本
# print(soup.title.text)

#find_all()
# print(soup.find_all('a')) #查找所有a标签

#[]:或运算
# print(soup.find_all(['a','title'])) #查找所有a标签或title标签

#按照属性找
# print(soup.find_all('a',id='link1'))

#按照标签值找
# print(soup.find_all('a',text='Lacie'))

#select() 用法跟$()类似
# print(soup.select('.sister'))