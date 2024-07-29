# _*_ coding : utf-8 _*_
# @Time : 2024/7/17 20:40
# @Author : chalet.you
# @File : 01_excel_base
# @Project : bigdata_python_course

from openpyxl import Workbook

wk = Workbook()
ws = wk.active
ws.title = 'sheet1'

ws.append(['学号','姓名','课程', '分数'])
ws.append(['1001','张三','语文', 92])
ws.append(['1002','李四','数学', 98.5])

wk.save("第一个工作簿.xlsx")
