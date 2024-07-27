# _*_ coding : utf-8 _*_
# @Time : 2024/4/20 16:20
# @Author : chalet.you
# @File : my_tools
# @Project : bigdata_python_course

def read_confirm_select():
    print("请输入你的选择(Y/N)，请确认选择:", end='')
    while True:
        key = input()
        if key.lower() == 'y' or key.lower() == 'n':
            break
        else:
            print("选择错误, 请重新输入: ", end="")

    return key.lower()


def read_str(tip, default_value):
    key = input(tip)
    if len(key) > 0:
        return key
    else:
        return default_value



