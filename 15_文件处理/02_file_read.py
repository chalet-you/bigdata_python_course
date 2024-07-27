# _*_ coding : utf-8 _*_
# @Time : 2024/4/22 22:50
# @Author : chalet.you
# @File : 02_file_read
# @Project : bigdata_python_course
f = open("F:a/hello.txt","r", encoding="UTF-8")
# 读取方式1：read(), 一次性返回整个文件的内容
context = f.read()

# 请思考如果执行 f.read(6) 会读取到什么内容, 分析一下
# content = f.read(6) #content: # 列表的定
# 关闭文件, 释放文件占用的系统资源

print(context)
f.close()
# line1 = f.readline()
# line2 = f.readline()
#
# print(f"第一行数据是{line1}")
# print(f"第二行数据是{line2}")
# f.close()

# while True:
#     line = f.readline()
#     if line =="":
#         break
#     print(line.strip())
#
# f.close()

# # 读取方式3: f.readlines()列表形式读取文件中的所有行

# lines = f.readlines()
# print(f"lines类型是->{type(lines)}") #list
# print(f"lines内容是->{lines}") #["第一行的数据\n", "第2行的数据\n"...]
# for line in lines:
#     print(line, end="")
# f.close()

# 读取方式4: for line in f形式读取文件

# for line in f:
#     print(line.strip())
#
# f.close()

# with open("F:a/hello.txt","r", encoding="UTF-8") as f:
#     for line in f:
#         print(line.strip())
