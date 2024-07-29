# _*_ coding : utf-8 _*_
# @Time : 2024/7/27 20:55
# @Author : chalet.you
# @File : 02_第二个爬虫程序requests
# @Project : bigdata_python_course
# 安装requests
# pip install requests
# 国内源
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

import requests

keyword = input("请输入你要搜索的关键词:")
url = f"http://www.sogou.com/web?query={keyword}"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
response = requests.get(url, headers = headers)  # 处理了一个小小的反爬

print(response.text)          # 拿到页面的源代码

response.close()  # 关掉 response