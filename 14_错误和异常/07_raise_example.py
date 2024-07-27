# _*_ coding : utf-8 _*_
# @Time : 2024/4/22 22:06
# @Author : chalet.you
# @File : 07_raise_example
# @Project : bigdata_python_course

try:
    raise ZeroDivisionError("我主动触发一个异常玩玩")
except ZeroDivisionError as e:
    print(f"捕获到异常 信息{e} 类型->{type(e)}")
