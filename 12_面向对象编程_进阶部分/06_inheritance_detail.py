# _*_ coding : utf-8 _*_
# @Time : 2024/4/20 14:13
# @Author : chalet.you
# @File : 06_inheritance_detail
# @Project : bigdata_python_course

class Base:
    n1= 100
    __a  = None

    def __init__(self):
        print("Base 构造方法")

    def hi(self):
        print("hi() 公共方法")

    def __hello(self):
        print("__hello 私有方法")

class Sub(Base):

    def __init__(self):
        print("Sub 构造方法")

    def say_ok(self):
        print("say_ok()", self.n1)
        self.hi()

sub = Sub()
sub.say_ok()


