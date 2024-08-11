# _*_ coding : utf-8 _*_
# @Time : 2024/8/10 17:28
# @Author : chalet.you
# @File : 03_防盗链的处理
# @Project : bigdata_python_course



# 1. 拿到contId
# 2. 拿到videoStatus返回的json  -> srcURL
# 3. srcURL里面的内容进行修整
# 4. 下载视频
import requests

# 拉取视频的网址
url = "https://pearvideo.com/video_1795594"
contId = url.split("_")[1]

videoStatusUrl = f"https://pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.8761496131494706"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    # 防盗链：溯源，当前本次请求的上一级是谁
    "referer": url
}

resp = requests.get(videoStatusUrl, headers=headers)
dic = resp.json()


systemTime = dic["systemTime"]
srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")


# 下载视频
with open("a.mp4", "wb" ) as f:
    f.write(requests.get(srcUrl).content)




