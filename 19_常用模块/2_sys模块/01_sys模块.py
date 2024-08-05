# _*_ coding : utf-8 _*_
# @Time : 2024/7/27 16:17
# @Author : chalet.you
# @File : 02_SYS模块
# @Project : bigdata_python_course
"""
sys 模块主要用于与Python解释器进行交互，保活获取和设置解释器的各种参数和状态。
"""
import sys

# sys模块主要用于与Python解释器进行交互，包括获取和设置解释器的各种参数和状态。
print(sys.stdin)  # 标准输入流
print(sys.stdout) # 标准输出流
print(sys.argv)   # 命令行参数列表
# 当我们导入一个模块时：import xxx， 默认情况下python解释器会搜索当前目录、已安装的内置模块和第三方模块。
# 搜索路径存放在sys模块的path中。【即默认搜索路径可以通过sys.path打印查看】
print(sys.path)
# sys.path 是一个列表 list，她里面包含了已经添加到系统的环境变量路径
# 当我们要添加自己的引用模块搜索目录时，可以通过列表 list的append()方法
sys.path.append('../09_异常模块与包')

print(sys.path)

