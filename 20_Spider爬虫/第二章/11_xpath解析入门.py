# _*_ coding : utf-8 _*_
# @Time : 2024/8/4 15:02
# @Author : chalet.you
# @File : 09_xpath解析入门
# @Project : bigdata_python_course

from lxml import etree
tree = etree.parse("./b.html")  # etree.parse(参数) 用于从文件或文件对象中解析XML或HTML文档。接受一个文件路径或文件对象作为参数。返回一个`ElementTree`对象，该对象表示整个文档树，可以用于进一步操作和查询
# result = tree.xpath('/html')

# result = tree.xpath("/html/body/ul/li/a/text()")
# result = tree.xpath("/html/body/ul/li[1]/a/text()")                 # xpath的顺序是从1开始数的， []表示索引
# result = tree.xpath("/html/body/ol/li/a[@href='feiji']/text()")       # [@xxx=xxx] 特定属性的值筛选
# print(result)

# ol_li_list = tree.xpath("/html/body/ol/li")
#
# for li in ol_li_list:
#     # 从每一个li中提取到文字信息
#     result = li.xpath("./a/text()")  # 在li中继续去寻找。相对查找
#     print(result)
#
#     result1 = li.xpath('./a/@href')  # 拿到属性值  @属性名称
#     print(result1)
#
#
# print(tree.xpath("/html/body/ul/li/a/@href"))

print(tree.xpath("/html/body/div[1]/text()"))
print(tree.xpath("/html/body/ul/li/a/text()"))
