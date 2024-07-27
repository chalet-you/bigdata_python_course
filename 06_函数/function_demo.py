# _*_ coding : utf-8 _*_
# @Time : 2024/7/4 21:08
# @Author : chalet.you
# @File : function_demo
# @Project : bigdata_python_course
# coding=utf-8

import configparser
import os


script_directory = os.environ.get('script_directory')

config_file = f'{script_directory}/tools/all.conf'

config = configparser.ConfigParser()
config.optionxform=str
config.read(config_file)


for section in config.sections():
    print(f"[{section}]")
    for key, value in config.items(section):
        print(f"{key} = {value}")
        print("${setValue(%s=%s)}" % (key, value))
        os.environ[key] = value


