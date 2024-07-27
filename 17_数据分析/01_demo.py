import numpy as np

import random

# student = np.dtype([('name', 'S20'),('age', 'i4'), ('score', 'f4')])
#
# arr = np.array([('youxuan', 33, 145.6), ('lisi', 13, 95.6), ('wuhansan', 23, 3.14)],dtype = student)
# print(arr, type(arr))
#
#
# arr1 = np.zeros([2,3],dtype='i4')
#
# print(arr1)

# arr = np.linspace(0, 100, num=20, dtype='i4')
# arr.reshape((3,4),'F')
# print(arr)
# a = range(start = 1, stop = 100,step = 2)
# print(a, list(a))
#
#
# a = random.random()
# print(a)

# arr1 = np.random.rand(3,2)
# print(arr1)

# a = random.randint(1,3)
# print(a)

# for i in range(10):
#     a = random.randint(5,7)
#     print(a)

# a = np.arange(12).reshape(3,4)
# print(a)
# print('')
# b = np.insert(a, 3, [[100],[200]], axis = 1)
# print(b)

# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 11, 2, 3, 4])
# print(x)
# print(x.size)
#
# y = np.unique(x)
# print(y)
# print(y.size)

print(np.char.add(["hello"],["python"]))
print(np.char.add(["名字",'年龄'],["李四",'100']))

print(np.char.multiply("hello numpy ", 3))

print(np.char.center(["标题", "文本"],20, "#"))

print(np.char.capitalize(["wo shi shuI","jin tian yao zuo shen me", "bu zhi dao"]))

print(np.char.title(["wo shi shuI","jin tian yao zuo shen me", "bu zhi dao"]))

print(np.char.encode(['zhangsan', 'lisisi'],'utf-8'))
print(np.char.encode(['张三', '李四'],'utf-8'))

# a = np.random.randint(1, 100, 12).reshape(3,4)
# print(a)
#
# a_sort = np.sort(a, axis=1)
#
# print(a_sort)
#
# print(a[np.where(a > 50)])

x = np.array([[10, 10], [2, 3], [4, 5]])
print("x数组：")
print(x)

print("创建x的深层副本y")
y = x.copy()
print(y)
print("\n")
print(x is y)
print("\n")







