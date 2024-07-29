# _*_ coding : utf-8 _*_
# @Time : 2024/7/27 22:47
# @Author : chalet.you
# @File : 02_requests入门02
# @Project : bigdata_python_course

import requests


url = "https://movie.douban.com/j/chart/top_list"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
# 遍历10页，每一页20条数据，共200条数据
for i in range(0, 10):
    start = i * 20

    param = {
        'type': 24,
        'interval_id': '100:90',
        'action': '',
        'start': start,
        'limit': 20
    }



    response = requests.get(url, params = param, headers = headers)
    lis = response.json()
    for dic in lis:
        for k, v in dic.items():
            print(f"{k}\t\t\t {v}")
    print("============="*10)
    # print(response.json())
    # 关闭请求
    response.close()