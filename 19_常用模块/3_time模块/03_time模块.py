# _*_ coding : utf-8 _*_
# @Time : 2024/7/27 16:17
# @Author : chalet.you
# @File : 03_time模块
# @Project : bigdata_python_course
import time

print(time.localtime())
# 打印出：东八区的   time.struct_time(tm_year=2024, tm_mon=7, tm_mday=17, tm_hour=13, tm_min=37, tm_sec=40, tm_wday=2, tm_yday=199, tm_isdst=0)

print(time.gmtime())
# 打印出：0时区的   time.struct_time(tm_year=2024, tm_mon=7, tm_mday=17, tm_hour=13, tm_min=37, tm_sec=40, tm_wday=2, tm_yday=199, tm_isdst=0)

print(time.time())
# 打印出：当前时间的时间戳：1721194828.1924155

print(time.strftime("%Y-%m-%d %H:%M:%S"))
# 打印出：格式化后的时间字符串，默认打印大侠的时间

print("="*30)

# 获取一个文件的访问时间，以及修改时间，以及创建时间
# modify_time = os.path.getatime('E:\\chalet\\works\\一天76w条数据,一月2300w条数据')
# modify_time_local = time.localtime(modify_time)
# last_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', modify_time_local)
# print(last_modify_time)
