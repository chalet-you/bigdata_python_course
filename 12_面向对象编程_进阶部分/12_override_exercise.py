# _*_ coding : utf-8 _*_
# @Time : 2024/4/20 15:08
# @Author : chalet.you
# @File : 12_override_exercise
# @Project : bigdata_python_course

class Person:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return f"name:{self.name}, age:{self.age}"


class Student(Person):
    id = None
    score = None

    def __init__(self, name, age, id, score):
        super().__init__(name, age)
        self.id = id
        self.score = score

    def say(self):
        return f"{super().say()}, id:{self.id}, score:{self.score}"


p = Person("张三", 33)
s = Student("李四", 30, "u-110", 100)

print(p.say())
print(s.say())
