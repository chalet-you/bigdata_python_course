# _*_ coding : utf-8 _*_
# @Time : 2024/4/22 21:21
# @Author : chalet.you
# @File : 02_exception_exercise
# @Project : bigdata_python_course

age = None

while True:
    try:
        age = int(input("请输入一个整数："))
        break
    except Exception as e:
        print("你输入的不是整数，请继续输入一个整数")

print(age)
