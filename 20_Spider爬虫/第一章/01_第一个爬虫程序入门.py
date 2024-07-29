# _*_ coding : utf-8 _*_
# @Time : 2024/7/27 18:17
# @Author : chalet.you
# @File : 01_第一个爬虫程序
# @Project : bigdata_python_course

# 爬虫：通过编写程序来获取互联网上的资源
# 百度
# 需求：用程序模拟浏览器，输入一个网址，从该网址中获取到资源或者内容
from urllib.request import urlopen

url = "http://www.baidu.com"
response = urlopen(url)

with open("./mybaidu.html", mode="w", encoding="utf-8") as f:
    f.write(response.read().decode("utf-8"))  # 读取到网页的页面源代码

print("over!")
