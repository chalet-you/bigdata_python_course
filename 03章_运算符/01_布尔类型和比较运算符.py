# _*_ coding : utf-8 _*_
# @Time : 2024/7/29 20:02
# @Author : chalet.you
# @File : 01_demo
# @Project : bigdata_python_course
"""
演示布尔类型的定义
以及比较运算符的应用
"""
# 定义变量存储布尔类型的数据
bool_1 = True
bool_2= False
res1 = f"bool_1变量的内容是：{bool_1}，类型是：{type(bool_1)}"
res2 = "bool_2变量的内容是：%s，类型是：%s" % (bool_2, type(bool_2))
print(res1)
print(res2)

# 比较运算符的使用
# ==， ！=， >，>=，<，<=
# 演示进行内容的相等比较
num1 = 10
num2 = 10
print(f"10 == 10的结果是{num1==num2}")

num3 = 10
num4 = 15
res3 = f"10 > 15的结果是{num3 > num4}"
print(res3)

res4 = f"10 != 15的结果是{num3 != num4}"
print(res4)