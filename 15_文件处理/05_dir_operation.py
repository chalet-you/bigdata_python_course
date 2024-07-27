# _*_ coding : utf-8 _*_
# @Time : 2024/4/24 21:10
# @Author : chalet.you
# @File : 05_dir_operation
# @Project : bigdata_python_course

import os

if os.path.isdir("F:/a/b/c"):
    os.removedirs("F:/a/b/c")
    print("删除目录F:/a/b/c成功")
else:
    os.mkdir("F:/a/b/c")
    print("创建目录F:/a/b/c成功")