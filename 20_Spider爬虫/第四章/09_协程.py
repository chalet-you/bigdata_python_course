# _*_ coding : utf-8 _*_
# @Time : 2024/8/11 15:05
# @Author : chalet.you
# @File : 09_协程
# @Project : bigdata_python_course

import time


def func():
    print("我爱中国")
    time.sleep(3)   # 让当前的线程处于阻塞状态，CPU是不为我工作
    print("我真的爱中国")


if __name__ == '__main__':
    func()


# input() 程序也是处于阻塞状态
# requests.get(B站)  在网络请求返回数据之前，程序也是处于阻塞状态的
# 一般情况下，当程序处于 IO 操作的时候，线程都会处于阻塞状态

# 协程：当程序遇见了IO操作的时候，可以选择性的切换到其他任务上
# 在微观上是一个任务一个任务的进行切换，切换条件一般就是IO操作
# 在宏观上，我们能看到的其实是多个任务一起在执行
# 多任务异步操作

# 上方所讲的一切，都是在单线程的条件下

