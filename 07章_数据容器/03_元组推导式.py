import random

# 元组推导式产生的生成器对象，我们还是可以遍历的，
# 但如果生成器对象转成列表，那该生成器就被消耗掉了，无法在迭代了


randomnumber = (random.randint(10, 100) for i in range(10))

# for element in randomnumber:
#     print(element)

# 元组生成器产生的生成器对象，还可以强转成列表和元组
print(list(random.randint(10, 20) for i in range(10)))
print(tuple(random.randint(10, 20) for i in range(10)))
