# _*_ coding : utf-8 _*_
# @Time : 2024/7/27 22:47
# @Author : chalet.you
# @File : 02_requests入门02
# @Project : bigdata_python_course

import requests

url = "https://fanyi.baidu.com/sug"
keyword = input("请输入你要翻译的单词:")
dat = {"kw": keyword}
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "6",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "BIDUPSID=5630FE329CCDC00DA9C4CB3B08DD796E; PSTM=1693036386; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; smallFlowVersion=old; APPGUIDE_10_7_2=1; newlogin=1; APPGUIDE_10_7_6=1; APPGUIDE_10_7_8=1; MCITY=-289%3A; APPGUIDE_10_7_1=1; BAIDUID=A54E08D0BF9DEBA119229EA4720A7E8B:FG=1; H_WISE_SIDS_BFESS=60276_60446; H_PS_PSSID=60276_60360_60469_60491_60502_60522; H_WISE_SIDS=60276_60360_60469_60491_60502_60522; BDUSS=NMWDFlbEo2UG41LX4tdGpxQ2pZOH43NW9jZVpxcXo5Zm9MVnBGU2RyUDhRTXhtSVFBQUFBJCQAAAAAAAAAAAEAAACp8WssxM~B1sDPue0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPyzpGb8s6RmSX; BDUSS_BFESS=NMWDFlbEo2UG41LX4tdGpxQ2pZOH43NW9jZVpxcXo5Zm9MVnBGU2RyUDhRTXhtSVFBQUFBJCQAAAAAAAAAAAEAAACp8WssxM~B1sDPue0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPyzpGb8s6RmSX; BAIDUID_BFESS=A54E08D0BF9DEBA119229EA4720A7E8B:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=5; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1721142907,1722074853,1722079325,1722089396; HMACCOUNT=F39642E01D9A7475; BA_HECTOR=a0212gala4al8k2k2l8l242gbd938h1jaa15a1u; ZFY=6EZdAnRLfhfLOwVvglwLSiFt6FTn8BWU9EjvGvwIsEQ:C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1722091065; ab_sr=1.0.1_MjE4NzE5ODA0YTEwMDI3MGQzNjkyYjU3M2U3OTQ1YWMwZTczYTFhY2E0NTYyNGYyYTNlYTZmMzljNGY0MjMyMmEzYTRlN2JkNWMzYWE2ZGMzNDAwNTQ4Nzc5ZjBlMGRkNGM0YzUwYTRkY2FmZGY1NTA2ZWVlNGUzNWVjNzNlZWI4MjA4YWJkMTAwMzA4ZGVlMDA1NjMwZjMwZjA5OTU5NTYxMDIwNjM2MDI5OWExMzg0ZjQ2MGM4ZmQ2MmQ0MDJj",
    "Host": "fanyi.baidu.com",
    "Origin": "https://fanyi.baidu.com",
    "Referer": "https://fanyi.baidu.com/",
    "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "Sec-Ch-Ua-Mobile":"?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

# 发送post请求，发送的数据必须放在字典中，通过data参数进行传递
response = requests.post(url, data=dat, headers = headers)

print(response.json())   # 将服务器返回的内容直接处理成json()  ==> dict

response.close()  # 关掉 response