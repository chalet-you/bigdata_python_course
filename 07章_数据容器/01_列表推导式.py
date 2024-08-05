"""
列表推导式的基本语法结构为：
[expression for item in iterable if condition]
其中，expression表示参与列表生成的表达式，可包含变量、函数调用等操作；item表示生成列表中的元素；
iterable表示可迭代的对象，
例如列表、元组、集合等； if condition表示对条件的筛选，可以省略。
expression表示要对每个item进行操作的表达式，item是可迭代对象中的每个元素，if condition是可选的筛选条件。
在执行完毕后，将得到一个新的列表new_list。
"""
# 生成1-9的整数列表
myList = [x for x in range(1, 10)]
print(myList)  # 打印：[1, 2, 3, 4, 5, 6, 7, 8, 9]

# 生成1-9之间的整数的平方列表
square_list = [x ** 2 for x in range(1, 10)]
print(square_list)  # 打印：[1, 4, 9, 16, 25, 36, 49, 64, 81]

# 从一个字符串列表中筛选出长度超过5的字符串，然后组成一个新的列表
str_list = ['hello', 'world', 'python', 'list', 'comprehension', 'study']
new_list = [ele for ele in str_list if len(ele) > 5]
print(new_list)  # 打印：['python', 'comprehension']

# 多重循环
my_list = [n * m for n in range(1, 4) for m in range(1, 4)]
# 此处通过两层循环实现了乘法操作，即n和m分别取 1、2、3时，他们的乘积构成了列表中的元素
print(my_list)  # 打印：[1, 2, 3, 2, 4, 6, 3, 6, 9]

# 嵌套列表推导式
my_lists = [
    [[1, 2, 3], [4, 5, 6]]
]

flat = [element for sub1 in my_lists for sub2 in sub1 for element in sub2]
print(flat) # 打印：[1, 2, 3, 4, 5, 6]


