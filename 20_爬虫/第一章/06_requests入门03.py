# _*_ coding : utf-8 _*_
# @Time : 2024/7/27 22:47
# @Author : chalet.you
# @File : 02_requests入门02
# @Project : bigdata_python_course

import requests


url = "https://movie.douban.com/j/chart/top_list"
param = {
    'type': 24,
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

response = requests.get(url, params = param, headers = headers)

print(response.json())

response.close()  # 关掉 response