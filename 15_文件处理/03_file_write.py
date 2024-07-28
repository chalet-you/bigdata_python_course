# _*_ coding : utf-8 _*_
# @Time : 2024/4/22 23:21
# @Author : chalet.you
# @File : 02_file_write
# @Project : bigdata_python_course

f = open("F:/a/abc.txt", "w", encoding="UTF-8")

for i in range(10):
    f.write("hello python\n")   # 一定要带 \n ，不带的话会写到一行里。
f.close()