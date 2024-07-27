# _*_ coding : utf-8 _*_
# @Time : 2024/4/20 15:46
# @Author : chalet.you
# @File : 15_ploy
# @Project : bigdata_python_course

class A:
    def hi(self):
        print("A-hi()......")


class B:
    def hi(self):
        print("B-hi()......")


def test(obj):
    obj.hi()


a = A()
b = B()

test(a)
test(b)
