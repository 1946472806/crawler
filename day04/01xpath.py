import lxml
from lxml import etree

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <ul>
        <li class="item0">
            <a href="aaa">1111</a>
        </li>
        <li class="item1">
            <a href="bbb">2222</a>
        </li>
        <li class="item2">
            <a href="ccc">3333</a>
        </li>
        <li class="item2">
            <a href="cc2">4444</a>
        </li>
        <li class="item2">
            <a href="ccc">5555</a>
        </li>
    </ul>
</body>
</html>

"""

#创建etree对象
myetree = lxml.etree.HTML(html)

# /:子节点
# //：后代节点
print(myetree.xpath('/html')) #列表
print(myetree.xpath('/html/body'))
print(myetree.xpath('/body'))
print(myetree.xpath('//body'))
print(myetree.xpath('//li')) #所有li
print(myetree.xpath('//ul/li')) #所有li

ul = myetree.xpath('//ul')[0] #获取第一个ul
lis = ul.xpath('./li') #点.表示当前ul节点
print(lis)

#[index]:下表从1开始
print(myetree.xpath('//li[1]/a'))
print()

#属性
print(myetree.xpath('//li[1]/@class')) #获取属性item0
print(myetree.xpath('//li[2]/a/@href'))

#文本
print(myetree.xpath('//li[3]/a/text()')) #'3333'

#谓语
#last() 最后一个,没有first()
print(myetree.xpath('//li')[-1])
print(myetree.xpath('//li[last()]')) #倒数第一个
print(myetree.xpath('//li[last()-1]/a/@href')) #倒数第二个中的a的属性

#根据属性获取属性元素
print(myetree.xpath('//li[@class]')) #表示包含class属性的元素
print(myetree.xpath('//li[@class="item0"]')) #表示包含class="item0"属性的元素

# | 或
print(myetree.xpath('//li[@class="item0"] | //li[@class="item1"]'))

#position()位置
print(myetree.xpath('//li[position()<3]')) #前两个

#切片
print(myetree.xpath('//li')[1:4])

# *通配符
print(myetree.xpath('//ul/*')) #ul的所有子节点
print(myetree.xpath('//ul//*')) #ul的所有后代节点

