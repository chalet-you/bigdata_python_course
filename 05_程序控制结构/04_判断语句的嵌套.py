# _*_ coding : utf-8 _*_
# @Time : 2024/7/29 20:23
# @Author : chalet.you
# @File : 04_判断语句的嵌套.py
# @Project : bigdata_python_course
"""
演示判断语句的嵌套使用
"""

if int(input("你的身高是多少：")) > 120:
    print("身高超出限制，不可以免费")
    print("但是，如果VIP级别超过大于3，可以免费")

    if int(input("你的vip级别是多少：")) > 3:
        print("你的级别达标，可以免费游玩")
    else:
        print("对不起，你需要买票10元")
else:
    print("欢迎小朋友，免费游玩")