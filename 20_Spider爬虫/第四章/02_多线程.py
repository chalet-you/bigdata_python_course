# _*_ coding : utf-8 _*_
# @Time : 2024/8/11 9:58
# @Author : chalet.you
# @File : 01_多线程
# @Project : bigdata_python_course

# 线程，进程
# 进程是资源单位，每一个进程至少有一个线程
# 线程是执行单位

# 多线程第二种写法
from threading import Thread  # 线程类


class MyThread(Thread):
    def run(self):
        for i in range(100):
            print("子线程", i)


if __name__ == '__main__':
    t = MyThread()
    t.start()  # 开始执行该线程

    for i in range(100):
        print("主线程", i)
