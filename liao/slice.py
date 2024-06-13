#!/usr/bin/env python3


def trim(s):
    # 寻找字符串首部的非空格字符位置
    start = 0
    while start < len(s) and s[start].isspace():
        start += 1

    # 寻找字符串尾部的非空格字符位置
    end = len(s) - 1
    while end >= 0 and s[end].isspace():
        end -= 1

    # 返回中间部分字符串，即去除了首尾空格的字符串
    return s[start:end + 1]


if __name__ == '__main__':
    names = ['Michael', 'Green', 'Tracy', 'Bob', 'Lisa']
    print(names[0:2])
    print(names[:2])  # 0 开始时可以省略
    print(names[-2:-1])  # 倒数第一个索引是 -1
    print(names[-2:])

    L = list(range(100))
    print(L)
    print(L[:10])  # 前10
    print(L[-10:])  # 后10
    print(L[::5])  # 每5个取一个
    # tuple 也是一种 list，唯一区别是 tuple 不可变
    print((0, 1, 2, 3, 4)[:3])
    # 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。字符串也可以用切片操作，只是操作结果仍是字符串
    print('ABCDEFG'[:3])
    print('ABCDEFG'[:])
    print('ABCDEFG'[::2])

