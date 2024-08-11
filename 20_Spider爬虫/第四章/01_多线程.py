# _*_ coding : utf-8 _*_
# @Time : 2024/8/11 9:58
# @Author : chalet.you
# @File : 01_多线程
# @Project : bigdata_python_course

# 线程，进程
# 进程是资源单位，每一个进程至少有一个线程
# 线程是执行单位

# 多线程第一种写法
from threading import Thread # 线程类


def func():
    for i in range(100):
        print("func", i)


if __name__ == '__main__':
    t = Thread(target=func)
    t.start()  # 开始执行该线程

    for i in range(100):
        print("main", i)
