# _*_ coding : utf-8 _*_
# @Time : 2024/6/14 21:29
# @Author : chalet.you
# @File : 00_demo
# @Project : bigdata_python_course
import sys
from datetime import datetime
import numpy as np


def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b

    return c


def pythonsum(n):
    a = range(n)
    b = range(n)
    c = []
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])

    return c


size = int(sys.argv[1])

start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start
print("The last 3 elements of the sum", c[-2:])
print("PythonSum elapsed time in microseconds", delta.microseconds)

start = datetime.now()
c = numpysum(size)
delta = datetime.now() - start
print("The last 3 elements of the sum", c[-2:])
print("PythonSum elapsed time in microseconds", delta.microseconds)


