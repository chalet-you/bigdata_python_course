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

# 定义 URL 模板和请求头
url_template = "https://movie.douban.com/top250?start={}&filter="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

# 解析数据的正则表达式对象
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<movie>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
                 r'class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<num>.*?)人评价</span>', flags=re.S)

# 打开CSV文件
with open("./Movie_plus.csv", mode="w", encoding="utf-8", newline="") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(["movie", "year", "score", "num"])  # 写入表头

    # 遍历10页，每一页25条数据，共250条数据
    for i in range(0, 10):
        start = i * 25
        url = url_template.format(start)
        response = requests.get(url, headers=headers)
        page_context = response.text

        # 开始匹配需要提取的子串
        result = obj.finditer(page_context)
        for i in result:
            row_dict = i.groupdict()
            row_dict['year'] = row_dict['year'].strip()
            csvwriter.writerow(row_dict.values())

        # 关闭请求
        response.close()


