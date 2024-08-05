"""
演示Python中的各类运算符
"""

# 算术运算符
print("1 + 1 =", 1 + 1)
print("2 - 1 =", 2 - 1)
print("3 * 3 =", 3 * 3)
print("3 ** 3 =", 3 ** 3)
print("9 / 3 =", 9 / 3)
print("11 // 2 = ", 11 // 2)
print("9 % 2 = ", 9 % 2)

# 赋值运算
num = 1 + 2 * 3
print(num)

# 复合赋值运算符
num = 4
num += 1
print("num += 1:", num)

num -= 2
print("num -= 2:", num)
num *= 4
print("num *= 2:", num)


num = 10
num /= 2
print("num /= 2:",num)

num = 2
num **=3
print("num = num ** 2结果为：", num)
