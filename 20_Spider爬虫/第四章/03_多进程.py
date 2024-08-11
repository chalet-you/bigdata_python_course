# _*_ coding : utf-8 _*_
# @Time : 2024/8/11 10:12
# @Author : chalet.you
# @File : 03_多进程
# @Project : bigdata_python_course

from multiprocessing import Process


def func():
    for i in range(1000):
        print("子进程", i)


if __name__ == '__main__':
    p = Process(target=func)
    p.start()

    for i in range(1000):
        print("主进程", i)
