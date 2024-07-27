# _*_ coding : utf-8 _*_
# @Time : 2024/4/20 13:08
# @Author : chalet.you
# @File : 05_why_inheritance
# @Project : bigdata_python_course

class Student:
    name = None
    age = None
    __score = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"name = {self.name}, age = {self.age}, score = {self.__score}")

    def set_score(self, score):
        self.__score = score

class Pupil(Student):

    def testing(selfs):
        print("小学生在考小学数学")

class Graduate(Student):

    def testing(self):
        print("大学生在考高等数学")


pupil = Pupil("a", 12)
pupil.testing()
pupil.set_score(99)
pupil.show_info()


graduate = Graduate("武汉三", 20)
graduate.testing()
graduate.set_score(100)
graduate.show_info()


