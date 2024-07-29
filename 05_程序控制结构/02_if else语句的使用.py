# _*_ coding : utf-8 _*_
# @Time : 2024/7/29 20:22
# @Author : chalet.you
# @File : 02_if else语句的使用.py
# @Project : bigdata_python_course
"""
演示 if else
"""
height = int(input("请输入您的身高："))

# 通过if进行判断
if height > 120:
    print("您的身高超过120cm，需要买票")
else:
    print("您的身高低于120cm，可以免费游玩")

print("祝你玩的愉快")