# _*_ coding : utf-8 _*_
# @Time : 2024/4/21 15:17
# @Author : chalet.you
# @File : 06_exception_exercise_01
# @Project : bigdata_python_course


while True:
    # age = 0
    try:
        age = int(input("请输入一个整数:"))
        break
    except Exception as e:
        print("你输入不是一个整数")
print(age)
