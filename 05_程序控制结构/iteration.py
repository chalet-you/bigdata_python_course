# _*_ coding : utf-8 _*_
# @Time : 2024/8/12 22:35
# @Author : chalet.you
# @File : iteration
# @Project : bigdata_python_course


def for_loop(n) -> int:
    res = 0
    for i in range(1, n + 1):
        res += i
    return res


def while_loop(n) -> int:
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 1
        i *= 2
    return res


def nested_for_loop1(n):
    res = ""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res += f"({i},{j})"

    return res


def nested_for_loop(n: int) -> str:
    """双层 for 循环"""
    res = ""
    # 循环 i = 1, 2, ..., n-1, n
    for i in range(1, n + 1):
        # 循环 j = 1, 2, ..., n-1, n
        for j in range(1, n + 1):
            res += f"({i}, {j}), "
    return res


def recur(n):
    if n == 1:
        return 1
    else:
        res = recur(n - 1)
        return n + res


def tail_recur(n, res):
    """尾递归"""
    # 终止条件
    if n == 0:
        return res
    # 尾递归调用
    return tail_recur(n - 1, res + n)


if __name__ == '__main__':
    print(tail_recur(100, 0))
