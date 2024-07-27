# _*_ coding : utf-8 _*_
# @Time : 2024/4/20 14:26
# @Author : chalet.you
# @File : 07_inheritance_exercise
# @Project : bigdata_python_course

class Computer:

    def __init__(self, cpu, memory, disk):
        self.cpu = cpu
        self.memory = memory
        self.disk = disk

    def get_detail(self):
        return f"cpu = {self.cpu}, memory = {self.memory}, disk = {self.disk}"


class PC(Computer):
    brand = None

    def __init__(self, cpu, memory, disk, brand):
        super().__init__(cpu, memory, disk)
        self.brand = brand

    def print_info(self):
        print(f"brand = {self.brand}, {self.get_detail()}")



class NotePad(Computer):
    color = None

    def __init__(self, cpu, memory, disk, color):
        super().__init__(cpu, memory, disk)
        self.color = color

    def print_info(self):
        print(f"颜色 = {self.color}, {self.get_detail()}")


pc = PC("酷睿i7", 64, "1T", "华硕")
pc.print_info()

note = NotePad("安卓", "32GB", "500GB", "red")
note.print_info()

