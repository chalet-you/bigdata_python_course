# _*_ coding : utf-8 _*_
# @Time : 2024/4/20 14:48
# @Author : chalet.you
# @File : 08_访问父类成员
# @Project : bigdata_python_course

class A:
    n1 = 100

    def run(self):
        print("A-run()....")

class B(A):
    n1 = 200

    def run(self):
        print(f"B-run()")

    def say(self):
        print(f"父类n1 {A.n1}, 本类的n1 {self.n1}")

        A.run(self)

        self.run()

b = B()
b.say()