"""
演示第一种字符串格式化的方式：%s
"""
name = "张三"
age = 11
message = "姓名:%s，年龄:%s" % (name, age)
print(message)


# 演示第二种字符串格式化的方式：f{占位}

name = "中华人民共和国"
set_up_year = 1949
stock_price = 19.99
msg = f"我是{name}，我成立于{set_up_year}年，我今天的股票价格是{stock_price}"

print(msg)

# TODO：演示对表达式进行字符串格式化，将内容转换成整数，放入占位位置
num = 10.5
height = 45.123
res = "我有%d个苹果，它的重量是%d" % (num, height)
print(res)

print("2 ** 4 的结果是：%d" % (2 ** 4))
print(f"10 % 3 的结果是：{10 % 3}")
print("字符串在Python中的数据类型是：%s" % type("字符串"))


# TODO：字符串的占位，控制精度

num1 = 11
num2 = 23.146
print("数字11宽度限制5，结果：%5d" % num1)
print("数字11宽度限制1，结果：%1d" % num1)
print("数字23.1415宽度限制7，小数精度2，结果：%7.2f" % num2)
print("数字23.1415不限制宽度，小数精度2，结果：%.2f" % num2)


