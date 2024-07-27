# _*_ coding : utf-8 _*_
# @Time : 2024/4/20 16:20
# @Author : chalet.you
# @File : house_operation
# @Project : bigdata_python_course
from my_tools import *

houses = [{"id": 1, "name": "tim", "phone": "112", "address": "海淀", "rent": 200, "state": "未出租"}]
# houses = []
id_count = 1


def main_menu():
    print("房屋出租系统菜单".center(32, "="))
    print("1 新　增　房　源")
    print("2 查　找　房　屋")
    print("3 删　除　房　屋　信　息")
    print("4 修　改　房　屋　信　息")
    print("5 房　屋　列　表")
    print("6 退　　　　　出")


def update():
    print("修改房屋信息".center(32, "="))
    key = int(input("请输入待修改房屋的编号(-1退出):"))
    if key == -1:
        return
    house = find_by_id(key)
    if house:

        house["name"] = read_str(f"姓名({house['name']})", house["name"])
        house["phone"] = read_str(f"电话({house['phone']})", house["phone"])
        house["address"] = read_str(f"地址({house['address']})", house["address"])
        house["rent"] = read_str(f"租金({house['rent']})", house["rent"])
        house["state"] = read_str(f"状态({house['state']})", house["state"])
        print("修改房屋信息成功".center(32, "="))
    else:
        print(f"要修改房屋信息的id{key}不存在".center(32, "="))


def find_house():
    print("查找房屋信息".center(32, "="))
    id = int(input("请输入要查找的id:"))

    house = find_by_id(id)
    if house:
        print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态(未出租/已出租)")
        for value in house.values():
            print(value, end="\t\t")
        print()
    else:
        print(f"查找房屋信息id={id}不存在".center(32, "="))


def exit_sys():
    key = read_confirm_select()
    return key == "y"


def find_by_id(id):
    for house in houses:
        if house["id"] == id:
            return house
    return None


def del_house():
    print("删除房屋信息".center(32, "="))
    key = int(input("请输入待删除房屋的编号(-1退出):"))
    if key == -1:
        return

    choice = read_confirm_select()

    if choice == "y":
        house = find_by_id(key)
        if house:
            houses.remove(find_by_id(key))
            print(f"删除房屋id={key}成功".center(32, "="))
        else:
            print(f"删除房屋id={key}不存在,删除失败".center(32, "="))
    else:
        print("放弃删除房屋信息".center(32, "="))


def add_house():
    print("添加房屋".center(32, "="))
    name = input("姓名：")
    phone = input("电话：")
    address = input("地址：")
    rent = int(input("租金："))
    state = input("状态：")
    global id_count
    id_count += 1
    house = {"id": id_count, "name": name, "phone": phone, "address": address, "rent": rent, "state": state}
    houses.append(house)
    print("添加房屋成功".center(32, "="))


def list_houses():
    print("房屋列表".center(32, "="))
    print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态(未出租/已出租)")
    for house in houses:
        for value in house.values():
            print(value, end="\t\t")
        print()
