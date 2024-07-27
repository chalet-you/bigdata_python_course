# _*_ coding : utf-8 _*_
# @Time : 2024/4/22 23:35
# @Author : chalet.you
# @File : 04_file_del
# @Project : bigdata_python_course

import os
# print(os.path.exists("F:/a"))
# if os.path.isdir("F:/a"):
#     os.rmdir("F:/a/")
# else:
#     print("不存在")

# print(os.path.isdir("F:/a/b/b.txt"))
# print(os.path.isdir("F:/a/b/c"))

if os.path.exists("F:/a/b/c/c.txt"):
    os.remove("F:/a/b/c/c.txt")
else:
    print("不存在")