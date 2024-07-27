# _*_ coding : utf-8 _*_
# @Time : 2024/4/22 23:21
# @Author : chalet.you
# @File : 02_file_write
# @Project : bigdata_python_course

f = open("F:/a/abc.txt", "a", encoding="UTF-8")

for i in range(10):
    f.write("你好\n")

f.close()