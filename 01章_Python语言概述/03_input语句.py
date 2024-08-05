"""
演示Python的input语句
获取键盘的输入信息
"""

name = input("请告诉我你的名字:")
result = "我知道了，你是%s" % name
print(result)


# 输入数字类型
num = input("请告诉我你的密码：")
num = int(num)
print("你的银行卡密码的类型是：", type(num))
