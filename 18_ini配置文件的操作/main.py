# _*_ coding : utf-8 _*_
# @Time : 2024/7/7 16:39
# @Author : chalet.you
# @File : main
# @Project : bigdata_python_course
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")


def login(usernm, passwd):
    data = {"client": "windows"}
    data.update(config.items("user-info"))  # 等同于 data |= config.items("user-info")
    username = data["username"]
    password = data["password"]
    if usernm == username and passwd == password:
        print("登入成功")
    else:
        print("你的账号或者密码错误")


if __name__ == '__main__':
    usernm = input("请输入你的账号:")
    passwd = input("请输入你的密码:")
    login(usernm, passwd)