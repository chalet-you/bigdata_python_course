# _*_ coding : utf-8 _*_
# @Time : 2024/4/20 12:54
# @Author : chalet.you
# @File : 03_encap_exercise
# @Project : bigdata_python_course

class Account:
    __name = None
    __balance = None
    __passwd = None

    def set_name(self, name):
        if 2 <= len(name) <= 4:
            self.__name = name
        else:
            print("名字长度不在2-4位之间")

    def set_balance(self, balance):
        if balance > 20:
            self.__balance = balance
        else:
            print("余额必须大于20")

    def set_passwd(self, passwd):
        if len(passwd) == 6:
            self.__passwd = passwd
        else:
            print("密码必须是6位")

    def query_info(self, name, passwd):
        if self.__name == name and self.__passwd == passwd:
            return f"账号是{self.__name}，余额是{self.__balance}"
        else:
            return "请输入正确的名字和密码"


account = Account()
account.set_name("张三")
account.set_passwd("123456")
account.set_balance(1000)

print(account.query_info("张三","123456"))


