# _*_ coding : utf-8 _*_
# @Time : 2024/6/18 22:27
# @Author : chalet.you
# @File : 04_pandas
# @Project : bigdata_python_course
from pandas import Series
import numpy as np

s = Series(data=np.random.randint(1, 100, size=(5, )), index=['第1个元素', '第2个元素', '第3个元素', '第4个元素', '第5个元素'])
print(s)


arr = np.random.randint(1, 100, size=(3,5))
print('shape属性值：', arr.shape)
print('size属性值：', arr.size)
print('维度属性值：', arr.ndim)
print('数据类型属性值：', arr.dtype)
