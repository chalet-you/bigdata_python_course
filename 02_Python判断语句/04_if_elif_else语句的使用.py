"""
演示if elif else 多条件判断语句的使用
"""

# 通过if判断，可以使用多条件判断的语法
# 第一个条件就是if
if int(input("请输入你的身高：")) < 120:
    print("身高小于120cm，可以免费游玩")
elif int(input("请输入你的VIP等级（1-5）：")) > 3:
    print("VIP级别大于3，可以免费游玩。")
elif int(input("请告诉我今天是几号：")) == 1:
    print("今天是1号，可以免费游玩")
else:
    print("不好意思，条件都不满足，需要买票10元才能游玩。")


