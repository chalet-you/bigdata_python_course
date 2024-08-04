# _*_ coding : utf-8 _*_
# @Time : 2024/7/28 12:56
# @Author : chalet.you
# @File : 01_re模块
# @Project : bigdata_python_course
import re

# 正则中的内容如何单独提取出来呢？
# 单独获取到正则中的具体内容可以给分组其名字  eg:(?P<name>pattern)，命名捕获，将匹配的子字符串捕获到一个组名称或编号名称中。
# (?P<分组名字>正则)   可以单独从正则匹配的内容中进一步提取内容

s = """
<div class='jay'><span id='1'>张三</span></div>
<div class='jor'><span id='2'>李四</span></div>
<div class='jlin'><span id='3'>王五</span></div>
<div class='lar'><span id='4'>赵六</span></div>
<div class='tory'><span id='5'>田七</span></div>
"""

obj = re.compile(r"<div class='(.*?)'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", flags=re.S)   # 这里的flags = re.S 表达的是 让【.】匹配包括换行符在内的所有字符


it = obj.finditer(s)
for i in it:
    print(i.group("id"))     # 等同于 i.group(2)
    print(i.group("name"))   # 等同于 i.group(3)

