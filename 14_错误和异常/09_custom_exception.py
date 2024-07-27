# _*_ coding : utf-8 _*_
# @Time : 2024/4/22 22:15
# @Author : chalet.you
# @File : 09_custom_exception
# @Project : bigdata_python_course

class AgeError(Exception):
    pass


while True:
    try:
        age = int(input("请输入年龄(18-120)："))
        if not (18 <= age <= 120):
            raise AgeError("年龄不在18-120之间")
        break
    except ValueError as e:
        print("请输入一个合法整数")
    except AgeError as e:
        print(e)

print(age)
