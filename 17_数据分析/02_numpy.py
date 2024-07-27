# _*_ coding : utf-8 _*_
# @Time : 2024/6/12 23:31
# @Author : chalet.you
# @File : 01_numpy
# @Project : bigdata_python_course
import matplotlib.pyplot as plt
import numpy as np

img_arr = plt.imread('F:\datas\图片资源\meimei.jpg')
print(img_arr)

arr1 = np.zeros(shape=(3,2), dtype=int)
print(arr1)

arr2 = np.linspace(0, 100, num=20, dtype=int)
print(arr2)

arr3 = np.arange(3)
print(arr3)

arr4 = np.random.randint(0,100, size=(5,3))
print(arr4)







