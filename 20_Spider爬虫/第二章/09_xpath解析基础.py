# _*_ coding : utf-8 _*_
# @Time : 2024/8/11 11:31
# @Author : chalet.you
# @File : test11
# @Project : bigdata_python_course

import requests
from lxml import etree

xml = """
<table class="hq_table">
    <tr class="tr_color">
        <td>品名</td>
        <td>最低价</td>
        <td>平均价</td>
        <td>最高价</td>
        <td>规格</td>
        <td>单位</td>
        <td>发布时间</td>
    </tr>
    <tr class="tr_color">
        <td>小黄瓜</td>
        <td>4.50</td>
        <td>5.25</td>
        <td>6.00</td>
        <td>旱\荷兰</td>
        <td>斤</td>
        <td>2021-03-11</td>
    </tr>
    <tr class="tr_color">
        <td>大白菜</td>
        <td>1.10</td>
        <td>3.15</td>
        <td>4.00</td>
        <td>上海//崇明</td>
        <td>斤</td>
        <td>2022-10-20</td>
    </tr>
    <tr class="tr_color">
        <td>猪肉</td>
        <td>21.30</td>
        <td>15.50</td>
        <td>12.00</td>
        <td>乌克兰</td>
        <td>斤</td>
        <td>2024-08-11</td>
    </tr>
</table>
"""

tree = etree.XML(xml)

table = tree.xpath("/table")[0]
trs = table.xpath("./tr")[1:]  # 列表切片，切掉表头
for tr in trs:
    lis = tr.xpath("./td/text()")
    res = [li.replace('\\', '').replace('//', '') for li in lis]
    print(res)
