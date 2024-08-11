# _*_ coding : utf-8 _*_
# @Time : 2024/8/10 23:13
# @Author : chalet.you
# @File : 04_代理
# @Project : bigdata_python_course
# 原理，通过第三方的一个机器去发送请求
import requests

# 免费代理IP的网址：https://www.zdaye.com/free/     一般类型为：[透明]是可用的
# 119.123.247.26:9000
proxies = {
    "https": "https://119.123.247.26:9000",
    "http": "http://119.123.247.26:9000"
}
resp = requests.get("https://www.baidu.com", proxies=proxies)
resp.encoding = "UTF-8"
print(resp.text)