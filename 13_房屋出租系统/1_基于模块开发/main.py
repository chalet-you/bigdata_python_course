# _*_ coding : utf-8 _*_
# @Time : 2024/4/20 16:20
# @Author : chalet.you
# @File : main
# @Project : bigdata_python_course

from house_operation import *


def main():
    while True:
        main_menu()
        key = input("请输入你的选择(1-6):")
        if key == "1":
            add_house()
        elif key == "2":
            find_house()
        elif key == "3":
            del_house()
        elif key == "4":
            update()
        elif key == "5":
            list_houses()
        elif key == "6":
            if exit_sys:
                print("你退出了程序，欢迎下次使用")
                break


if __name__ == "__main__":
    main()
