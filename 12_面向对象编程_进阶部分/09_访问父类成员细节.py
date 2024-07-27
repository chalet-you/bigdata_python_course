# _*_ coding : utf-8 _*_
# @Time : 2024/4/20 14:58
# @Author : chalet.you
# @File : 09_访问父类成员细节
# @Project : bigdata_python_course

class Base:
    n3 = 800

    def fly(self):
        print("Base-fly()......")

class A(Base):
    n1 = 100
    __n2= 600

    def run(self):
        print("A-run()......")

    def __jump(self):
        print("A-jump()......")


class B(A):

    def say(self):

        print("say()......")

        print(Base.n3, A.n3, super().n3)

        Base.fly(self)

        A.fly(self)

        super().fly()

b = B()
b.say()


