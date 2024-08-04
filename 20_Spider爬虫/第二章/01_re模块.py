# _*_ coding : utf-8 _*_
# @Time : 2024/7/28 12:56
# @Author : chalet.you
# @File : 01_re模块
# @Project : bigdata_python_course
import re

# findall：匹配字符串中松油符合正则的内容，并且返回一个列表，如果匹配的字符串是一个很大的文本的时候，findall返回的list列表效率不高。所以我们很少用
# lst = re.findall(r"\d+", "我的手机号是：10086，我老婆的手机号是15800376002")
# print(lst)

# finditer：匹配字符串中所有的内容[返回的是迭代器]，从迭代器中拿到内容需要.group()，finditer返回的迭代器效率很高，所以我们常用finditer。
# it = re.finditer(r"\d+", "我的手机号是：10086，我老婆的手机号是15800376002")
# for i in it:
#     print(type(i))
#     print(i.group())

# search，匹配到第一个结果就返回【注意：只要找到一个就返回】，返回的结果是match对象，拿数据需要.group()，所以只能匹配到一个目录结果
# s = re.search(r"\d+", "我的手机号是：10086，我老婆的手机号是15800376002")
# print(s.group())

# match是从字符串开头进行匹配的，就相当于正则表达式是(^\d+)，匹配字符串的开始位置，而不匹配每行开始。
# s = re.match(r"\d+", "我的手机号是：10086，我老婆的手机号是15800376002")
# print(s.group())

# compile() 可以将一个长长的正则进行预加载，方便后面的使用，compile()返回的是Pattern对象
obj = re.compile(r"\d+")

it = obj.finditer("我的手机号是：10086，我老婆的手机号是15800376002")
for i in it:
    print(i.group())

ret = obj.findall("呵呵哒，我今天在星巴克里学习了100分钟")
print(ret)