# _*_ coding : utf-8 _*_
# @Time : 2024/8/11 13:45
# @Author : chalet.you
# @File : 07_线程池爬新发地
# @Project : bigdata_python_course

import requests
from concurrent.futures import ThreadPoolExecutor
from lxml import etree
import csv

f = open("./新发地.csv", "w", encoding="utf-8", newline='')
csv_write = csv.writer(f)


def download_one_page(data):
    url = "http://www.xinfadi.com.cn/getPriceData.html"
    resp = requests.post(url, data=data)
    dic = resp.json()
    lists = dic["list"]
    for lis in lists:
        prod_name = lis["prodName"]
        low_price = lis["lowPrice"]
        avg_price = lis["avgPrice"]
        high_price = lis["highPrice"]
        spec_info = lis["specInfo"]
        place = lis["place"]
        unit_info = lis["unitInfo"]
        pub_date = lis["pubDate"].split(' ')[0]
        row = [prod_name, low_price, avg_price, high_price, spec_info, place, unit_info, pub_date]
        csv_write.writerow(row)
        print(f"第{data['current']}页下载完成")


if __name__ == '__main__':

    with ThreadPoolExecutor(50) as t:
        for i in range(1, 2001):
            data = {"limit": 20, "current": i}
            t.submit(download_one_page, data=data)
