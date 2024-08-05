"""
设置一个范围 1 - 100的随机数变量，通过while循环，配合 input语句，判断输入的数字是否等于随机数
"""

import random

num = random.randint(1, 100)
flag = True
count = 0

while flag:
    guess_num = int(input("请输入你猜的数字："))
    if guess_num < num:
        print(f"您猜的数字：{guess_num}，小了")
    elif guess_num > num:
        print(f"您猜的数字：{guess_num}，大了")
    elif guess_num == num:
        print("恭喜你猜对了")
        flag = False
    count += 1
print(f"你一共猜了{count}次")
