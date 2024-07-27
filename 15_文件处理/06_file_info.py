# _*_ coding : utf-8 _*_
# @Time : 2024/4/24 21:13
# @Author : chalet.you
# @File : 06_file_info
# @Project : bigdata_python_course
import os
import time

f_stat = os.stat("F:/a/b/b.txt")

print("文件信息".center(30, "="))

print(f"文件大小{f_stat.st_size}")
print(f"最近的访问时间{time.ctime(f_stat.st_atime)}")
print(f"最近的修改时间{time.ctime(f_stat.st_mtime)}")
print(f"文件创建时间{time.ctime(f_stat.st_ctime)}")
