#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2float(s):
    dot = s.index('.')
    s = s.replace('.', '')

    def char2num(a):
        return DIGITS[a]

    def fn(x, y):
        return x * 10 + y

    return reduce(fn, map(char2num, s)) / 10**dot


if __name__ == '__main__':
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')
