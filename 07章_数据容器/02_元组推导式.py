import random

# 元组推导式类似于列表推导式，只是将中括号换成了小括号
# 元组推导式和列表推导式不一样，其生成的是一个对象，一个生成器对象，并不直接是一个元组；
# 如果想要得到一个元组或者列表的话，那么就需要通过 tuple()或者list()来进行转化
yz = (random.randint(1,3) for i in range(10))

print(yz, type(yz))
# 打印出是：
# <generator object <genexpr> at 0x000001F8C9A1C4A0>    <class 'generator'>

randomnumber = (random.randint(10, 100) for i in range(10))
my_tuple = tuple(randomnumber)
print(my_tuple, type(my_tuple))
# 打印出是：
# (96, 44, 29, 27, 11, 60, 54, 86, 67, 39) <class 'tuple'>

# 综上，我们使用元组推导式时，得到的并不是一个元组，二十一个生成器，如果我们希望输出元组，我们还需要使用tuple()函数转换一下。
# 另外，我们还可以直接遍历生成器：


