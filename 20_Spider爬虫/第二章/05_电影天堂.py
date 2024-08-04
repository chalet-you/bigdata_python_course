# _*_ coding : utf-8 _*_
# @Time : 2024/8/3 18:01
# @Author : chalet.you
# @File : 电影天堂
# @Project : bigdata_python_course

# 1。定位到[华语电视剧]
# 2。从[华语电视剧]中提取到子页面的链接地址
# 3。请求子页面的链接地址，拿到我们想要的下载地址
import requests
import re

domain = "https://www.dygod.net/"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie':'guardok=jR2/u1uE0qudH/f8jMoTWmLpeagfGDAyb12eAG2glRIhXj7NAM0bnzf+UL6B615sJE2N9jS6t3lKnTtv295WFw==; __vtins__KSH97KiL32Rqbx0w=%7B%22sid%22%3A%20%2246b8652b-48e3-5143-9879-1fbbda2da21b%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201722677516711%2C%20%22ct%22%3A%201722675716711%7D; __51uvsct__KSH97KiL32Rqbx0w=1; __51vcke__KSH97KiL32Rqbx0w=f1ef3689-b752-5db4-9488-5345e52e5bbd; __51vuft__KSH97KiL32Rqbx0w=1722675716714; Hm_lvt_f7abbae08c28b34b707daf8674110ce5=1722178285,1722675718; HMACCOUNT=F39642E01D9A7475; __tins__21827803=%7B%22sid%22%3A%201722675718954%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201722677518954%7D; __51cke__=; __51laig__=1; Hm_lpvt_f7abbae08c28b34b707daf8674110ce5=1722679777',
    'priority':'u=0, i',
    'referer':'https://dygod.net/',
    'sec-ch-ua':'"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1'
}

resp = requests.get(domain, headers = headers, verify=False)  # verify = False 去掉安全验证
resp.encoding = "gb2312"   # 指定字符集 charset为 gb2312
# print(resp.text)

# 拿到ul里面的li
obj1 = re.compile(r"迅雷电影资源.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名　(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf">'
                  r'<a href="(?P<download>.*?)">', re.S)

child_href_list = []

result1 = obj1.finditer(resp.text)
ul = result1.__next__().group("ul")

# 提取子页面
result2 = obj2.finditer(ul)
for it in result2:
    child_href = domain + it.group("href").strip("/")
    child_href_list.append(child_href)

# 提取子页面内容：
for href in child_href_list:
    child_resp = requests.get(href, headers = headers, verify= False)
    child_resp.encoding = "gb2312"
    # print(child_resp.text) # 打印子页面内容
    result3 = obj3.finditer(child_resp.text)
    for it in result3:
        print(it.group("movie"))
        print(it.group("download"))





