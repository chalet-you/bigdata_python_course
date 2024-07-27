# _*_ coding : utf-8 _*_
# @Time : 2024/4/21 19:55
# @Author : chalet.you
# @File : 01_exception01
# @Project : bigdata_python_course

try:
    num1 = 10
    num2 = 0
    res = num1 / num2
except ZeroDivisionError as e:
    print(e)
    print(f"捕获到异常，异常是：{e}")

print("程序继续")


