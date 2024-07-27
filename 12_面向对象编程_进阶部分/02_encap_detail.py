# _*_ coding : utf-8 _*_
# @Time : 2024/4/20 12:48
# @Author : chalet.you
# @File : 02_encap_detail
# @Project : bigdata_python_course

class Clerk:

    name = None
    __job = None
    __salary = None

    def __init__(self, name, job, salary):
        self.name = name
        self.__job = job
        self.__salary = salary

    def get_job(self):
        return self.__job

clerk = Clerk("张三", "python工程师", 20000)

clerk.__job = "Go工程师"

print(clerk.__job)

print(clerk.get_job())