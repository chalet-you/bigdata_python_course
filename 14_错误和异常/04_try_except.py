# _*_ coding : utf-8 _*_
# @Time : 2024/4/22 20:59
# @Author : chalet.you
# @File : 04_try_except
# @Project : bigdata_python_course

num1 = 10
num2 = 10

try:
    result = num1 / num2
    str = "hello"
    print("hi......")

# except Exception as e:
#     print("出现异常了", e, f"异常类型是{type(e)}")

except Exception as e:
    print(f"捕获异常，异常是{e}")
else:
    print("执行了else....")
finally:
    print("不管是否发生异常都会执行此行代码")

print("继续执行......")
