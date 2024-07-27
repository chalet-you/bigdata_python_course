# _*_ coding : utf-8 _*_
# @Time : 2024/7/7 16:54
# @Author : chalet.you
# @File : 遍历ini文件
# @Project : bigdata_python_course

import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

for section in config.sections():
    print(f"[{section}]")
    for key, value in config.items(section):
        print(f"{key}={value}")
    print("")


