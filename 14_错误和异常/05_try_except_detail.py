# _*_ coding : utf-8 _*_
# @Time : 2024/4/21 19:59
# @Author : chalet.you
# @File : 05_try_except_detail
# @Project : bigdata_python_course
num1 = 10
num2 = 0

# try:
#     res = num1 / num2
#     print("hi....")
# except Exception as e:
#     print(f"出现异常，异常信息是{e}")
#
# print("继续执行......")


try:
    res = num1 / num2
    print("hello"[1000])
    f = open("F:/datas/a.txt", "r", encoding="UTF-8")
    print("hi....")
except (IndexError, ZeroDivisionError, FileNotFoundError) as e:
    print(f"捕获多种异常 信息->{e}，类型{type(e)}")

print("继续执行......")
