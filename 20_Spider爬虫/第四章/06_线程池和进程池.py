# _*_ coding : utf-8 _*_
# @Time : 2024/8/11 10:25
# @Author : chalet.you
# @File : 06_线程池和进程池
# @Project : bigdata_python_course

# 线程池：一次性开辟一些线程，我们用户直接给线程池提交任务，线程任务的调度交给线程池来完成

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def fn(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        # 提交 100 个线程给这有59个线程的线程池用
        for i in range(100):
            t.submit(fn, name=f"线程{i}")

    # 等待线程池中的任务全部执行完毕，才继续执行（守护进程）
    print("over!!!!")
