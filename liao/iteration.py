#!/usr/bin/env python3


from collections.abc import Iterable


def findMinAndMax(numbers):
    if len(numbers) == 0:
        return None, None

    min_x = numbers[0]
    max_x = numbers[0]

    for z in numbers:
        if z < min_x:
            min_x = z
        if z > max_x:
            max_x = z
    return min_x, max_x


if __name__ == '__main__':
    # list tuple 可迭代对象
    L = ['Green', 'Bob', 'Cara']
    for value in L:
        print(value)

    Dic = {'a': 1, 'b': 2, 'c': 3}
    for key in Dic:  # 默认是迭代 key
        print(key)
    for item in Dic.values():  # 迭代 values
        print(item)

    for k, v in Dic.items():  # 迭代 key + value
        print('key=', k, 'value=', v)

    # 判断一个对象是否是可迭代对象
    print(isinstance('abc', Iterable))  # str是否可迭代

    for x, y in [(1, 1), (2, 4), (3, 9)]:
        print(x, y)

    if findMinAndMax([]) != (None, None):
        print('1测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('2测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('3测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('4测试失败!')
    else:
        print('测试成功!')
