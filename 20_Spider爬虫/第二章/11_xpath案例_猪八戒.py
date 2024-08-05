# _*_ coding : utf-8 _*_
# @Time : 2024/8/4 21:00
# @Author : chalet.you
# @File : 11_xpath案例_猪八戒.py
# @Project : bigdata_python_course

import requests
from lxml import etree

url = "https://www.zbj.com/fw/?k=saas"
resp = requests.get(url)
lis = []

tree = etree.HTML(resp.text)
divs_list = tree.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div')
for div in divs_list:
    price = div.xpath('./div/div[3]/div[1]/span/text()')[0].strip('¥')
    title_raw = div.xpath('./div/div[3]/div[2]/a/span/text()')
    title_process = 'Saas'.join([ele+'Saas' for ele in title_raw])
    company = div.xpath('./div/div[5]/div/div/div/text()')[0]
    lis.append([price, title_process, company])

print(lis)


