"""
演示字符串的三种定义方式
一：单引号定义
二：双引号定义
三：三引号定义
"""


# 单引号定义法，使用打印好进行包围
name = '你好'
print(type(name))

# 双引号定义法
name = "中华人民共和国"
print(type(name))

# 三引号定义法，写法和多行注释一样
name = """我是中国人"""
print(type(name), name)

# 在字符串内，包含双引号
name1 = '"name":"俺是张三"'
name2 = "\"name\":\"张三\""
print(name1,name2)

# 在字符串内，包含单引号
name3 = "'type'"
name4 = '\'type\''
print(name3, name4)

name = '\\'
print(name)


# 使用转义字符  \ 解除引号的效果
name5 = "\"程序员\""
name6 = '\'大数据工程师\''
print(name5, name6)

