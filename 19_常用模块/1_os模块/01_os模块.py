# _*_ coding : utf-8 _*_
# @Time : 2024/7/27 16:16
# @Author : chalet.you
# @File : 01_OS模块
# @Project : bigdata_python_course

# os模块主要用于与操作系统进行交互，包括文件和目录操作、环境变量操作等。常用功能包括：
# 1. 文件和目录操作
# 2. 路径操作
# 3. 环境变量操作
# 4. 进程操作
import os
import sys

# os.mkdir("test") # 创建单级目录
# os.makedirs("test1/test2/test3", exist_ok=True) # 创建单级目录
# 
# os.rmdir("D:/Users/Chalet.you/PycharmProjects/python_learn/13_os模块/test") # 指定删除某个目录
if os.path.exists("D:/Users/Chalet.you/PycharmProjects/python_learn/13_os模块/test1/test2/test3/ReadMe.md"):
    os.remove("D:/Users/Chalet.you/PycharmProjects/python_learn/13_os模块/test1/test2/test3/ReadMe.md")

if os.path.exists("D:/Users/Chalet.you/PycharmProjects/python_learn/13_os模块/test1/test2/test3/"):
    os.rename("D:/Users/Chalet.you/PycharmProjects/python_learn/13_os模块/test1/test2/test3/",
              "D:/Users/Chalet.you/PycharmProjects/python_learn/13_os模块/test1/test2/test3_bak/")

# print(os.listdir("D:/Users/Chalet.you/PycharmProjects/python_learn/"))

# os.system("dir")

# if os.path.isfile("D:/Users/Chalet.you/PycharmProjects/python_learn/13_os模块/01_os_base.py"):
#     print(os.path.getsize("D:/Users/Chalet.you/PycharmProjects/python_learn/13_os模块/01_os_base.py"))

# print(os.path.isdir("D:/Users/Chalet.you")) # 判断某个路径是否为目录
# print(os.environ) # 获取系统的环境变量
print("=" * 20)
# print(sys.path)

# directory, filename= os.path.split("D:/Users/Chalet.you/PycharmProjects/python_learn/13_os模块/01_os_base.py")
# print(directory)
# print(filename)

# print(os.path.dirname("D:/Users/Chalet.you/PycharmProjects/python_learn/13_os模块/01_os_base.py"))
# print(os.getenv("HOME"))
# print(os.linesep)
# print(os.stat("D:/Users/Chalet.you/PycharmProjects/python_learn/13_os模块/01_os_base.py"))
