# _*_ coding : utf-8 _*_
# @Time : 2024/4/25 21:14
# @Author : chalet.you
# @File : 09_homework01
# @Project : bigdata_python_course
import time


def operation_menu():
    print()
    print("请选择操作".center(32, "="))
    print("\t\t\t1 查看当前登录用户")
    print("\t\t\t2 查看登录日志")
    print("\t\t\t3 退出系统")


def record_log(username, info):
    with open("log.txt", "a", encoding="UTF-8") as f:
        f.write(f"登入用户：{username}，{info} 登入时间{time.strftime('%m-%d %H:%M:%S', time.localtime(time.time()))}\n")


def read_log():
    with open("log.txt", "r", encoding="UTF-8") as f:
        for line in f:
            print(line.strip())


def main():
    usename = input("请输入用户名:")
    password = input("请输入密码:")

    if usename in ["smith", "tom", "hsp"] and password == "888":
        record_log(usename, "登入成功")
        while True:
            operation_menu()
            choice = input("请输入你的选择:")
            if choice == "1":
                print(f"当前登录用户:{usename}")
            elif choice == "2":
                read_log()
            elif choice == "3":
                return
            else:
                print("你的选择有误，请重新输入")
    else:
        record_log(usename, "登入失败")


if __name__ == "__main__":
    main()
