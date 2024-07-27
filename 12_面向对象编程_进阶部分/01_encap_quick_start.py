# _*_ coding : utf-8 _*_
# @Time : 2024/4/20 12:05
# @Author : chalet.you
# @File : method_detail
# @Project : bigdata_python_course

class Clerk:
    name = None
    __job = None
    __salary = None

    def __init__(self, name, job, salary):
        self.name = name
        self.__job = job
        self.__salary = salary

    def set_job(self, job):
        self.__job = job

    def get_job(self):

        return self.__job

    def __hi(self):
        print("hi()")

    def f(self):
        self.__hi()


clerk = Clerk("张三", "python工程师", 20000)

print(clerk.name)
clerk.set_job("NLP工程师")
print(clerk.get_job())

clerk.f()
