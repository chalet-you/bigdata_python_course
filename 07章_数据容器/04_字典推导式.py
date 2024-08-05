# mew_dictionary = {key_exp:value_exp for key, value in dict.items() if condition}
# 字典推导式说明：
# key: dict.items() 字典中的key
# value: dict.items() 字典中的value
# dict.items(): 序列
# condition：if条件表达式   :  可以用key，也可以用value
# key_exp：在for循环中，如果if条件表达式condition成立(即条件表达式成立)，返回对应的**key,value当作key_exp,value_exp**处理
# value_exp：在for循环中，如果if条件表达式condition成立(即条件表达式成立)，返回对应的**key,value当作key_exp,value_exp**处理
# 这样就返回一个新的字典。

dictionary_1 = {'a': '1234', 'B': 'FFFF', 'c': '23432', 'D': '124fgr', 'e': 'eeeee', 'F': 'QQQQQ'}
# 案例一：获取字典种key值是小写字母的键值对
new_dic_1={key:value for key, value in dictionary_1.items() if key.islower()}
print(new_dic_1) # 打印出：{'a': '1234', 'c': '23432', 'e': 'eeeee'}

# 案例二：将字典中的所有key设置为小写
new_dic_2 = {key.lower() : value for key, value in dictionary_1.items()}
print(new_dic_2)

# 案例三：将字典种的所有key设置小写，value设置为大写
new_dic_3 = {key.lower(): value.upper() for key, value in dictionary_1.items()}
print(new_dic_3)
