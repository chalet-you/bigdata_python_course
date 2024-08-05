# _*_ coding : utf-8 _*_
# @Time : 2024/7/27 16:18
# @Author : chalet.you
# @File : 04_datetime模块
# @Project : bigdata_python_course
import datetime

# 创建日期
d = datetime.date(2024, 7, 17)
print(d)

# 创建时间
t = datetime.time(14,25, 23)
print(t)

# 创建日期时间
dt = datetime.datetime(2024, 7, 17, 14,25, 23)
print(dt, type(dt))

print("="*50)

# 获取当前时间
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %X"), type(now))

# 只获取当前日期
today = datetime.date.today()
print(today)

print("="*50)
print(type(datetime.date.fromtimestamp(1234564525)))



