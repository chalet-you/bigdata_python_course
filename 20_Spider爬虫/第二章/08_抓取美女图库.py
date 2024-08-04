# _*_ coding : utf-8 _*_
# @Time : 2024/8/4 11:15
# @Author : chalet.you
# @File : 08_抓取美女图库
# @Project : bigdata_python_course
import requests
from bs4 import BeautifulSoup
import time
import csv

# 1.拿到主页面的源代码。然后提取到子页面的链接地址，href
# 2.通过href拿到子页面的内容。从子页面中找到图片的下载地址  img -> src
# 3.下载图片

domain = "https://www.umei.cc/"
url = "https://www.umei.cc/bizhitupian/meinvbizhi/"
resp = requests.get(url)
resp.encoding = "utf-8"  # 处理乱码
# 定义一个set集合
child_set = set()

# print(resp.text)
# 把源代码交给bs
main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", attrs={"class": "item_list infinite_scroll"}).find_all("a")
# print(alist)


for a in alist:
    # print(a.get("href"))    # 直接通过get就可以拿到属性的值
    path = a.get("href").split("/")[-1]  # 拿到子页面的资源路径
    child_url = url + path  # 拼接出子页面
    # 拿到子页面的url,并且放在set集合中
    child_set.add(child_url)

for child_url in child_set:
    # 拿到子页面的源代码
    child_page_resp = requests.get(child_url)
    child_page_resp.encoding = "utf-8"
    child_page_text = child_page_resp.text
    # 从子页面中拿到图片的下载路径
    child_page = BeautifulSoup(child_page_text, "html.parser")
    div = child_page.find("div", attrs={"class": "big-pic"})
    img = div.find("img")
    src = img.get("src")

    # 下载图片
    img_resp = requests.get(src)
    # img_resp.content                 # 拿到图片的字节
    img_name = src.split("/")[-1]  # 拿到url中的最后一个/以后的内容
    with open("img/" + img_name, "wb") as f:
        f.write(img_resp.content)  # 图片写入文件中

    print("over!!!" + img_name)
    time.sleep(1)

print("all over!!!!!")
