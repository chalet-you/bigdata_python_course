# _*_ coding : utf-8 _*_
# @Time : 2024/7/16 21:43
# @Author : chalet.you
# @File : demo
# @Project : bigdata_python_course

import json

names = ["Alex大王", "小猪佩奇", "黑姑娘"]

res = json.dumps(names)
print(res)
print('=' * 20)

import pickle

data = {'k1':123, 'k2':'Hello'}
p_str = pickle.dumps(data)
print(p_str)

with open('result.pk', "wb") as fp:
    pickle.dump(data, fp)

f = open("result.pk", "rb")
d = pickle.load(f)
print(d)

