# _*_ coding : utf-8 _*_
# @Time : 2024/7/28 15:28
# @Author : chalet.you
# @File : 03_手刃豆瓣TOP250
# @Project : bigdata_python_course

# 拿到页面源代码。   requests
# 通过re来提取想要的有效信息    re
import re
import requests
import csv

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers = headers)
page_context = resp.text

# 解析数据

obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<movie>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
                 r'class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<num>.*?)人评价</span>', flags=re.S)
# 开始匹配
result = obj.finditer(page_context)

with open("./Movie.csv", mode="w", encoding="utf-8", newline='') as f:
    csvwriter = csv.writer(f)

    for it in result:
        # print(it.group("movie"))
        # print(it.group("year").strip())
        # print(it.group("score"))
        # print(it.group("num"))
        dict = it.groupdict()
        dict['year'] = dict['year'].strip()
        csvwriter.writerow(dict.values())

# 关闭请求
resp.close()