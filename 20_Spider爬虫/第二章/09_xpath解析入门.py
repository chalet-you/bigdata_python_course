# _*_ coding : utf-8 _*_
# @Time : 2024/8/4 15:02
# @Author : chalet.you
# @File : 09_xpath解析入门
# @Project : bigdata_python_course

# xpath 是在XML文档中搜索内容的一门语言
# html  是xml的一个子集

"""
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <author>
        <nick>周大强</nick>
        <nick>周芷诺</nick>
    </author>
</book>
"""

# 安装lxml模块
# pip install lxml -i 清华源
# xpath解析

from lxml import etree
xml="""
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷诺</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>热热热热1</nick>
        </div>
        <span>
            <nick>热热热热2</nick>
        </span>
    </author>
    
    <partner>
        <nick id="ppc">胖胖胖</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""

tree = etree.XML(xml)
# result = tree.xpath("/book/name")    # /表示层级关系。第一个/是根节点
# result = tree.xpath("/book/name")
# result = tree.xpath("/book/name/text()")         # text() 拿文本
# result = tree.xpath("/book/author//nick/text()")   # // 后代
# result = tree.xpath("/book/author/*/nick/text()")   # * 任意的节点。通配符
result = tree.xpath("/book//nick/text()")
print(result)