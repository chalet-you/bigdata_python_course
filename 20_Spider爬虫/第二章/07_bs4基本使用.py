# _*_ coding : utf-8 _*_
# @Time : 2024/8/4 10:22
# @Author : chalet.you
# @File : 06_bs4基本使用
# @Project : bigdata_python_course
# 安装
# pip install bs4 -i 清华源

# 1。拿到页面源代码
# 2。使用bs4进行解析。拿到数据

import requests
from bs4 import BeautifulSoup
import csv

# url = "http://www.xinfadi.com.cm/marketanalysis/0/list/l.shtml"
url = "https://movie.douban.com/"
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}
resp = requests.get(url, headers = headers)
# print(resp.text)
f = open("./菜价.csv", mode="w", newline='')
csvwriter  = csv.writer(f)


# 解析数据
# 1.把页面源代码交给BeautifulSoup进行处理，生成bs对象 <class 'bs4.BeautifulSoup'>
page = BeautifulSoup(resp.text, "html.parser")    # 指定html解析器

# 2。从bs对象中查找数据
# find(标签, 属性=值)       只要找到一个就返回
# find_all(标签, 属性=值)   找到所有的，并返回一个list列表
# table = page.find("table", class_="hq_table")    # class是python的关键字，所以用 class_区别 class 关键字
table = page.find("table", attrs={"class": "hq_table"})    # 和上一行是一个意思。此时可以避免class

# 拿到所有数据行
trs = table.find_all("tr")[1:]   # 过滤掉表头，表头不需要，只要数据，tr表示行
for tr in trs: # 每一行
    td = tr.find_all("td")  # 拿到每行中所有td，td表示单元格
    name = td[0].text       # .text 表示拿到被标签标记的内容
    low = td[1].text       # .text 表示拿到被标签标记的内容
    avg = td[2].text       # .text 表示拿到被标签标记的内容
    high = td[3].text       # .text 表示拿到被标签标记的内容
    guige = td[4].text       # .text 表示拿到被标签标记的内容
    kind = td[5].text       # .text 表示拿到被标签标记的内容
    date = td[6].text       # .text 表示拿到被标签标记的内容
    lis = [name, low, avg, high, guige, kind, date]
    csvwriter.writerow(lis)

f.close()
print("over!!!!")